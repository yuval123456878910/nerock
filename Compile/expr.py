
import AST
from . import packager
from .returnType import typeMatch
from AST.nerockParser import nerockParser
from llvmlite import ir
import Compile.packager

def add(listener, ctx: nerockParser.ExprContext):
    exprValueLeft = listener.values[ctx.expr(0)]
    exprValueRight = listener.values[ctx.expr(1)]
    if exprValueLeft.type != exprValueRight.type:
        raise TypeError("The two expr given aren't the same type! 1. "+exprValueLeft.type+" 2. "+ exprValueRight.type)
    add = None
    match str(exprValueLeft.type):
        case 'i32':
            add = listener.builder.add(exprValueLeft, exprValueRight)
        case 'f32':
            add = listener.builder.fadd(exprValueLeft, exprValueRight)
    listener.last_value = add
    listener.values[ctx] = add

def LoadID(listener, ctx: nerockParser.ExprContext):
    print(listener.variables)
    var = listener.variables[ctx.atom().ID().getText()]
    if var is None:
        raise NameError(var, "is not defined!")
    
    returnData = listener.builder.load( var, name=ctx.atom().ID().getText())
    
    listener.last_value = returnData
    listener.values[ctx] = returnData
    

def Expr(listener, ctx: nerockParser.ExprContext):
    if ctx.atom() is not None:
        if ctx.atom().NUM() is not None:
            listener.last_value = ir.IntType(32)(int(ctx.atom().NUM().getText()))
            listener.values[ctx] = listener.last_value
        if ctx.atom().FLOAT() is not None:
            listener.last_value = ir.FloatType()(float(ctx.atom().FLOAT().getText()))
            listener.values[ctx] = listener.last_value
        elif ctx.atom().ID() is not None:
            LoadID(listener, ctx)
    if ctx.PLUS() is not None:
        Expr(listener, ctx.expr(0))
        Expr(listener, ctx.expr(1))
        add(listener, ctx)
        

