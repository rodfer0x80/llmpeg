from dataclasses import dataclass
from PIL.Image import Image

from transformers import (
    BitsAndBytesConfig,
    PaliGemmaProcessor,
    PaliGemmaForConditionalGeneration,
)
import torch


@dataclass
class VLM:
    def __post_init__(self):
        nf4_config = BitsAndBytesConfig(
            load_in_4bit=True,
            bnb_4bit_quant_type='nf4',
            bnb_4bit_use_double_quant=True,
            bnb_4bit_compute_dtype=torch.bfloat16,
        )
        self.device = torch.device('cuda' if torch.cuda.is_available() else 'cpu')
        model_id = 'google/paligemma-3b-mix-224'
        self.model = PaliGemmaForConditionalGeneration.from_pretrained(
            model_id,
            torch_dtype=torch.bfloat16,
            quantization_config=nf4_config,
            device_map={'': 0},
        )  # device=self.device
        self.processor = PaliGemmaProcessor.from_pretrained(model_id)

    def generate(self, query: str, image: Image) -> str:
        inputs = self.processor(
            text=query,
            images=image,
            return_tensors='pt',
            do_convert_rgb=True,
        ).to(self.device)
        inputs = inputs.to(dtype=self.model.dtype)
        with torch.no_grad():
            outputs = self.model.generate(**inputs, max_length=496)
        return self.processor.decode(outputs[0], skip_special_tokens=True)
