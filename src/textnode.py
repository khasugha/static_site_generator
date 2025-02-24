from enum import Enum
from typing import Optional

class TextType(Enum):
    NORMAL = "normal"
    BOLD = "bold"
    ITALIC = "italic"
    CODE = "code"
    LINK = "link"
    IMAGE = "image"

class TextNode:
    def __init__(self, text: str, text_type: TextType, url: Optional[str] = None):
        if not isinstance(text_type, TextType):
            raise ValueError(f"text_type must be an instance of TextType Enum, got {type(text_type)}")
        self.text = text
        self.text_type = text_type
        self.url = url

    def __eq__(self, target):
        return (
            self.text == target.text and
            self.text_type == target.text_type and
            self.url == target.url
        )

    def __repr__(self):
        return (f"TextNode({self.text}, {self.text_type.value   }, {self.url})")

