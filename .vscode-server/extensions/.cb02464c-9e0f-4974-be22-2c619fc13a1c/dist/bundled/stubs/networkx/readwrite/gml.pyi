from collections.abc import Iterable
from typing import Any, Callable
import html.entities as htmlentitydefs
import re
import warnings
from ast import literal_eval
from collections import defaultdict
from enum import Enum
from io import StringIO
from typing import Any, NamedTuple

from ..classes.graph import Graph
from ..exception import NetworkXError
from ..utils import open_file

__all__ = ["read_gml", "parse_gml", "generate_gml", "write_gml"]

def escape(text): ...
def unescape(text): ...
def literal_destringizer(rep: str) -> Any: ...
def read_gml(path, label: str = "label", destringizer: Callable | None = None): ...
def parse_gml(
    lines: str | Iterable[str],
    label: str = "label",
    destringizer: Callable | None = None,
): ...

class Pattern(Enum):

    KEYS = ...
    REALS = ...
    INTS = ...
    STRINGS = ...
    DICT_START = ...
    DICT_END = ...
    COMMENT_WHITESPACE = ...

class Token(NamedTuple):
    category: Pattern = ...
    value: Any = ...
    line: int = ...
    position: int = ...

LIST_START_VALUE: str = ...

def parse_gml_lines(lines, label, destringizer): ...
def literal_stringizer(value: Any) -> str: ...
def generate_gml(G: Graph, stringizer: Callable | None = None): ...
def write_gml(G: Graph, path, stringizer: Callable | None = None): ...
