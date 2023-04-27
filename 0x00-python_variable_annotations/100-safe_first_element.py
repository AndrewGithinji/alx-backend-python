#!/usr/bin/env python3
"""100-safe_first_element.py"""

from typing import Any, Sequence, Union


def safe_first_element(lst: Sequence[Any]) -> Union[Any, None]:
    """Returns the first element of a list"""
    if lst:
        return lst[0]
    else:
        return None
