from abc import ABC, abstractmethod
from PIL import Image

class LayoutInterface(ABC):
    @abstractmethod
    def apply_layout(self) -> Image:
        pass