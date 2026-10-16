import AST
from . import packager
from .returnType import typeMatch
from AST.nerockParser import nerockParser
from llvmlite import ir
import Compile.packager
from . import funcDecl
from .global_funcs import FormatType

MallocName = "malloc"
def mallocCreate(lis, ctx: nerockParser.Decl_mallocContext):
    name = ctx.ID().getText()
    size_value = lis.values[ctx.expr()]

    i8 = ir.IntType(8)
    size_type = ir.IntType(64)

    malloc_type = ir.FunctionType(i8.as_pointer(), [size_type])
    malloc = funcDecl.ExistFunc(lis, MallocName)

    if malloc is None:
        malloc = ir.Function(lis.Moudle, malloc_type, name=MallocName)
        lis.Funcs[MallocName] = malloc
    elif malloc.function_type != malloc_type:
        raise TypeError("malloc was already declared with a different function type")

    if size_value.type.width > size_type.width:
        size = lis.builder.trunc(size_value, size_type)
    elif size_value.type.width < size_type.width:
        size = lis.builder.zext(size_value, size_type)
    else:
        size = size_value

    ptr = lis.builder.call(malloc, [size], name=name)
    
    slot = lis.builder.alloca(ptr.type, name=f"{name}.addr")
    lis.builder.store(ptr, slot)
    lis.variables[name] = slot

    lis.last_value = ptr
    lis.values[ctx] = ptr
    lis.mallocated_vars.append(ptr)