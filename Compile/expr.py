
import AST
from . import packager
from .returnType import typeMatch
from AST.nerockParser import nerockParser
from llvmlite import ir
import Compile.packager

def Expr(listener, ctx: nerockParser.ExprContext):
    if ctx.atom() is not None:

        if ctx.atom().NUM() is not None:
            listener.last_value = ir.IntType(32)(int(ctx.atom().NUM().getText()))
            listener.values[ctx] = listener.last_value


