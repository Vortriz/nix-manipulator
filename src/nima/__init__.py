"""
High-level example usage of the Nix manipulator library.
"""

from nima.expressions import NixSourceCode
from nima.manipulations import remove_value, set_value
from nima.parser import parse
from nima.serializer import to_dict, to_nix

__all__ = [
    "parse",
    "to_nix",
    "to_dict",
    "set_value",
    "remove_value",
    "NixSourceCode",
]
