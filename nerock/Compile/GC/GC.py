from llvmlite import ir

from AST.nerockListener import nerockListener
from AST.nerockParser import nerockParser
from Compile import packager
from Compile.funcDecl import returnLoopType
from Compile.returnType import typeMatch


def getParams(ctx: nerockParser.Func_declerationContext):
    return ctx.paramList().param()


def GetOrCreateType(lister, typeReturn, parametersType) -> ir.types.FunctionType:
    key = packager.Package(typeReturn, parametersType)
    function_type = lister.FuncTypes.get(key)
    if function_type is None:
        function_type = ir.FunctionType(typeReturn, parametersType)
        lister.FuncTypes[key] = function_type
    return function_type


def getReturnType(ctx: nerockParser.Func_declerationContext):
    return ctx.returnFunc().typesKeyword().getText()


class MallocVar:
    """A heap allocation tracked by the compiler's GC analysis pass."""

    def __init__(self, name: str):
        self.name = name
        self.refrences = 0

    def AddRefrence(self):
        self.refrences += 1

    def __repr__(self):
        return f"({self.name} : {self.refrences})"


class GC_walk(nerockListener):
    def __init__(self, moudle: ir.Module):
        self.FuncsNames = []
        self.Moudle = moudle
        self.FuncTypes: dict[packager.Package, ir.types.FunctionType] = {}
        self.Funcs: dict[str, ir.Function] = {}
        self.VarsPerFunc: dict[str, dict[str, MallocVar]] = {}
        self.CurrentFuncName = ""

        # Make free available to the compile listener through the shared Funcs map.
        free_type = ir.FunctionType(ir.VoidType(), [ir.IntType(8).as_pointer()])
        self.Funcs["free"] = ir.Function(moudle, free_type, name="free")

    def NewMallocVar(self, name: str):
        self.VarsPerFunc[self.CurrentFuncName][name] = MallocVar(name)

    def RefrenceVarFound(self, name: str):
        variables = self.VarsPerFunc.get(self.CurrentFuncName, {})
        variable = variables.get(name)
        if variable is not None:
            variable.AddRefrence()

    def enterFunc_decleration(self, ctx: nerockParser.Func_declerationContext):
        name = ctx.ID().getText()
        self.FuncsNames.append(name)
        self.CurrentFuncName = name
        params = getParams(ctx)
        self.VarsPerFunc[name] = {
            param.ID().getText(): MallocVar(param.ID().getText())
            for param in params
        }

        return_type = typeMatch(getReturnType(ctx))
        parameter_types = returnLoopType(params)
        function_type = GetOrCreateType(self, return_type, parameter_types)
        self.Funcs[name] = ir.Function(self.Moudle, function_type, name=name)

    def enterDecl_malloc(self, ctx: nerockParser.Decl_mallocContext):
        self.NewMallocVar(ctx.ID().getText())

    def enterAtom(self, ctx: nerockParser.AtomContext):
        if ctx.ID() is not None:
            self.RefrenceVarFound(ctx.ID().getText())

    def __repr__(self):
        text = f"Funcs: {self.Funcs}\n"
        for func_name, variables in self.VarsPerFunc.items():
            text += f"{func_name}: {variables}\n"
        return text
