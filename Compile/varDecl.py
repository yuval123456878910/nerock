import AST
from . import packager
from .returnType import typeMatch
from llvmlite import ir
import Compile.packager
from .dependesise import *
from .global_funcs import FormatType

def GetType(data):
    print(data)
    if isinstance(data, ir.IntType):
        return 'i32'
    elif isinstance(data, ir.FloatType):
        return 'f32'



def varDecl(listener, ctx: nerockParser.Decl_varContext):
    if FormatType(ctx.typesKeyword().getText()) != str(listener.last_value.type):
        raise TypeError("Unmaching types in var decleration!", ctx.typesKeyword().getText(),  str(listener.last_value.type))
    var = listener.builder.alloca(listener.last_value.type, name=ctx.ID().getText())
    listener.builder.store(listener.last_value, var)
    listener.variables[ctx.ID().getText()] = var