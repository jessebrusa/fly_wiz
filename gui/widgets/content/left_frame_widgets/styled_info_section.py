from .base_section import BaseSection

class StyledInfoSection(BaseSection):
    def __init__(self, parent, ui_helpers):
        super().__init__(parent, ui_helpers, 'Styled\nInfo')