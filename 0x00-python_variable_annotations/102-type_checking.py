#!/usr/bin/env python3
from typing import Tuple, Any


def zoom_array(lst: Tuple[Any, ...], factor: int = 2) -> Tuple[Any, ...]:
    """
    Zooms tuple by repeating them according to the specified factor.

    Parameters:
        lst (Tuple[Any, ...]): The input tuple.
        factor (int): The zoom factor (default is 2).

    Returns:
        Tuple[Any, ...]: The zoomed-in tuple.
    """
    zoomed_in = tuple(
        item for item in lst
        for i in range(factor)
    )
    return zoomed_in
