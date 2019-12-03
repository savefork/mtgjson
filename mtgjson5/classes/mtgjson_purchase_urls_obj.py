"""
MTGJSON container for Purchase URLs
"""
from typing import Any, Dict, Set

from mtgjson5.globals import to_camel_case


class MtgjsonPurchaseUrlsObject:
    """
    Container for purchase affiliate URLs
    """

    cardmarket: str
    tcgplayer: str
    mtgstocks: str

    def __init__(self) -> None:
        pass

    def build_keys_to_skip(self) -> Set[str]:
        """
        Build this object's instance of what keys to skip under certain circumstances
        :return What keys to skip over
        """
        excluded_keys = set()

        for _, value in self.__dict__.items():
            if not value:
                excluded_keys.add(value)

        return excluded_keys

    def for_json(self) -> Dict[str, Any]:
        """
        Support json.dumps()
        :return: JSON serialized object
        """
        skip_keys = self.build_keys_to_skip()

        return {
            to_camel_case(key): value
            for key, value in self.__dict__.items()
            if not key.startswith("__") and not callable(value) and key not in skip_keys
        }
