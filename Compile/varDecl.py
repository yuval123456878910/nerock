import AST
from . import packager
from .returnType import typeMatch
from llvmlite import ir
import Compile.packager
from .dependesise import *
from .global_funcs import FormatType

def GetType(data):
    print(data)
    match data.type:
        case ir.IntType(32):
            return 'i32'
        case ir.FloatType():
            return 'f32'
        case ir.IntType(1):
            return 'i1'



def varDecl(listener, ctx: nerockParser.Decl_varContext):
    if FormatType(ctx.typesKeyword().getText()) != str(listener.last_value.type):
        raise TypeError("Unmaching types in var decleration!", ctx.typesKeyword().getText(),  str(listener.last_value.type))
    var = listener.builder.alloca(listener.last_value.type, name=ctx.ID().getText())
    listener.builder.store(listener.last_value, var)
    listener.variables[ctx.ID().getText()] = var