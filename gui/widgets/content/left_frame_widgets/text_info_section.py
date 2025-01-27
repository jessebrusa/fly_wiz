from .base_section import BaseSection

class TextInfoSection(BaseSection):
    def __init__(self, parent, ui_helpers):
        super().__init__(parent, ui_helpers, 'Text\nInfo')