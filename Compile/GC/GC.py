from llvmlite import ir

from AST.nerockListener import nerockListener
from AST.nerockParser import nerockParser
from Compile import packager
from Compile.funcDecl import returnLoopType
from Compile.returnType import typeMatch


def getParams(ctx: nerockParser.Func_declerationContext) -> nerockParser.ParamContext:
    return ctx.paramList().param()
def GetOrCreateType(lister,typeReturn, parametersType) -> ir.types.FunctionType:
    Item = lister.FuncTypes.get(packager.Package(typeReturn, parametersType))
    if Item is None:
        TypeReturn = ir.FunctionType(typeReturn, parametersType)
        lister.FuncTypes[packager.Package(typeReturn, parametersType)] = TypeReturn
        return TypeReturn
    return Item

def getReturnType(ctx:nerockParser.Func_declerationContext):
    return ctx.returnFunc().typesKeyword().getText()

def getParams(ctx: nerockParser.Func_declerationContext) -> nerockParser.ParamContext:
    return ctx.paramList().param()
class Var:
    def __init__(self, name):
        self.name = name
        self.refrences = 0

    def AddRefrence(self):
        self.refrences += 1
    def __repr__(self):
        return f"({self.name} : {self.refrences})"

class GC_walk(nerockListener):
    def __init__(self, moudle):
        self.FuncsNames = []
        self.Moudle = moudle
        self.FuncTypes: dict[packager.Package, ir.types.FunctionType] = {}
        self.Funcs: dict[str, ir.Function] = {}
        self.VarsPerFunc: dict[str, dict[str,Var]] = {}
        self.CurrentFuncName = ""

    def NewVar(self,name: str):
        VarList = self.VarsPerFunc[self.CurrentFuncName]
        VarList[name] = Var(name)

    def RefrenceVarFound(self, name: str):
        VarList = self.VarsPerFunc[self.CurrentFuncName]
        VarList[name].AddRefrence()

    def enterFunc_decleration(self, ctx:nerockParser.Func_declerationContext):
        name = ctx.ID().getText()
        self.FuncsNames.append(name)
        self.CurrentFuncName = name
        self.VarsPerFunc[name] = {}
        self.VarsPerFunc[name] = {s.ID().getText():Var(s.ID().getText()) for s in getParams(ctx)}
        returnTypeName = getReturnType(ctx)
        returntype = typeMatch(returnTypeName)
        params = getParams(ctx)
        parameters = returnLoopType(params)
        func_type = GetOrCreateType(self, returntype, parameters)
        name = ctx.ID().getText()
        self.Funcs[name] = ir.Function(self.Moudle, func_type, name=name)

    def enterDecl_var(self, ctx:nerockParser.Decl_varContext):
        self.NewVar(ctx.ID().getText())

    def enterAtom(self, ctx:nerockParser.AtomContext):
        if ctx.ID() is not None:
            name = ctx.ID().getText()
            self.RefrenceVarFound(name)

    def __repr__(self):
        text = ""
        text += f"Funcs: {self.Funcs}\n"
        for funcName, vars in self.VarsPerFunc.items():
            text += f"{funcName}: {vars}\n"
        return text
