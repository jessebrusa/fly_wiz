from .base_section import BaseSection

class TextInfoSection(BaseSection):
    def __init__(self, parent):
        super().__init__(parent, 'Text\nInfo')