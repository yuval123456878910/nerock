
import AST
from . import packager
from .returnType import typeMatch
from llvmlite import ir
import Compile.packager

def getReturnType(ctx: AST.nerockParser.nerockParser.Func_declerationContext):
    return ctx.returnFunc().typesKeyword().getText()

def getParams(ctx: AST.nerockParser.nerockParser.Func_declerationContext) -> AST.nerockParser.nerockParser.ParamContext:
    return ctx.paramList().param()

def returnLoopType(params: list[AST.nerockParser.nerockParser.ParamContext]):
    if len(params) == 0:
        return []
    returnData = []
    for param in params:
        typeGot = typeMatch(param.typesKeyword().getText())
        returnData.append(typeGot)
    return returnData

def GetOrCreateType(lister,typeReturn, parametersType) -> ir.types.FunctionType:
    Item = lister.FuncTypes.get(packager.Package(typeReturn, parametersType))
    if Item is None:
        TypeReturn = ir.FunctionType(typeReturn, parametersType)
        lister.FuncTypes[packager.Package(typeReturn, parametersType)] = TypeReturn
        return TypeReturn
    return Item

def addArgss(lister, params: list[AST.nerockParser.nerockParser.ParamContext], args):
    for param, arg in zip(params, args):
        name = param.ID().getText()
        slot = lister.builder.alloca(arg.type, name=name)
        lister.builder.store(arg,slot)
        lister.variables[name] = slot

def funcDecl(lister, ctx: AST.nerockParser.nerockParser.Func_declerationContext):

    params = getParams(ctx)
    name = ctx.ID().getText()
    lister.CurrentFunc = lister.Funcs[name]

    lister.block = lister.CurrentFunc.append_basic_block("entry")
    lister.builder = ir.IRBuilder(lister.block)
    addArgss(lister, params, lister.CurrentFunc.args)

    lister.Funcs[name] = lister.CurrentFunc
