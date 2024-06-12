from dataclasses import dataclass
from pathlib import Path

from PIL.Image import Image
import torch
from transformers import AutoProcessor, PaliGemmaForConditionalGeneration, BitsAndBytesConfig
# TODO: fetch model weights and config from hf and cache them


@dataclass
class VLM:
  cache_dir: Path
  model_name: str

  def __post_init__(self):
    self.cache_dir = self.cache_dir / 'models'
    self.cache_dir.mkdir(exist_ok=True, parents=True)
    # model_dir = self.cache_dir / 'paligemma-3b-mix-224'
    # model_dir.mkdir(exist_ok=True, parents=True)
    # config_path = model_dir / 'config.json'
    # model_path = model_dir / 'pytorch_model.bin'
    self.setup()

  def setup(self):
    nf4_config = BitsAndBytesConfig(
      load_in_4bit=True,
      bnb_4bit_quant_type='nf4',
      bnb_4bit_use_double_quant=True,
      bnb_4bit_compute_dtype=torch.bfloat16,
    )
    self.device = torch.device('cuda' if torch.cuda.is_available() else 'cpu')
    self.model_name = 'google/paligemma-3b-mix-224'
    self.model = PaliGemmaForConditionalGeneration.from_pretrained(
      self.model_name, quantization_config=nf4_config
    ).eval()
    self.processor = AutoProcessor.from_pretrained(self.model_name)

  def generate(self, query: str, image: Image) -> str:
    inputs = self.processor(
      text=query,
      images=image,
      return_tensors='pt',
      do_convert_rgb=True,
    ).to(self.device)
    inputs = inputs.to(dtype=self.model.dtype)
    input_len = inputs['input_ids'].shape[-1]
    # with torch.no_grad():
    #   outputs = self.model.generate(**inputs, max_length=496)  # 496 is the maximum token length for this size
    with torch.inference_mode():
      generation = self.model.generate(**inputs, max_new_tokens=100, do_sample=False)
      generation = generation[0][input_len:]
      decoded = self.processor.decode(generation, skip_special_tokens=True)
    return decoded  # self.processor.decode(outputs[0], skip_special_tokens=True)
