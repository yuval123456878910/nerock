import AST
from . import packager
from .returnType import typeMatch
from llvmlite import ir
import Compile.packager
from .dependesise import *


def GetType(data):
    print(data)
    if isinstance(data, ir.IntType):
        return 'i32'
    elif isinstance(data, ir.FloatType):
        return 'f32'

def varDecl(listener, ctx: nerockParser.Decl_varContext):
    if ctx.typesKeyword().getText() != str(listener.last_value.type):
        raise TypeError("Unmaching types in var decleration!")
    listener.builder.alloca(listener.last_value.type, ctx.ID())