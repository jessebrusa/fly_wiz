from .base_section import BaseSection

class TitleSection(BaseSection):
    def __init__(self, parent):
        super().__init__(parent, 'Title')