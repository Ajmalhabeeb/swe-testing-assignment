from __future__ import annotations
import ast
import operator as op

_ALLOWED_OPS = {
    ast.Add: op.add,
    ast.Sub: op.sub,
    ast.Mult: op.mul,
    ast.Div: op.truediv,
    ast.USub: op.neg,
    ast.UAdd: op.pos,
}

class CalcError(ValueError):
    """Raised for invalid calculator expressions or divide-by-zero."""

def evaluate(expression: str) -> float:
    """
    Evaluate a math expression containing +, -, *, /, parentheses, decimals.
    Raises CalcError for invalid input or division by zero.
    """
    expression = (expression or "").strip()
    if not expression:
        raise CalcError("Empty expression")

    try:
        node = ast.parse(expression, mode="eval").body
        return _eval_node(node)
    except ZeroDivisionError as e:
        raise CalcError("Division by zero") from e
    except CalcError:
        raise
    except Exception as e:
        raise CalcError("Invalid expression") from e

def _eval_node(node) -> float:
    if isinstance(node, ast.Constant) and isinstance(node.value, (int, float)):
        return float(node.value)

    if isinstance(node, ast.UnaryOp) and type(node.op) in _ALLOWED_OPS:
        return float(_ALLOWED_OPS[type(node.op)](_eval_node(node.operand)))

    if isinstance(node, ast.BinOp) and type(node.op) in _ALLOWED_OPS:
        left = _eval_node(node.left)
        right = _eval_node(node.right)
        return float(_ALLOWED_OPS[type(node.op)](left, right))

    raise CalcError("Unsupported operation")