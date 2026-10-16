
import AST
from . import packager
from .returnType import typeMatch
from AST.nerockParser import nerockParser
from llvmlite import ir
import Compile.packager
from .global_funcs import FormatType


def add(listener, ctx: nerockParser.ExprContext):
    exprValueLeft = listener.values[ctx.expr(0)]
    exprValueRight = listener.values[ctx.expr(1)]
    if exprValueLeft.type != exprValueRight.type:
        raise TypeError("The two expr given aren't the same type! 1. "+exprValueLeft.type+" 2. "+ exprValueRight.type)
    add = None
    match FormatType(str(exprValueLeft.type)):
        case 'i32' | 'i64':
            add = listener.builder.add(exprValueLeft, exprValueRight)
        case 'f32' |  'f64':
            add = listener.builder.fadd(exprValueLeft, exprValueRight)
    listener.last_value = add
    listener.values[ctx] = add

def sub(listener, ctx: nerockParser.ExprContext):
    exprValueLeft = listener.values[ctx.expr(0)]
    exprValueRight = listener.values[ctx.expr(1)]
    if exprValueLeft.type != exprValueRight.type:
        raise TypeError("The two expr given aren't the same type! 1. "+exprValueLeft.type+" 2. "+ exprValueRight.type)
    sub = None
    match FormatType(str(exprValueLeft.type)):
        case 'i32' | 'i64':
            sub = listener.builder.sub(exprValueLeft, exprValueRight)
        case 'f32' | 'f64':
            sub = listener.builder.fsub(exprValueLeft, exprValueRight)
    listener.last_value = sub
    listener.values[ctx] = sub


def multiply(listener, ctx: nerockParser.ExprContext):
    left = listener.values[ctx.expr(0)]
    right = listener.values[ctx.expr(1)]
    if left.type != right.type:
        raise TypeError(f"Cannot multiply values of different types: {left.type} and {right.type}")

    match FormatType(str(left.type)):
        case 'i32' | 'i64':
            result = listener.builder.mul(left, right)
        case 'f32' | 'f64':
            result = listener.builder.fmul(left, right)
        case _:
            raise TypeError(f"Multiplication is not supported for type {left.type}")

    listener.last_value = result
    listener.values[ctx] = result

def div(listener, ctx: nerockParser.ExprContext):
    left = listener.values[ctx.expr(0)]
    right = listener.values[ctx.expr(1)]

    if left.type != right.type:
        raise TypeError("Not the same type during divition")

    match FormatType(str(right.type)):
        case 'i32' | 'i64':
            result = listener.builder.sdiv(left, right)
        case 'f32' | 'f64':
            result = listener.builder.fdiv(left, right)


    listener.last_value = result
    listener.values[ctx] = result
def LoadID(listener, ctx: nerockParser.ExprContext):
    var = listener.variables.get(ctx.atom().ID().getText())
    if var is None:
        raise NameError(var, "is not defined!")

    returnData = listener.builder.load(var, name=ctx.atom().ID().getText())
    
    listener.last_value = returnData
    listener.values[ctx] = returnData

def Condition_BIGGER_L(listener, ctx: nerockParser.ExprContext):
    expr1 = listener.values[ctx.expr(0)]
    expr2 = listener.values[ctx.expr(1)]

    if expr1.type != expr2.type:
        raise TypeError("Comperetion type arnt the same")
    ConditionValue = None
    match FormatType(str(expr1.type)):
        case 'i32' | 'i64':
            ConditionValue = listener.builder.icmp_signed(">", expr1, expr2)
        case 'f32' | 'f64':
            ConditionValue = listener.builder.fcmp_ordered(">",expr1, expr2)

    listener.last_value = ConditionValue
    listener.values[ctx] = ConditionValue

def LoadString(listener, ctx: nerockParser.ExprContext):
    text = ctx.getText()[1:-1] # bewere the getText gets: "<text>" insted of <text>

    text = (
    text.replace(r"\n", "\n")
        .replace(r"\r", "\r")
        .replace(r"\t", "\t")
        .replace(r"\\", "\\")
        .replace(r"\"", '"')
        .replace(r"\'", "'")
    )

    encoded_text =  bytearray(text.encode("utf-8") + b"\x00")
    arrayType = ir.ArrayType(ir.IntType(8), len(encoded_text))
    str_const = ir.Constant(arrayType, encoded_text)
    auto_name = listener.Moudle.get_unique_name("") 
    GlobalVariable = ir.GlobalVariable(listener.Moudle, str_const.type, name=auto_name)
    GlobalVariable.global_constant = True
    GlobalVariable.initializer = str_const
    zero = ir.Constant(ir.IntType(32), 0)
    ptr = listener.builder.gep(GlobalVariable, [zero, zero])
    listener.last_value = ptr
    listener.values[ctx] = ptr

# insted of malloc every time, use a function to use repitedly
def FastMalloc(PointerSize, Size):
    pass

def Expr(listener, ctx: nerockParser.ExprContext):
    if ctx in listener.values:
        return listener.values[ctx]
    if ctx.atom() is not None:
        if ctx.atom().NUM() is not None:
            listener.last_value = ir.IntType(32)(int(ctx.atom().NUM().getText()))
            listener.values[ctx] = listener.last_value
        if ctx.atom().FLOAT() is not None:
            listener.last_value = ir.FloatType()(float(ctx.atom().FLOAT().getText()))
            listener.values[ctx] = listener.last_value
        elif ctx.atom().ID() is not None:
            LoadID(listener, ctx)

        elif ctx.atom().STRING() is not None:
            LoadString(listener, ctx)

    if ctx.PLUS() is not None:
        Expr(listener, ctx.expr(0))
        Expr(listener, ctx.expr(1))
        add(listener, ctx)

    if ctx.MIN() is not None:
        Expr(listener, ctx.expr(0))
        Expr(listener, ctx.expr(1))
        sub(listener, ctx)

    if ctx.MUL() is not None:
        Expr(listener, ctx.expr(0))
        Expr(listener, ctx.expr(1))
        multiply(listener, ctx)
    if ctx.DIV() is not None:
        Expr(listener, ctx.expr(0))
        Expr(listener, ctx.expr(1))
        div(listener, ctx)

    if ctx.call() is not None:
        call = ctx.call()
        name = call.ID().getText()
        args = ReadArgs(listener,call.expr())
        if name not in listener.GC_LOAD_FUNCTIONS and name not in listener.Funcs:
            raise NameError(name, "is not defined!")
        call = listener.builder.call(listener.Funcs[name], args, name=name)
        listener.last_value = call
        listener.values[ctx] = call

    if ctx.BIGGER_L() is not None:
        Expr(listener, ctx.expr(0))
        Expr(listener, ctx.expr(1))
        Condition_BIGGER_L(listener, ctx)


def ReadArgs(listener, exprs):
    data = []
    for expr in exprs:
        Expr(listener, expr)
        data.append(  listener.values[expr] )
    return data
