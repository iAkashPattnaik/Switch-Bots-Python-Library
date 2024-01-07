from swibots.utils.types import JSONDict
from .types import Component
from typing import List, Optional, Any, Dict
from .ListItem import ListItem


class Dropdown(Component):
    type = "dropdown"

    def __init__(
        self,
        placeholder: str = None,
        selected: int = None,
        options: List[ListItem] = None,
        disabled: bool = None,
    ):
        self.disabled = disabled
        self.options = options
        self.selected = selected
        self.placeholder = placeholder

    def to_json(self) -> JSONDict:
        data = {
            "type": self.type,
            "placeHolder": self.placeholder,
            "options": [listitem.to_json() for listitem in self.options],
            "disabled": self.disabled,
        }
        if self.selected:
            data["selectedIndex"] = self.selected
        return data
