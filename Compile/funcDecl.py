
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
        return typeMatch('v')
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
    returnTypeName = getReturnType(ctx) 
    returntype = typeMatch(returnTypeName)
    params = getParams(ctx)
    parameters = returnLoopType(params)
    func_type = GetOrCreateType(lister ,returntype, parameters)
    name = ctx.ID().getText()
    lister.CurrentFunc = ir.Function(lister.Moudle, func_type, name=name)

    lister.block = lister.CurrentFunc.append_basic_block("entry")
    lister.builder = ir.IRBuilder(lister.block)
    addArgss(lister, params, lister.CurrentFunc.args)

    lister.Funcs[name] = lister.CurrentFunc
