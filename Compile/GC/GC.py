from AST.nerockListener import nerockListener
from AST.nerockParser import nerockParser

class Var:
    def __init__(self, name):
        self.name = name
        self.refrences = 0

    def AddRefrence(self):
        self.refrences += 1
    def __repr__(self):
        return f"({self.name} : {self.refrences})"
class GC_walk(nerockListener):
    def __init__(self):
        self.Funcs = []
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
        self.Funcs.append(name)
        self.CurrentFuncName = name
        self.VarsPerFunc[name] = {}

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
