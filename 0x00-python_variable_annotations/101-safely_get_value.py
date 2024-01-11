#!/usr/bin/env python3
from typing import TypeVar, Dict, Optional


T = TypeVar('T')

def safely_get_value(dct: Dict[str, T], key: str, default: Optional[T] = None) -> T:
    """
    Safely gets a value If the key exists, returns the corresponding value;
    otherwise, returns the default value.

    Parameters:
        dct (Dict[str, T]): The input dictionary.
        key (str): The key to look up in the dictionary.
        default (Optional[T]): The default value to return if the key is not present (default is None).

    Returns:
        T: The value corresponding to the key if the key exists; otherwise, the default value.
    """
    if key in dct:
        return dct[key]
    else:
        return default
