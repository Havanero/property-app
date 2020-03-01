from functools import partial
from typing import Any, Callable, Dict, Optional, Union


def _get_value(
    dict_obj: Dict,
    key,
    default: Optional[Callable[..., Any]] = None,
    coerce: Optional[Callable[..., Any]] = None,
) -> Optional[Any]:

    if default is not None and not callable(default):

        def default():
            return default

    if coerce is None:

        def coerce(x):
            return x

    try:
        result = dict_obj[key]
    except KeyError:
        result = None

    if result is not None:
        try:
            return coerce(result)
        except ValueError:
            pass

    return default() if default else None


def get_int(
    dict_obj: Dict, key: Any, default: Union[int, Callable[..., int], None] = None,
) -> Optional[int]:
    return _get_value(dict_obj, key, default=default, coerce=int)


def get_str(
    dict_obj: Dict, key: Any, default: Union[str, Callable[..., str], None] = None,
) -> Optional[int]:
    return _get_value(dict_obj, key, default=default, coerce=str)
