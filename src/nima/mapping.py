from __future__ import annotations

from nima.expressions.assertion import Assertion
from nima.expressions.binary import BinaryExpression
from nima.expressions.binding import Binding
from nima.expressions.comment import Comment
from nima.expressions.ellipses import Ellipses
from nima.expressions.expression import NixExpression, TypedExpression
from nima.expressions.function.call import FunctionCall
from nima.expressions.function.definition import FunctionDefinition
from nima.expressions.indented_string import IndentedString
from nima.expressions.inherit import Inherit
from nima.expressions.let import LetExpression
from nima.expressions.list import NixList
from nima.expressions.parenthesis import Parenthesis
from nima.expressions.path import NixPath
from nima.expressions.primitive import Primitive
from nima.expressions.select import Select
from nima.expressions.set import AttributeSet, RecursiveAttributeSet
from nima.expressions.unary import UnaryExpression
from nima.expressions.with_statement import WithStatement

EXPRESSION_TYPES: set[type[TypedExpression]] = {
    Assertion,
    BinaryExpression,
    NixList,
    AttributeSet,
    RecursiveAttributeSet,
    Select,
    WithStatement,
    Inherit,
    NixPath,
    FunctionCall,
    FunctionDefinition,
    Comment,
    Primitive,
    LetExpression,
    Binding,
    IndentedString,
    Parenthesis,
    Ellipses,
    UnaryExpression,
}

TREE_SITTER_TYPE_TO_EXPRESSION: dict[str, type[TypedExpression]] = {
    tree_sitter_type: expression_type
    for expression_type in EXPRESSION_TYPES
    for tree_sitter_type in expression_type.tree_sitter_types
}


def tree_sitter_node_to_expression(node) -> NixExpression:
    return TREE_SITTER_TYPE_TO_EXPRESSION[node.type].from_cst(node)
