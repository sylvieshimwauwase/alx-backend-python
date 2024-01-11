#!/usr/bin/env python3
from typing import Sequence, Any, Union, Optional


def safe_first_element(lst: Sequence[Any]) -> Union[Any, None]:
    """
    Returns the first element of the list if it exists, otherwise returns None.

    Parameters:
        lst (list): The input list.

    Returns:
        Optional[Any]: The first element if the list is empty.
    """
    if lst:
        return lst[0]
    else:
        return None
