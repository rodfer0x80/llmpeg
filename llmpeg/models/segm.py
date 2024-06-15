from dataclasses import dataclass
from pathlib import Path

#TODO: https://huggingface.co/pyannote/segmentation-3.0
@dataclass
class Segmentation:
    cache_dir: Path
    model: str = 'pyannote/segmentation-3.0'

    def __post_init__(self):
        self.cache_dir = self.cache_dir / 'models'
        self.cache_dir.mkdir(exist_ok=True, parents=True)
        self._setup()

    def _setup(self):
        return 0
    
    def infer(self, query: str) -> str:
        return query
    