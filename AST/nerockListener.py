# Generated from AST/nerock.g4 by ANTLR 4.13.2
from antlr4 import *
if "." in __name__:
    from .nerockParser import nerockParser
else:
    from nerockParser import nerockParser

# This class defines a complete listener for a parse tree produced by nerockParser.
class nerockListener(ParseTreeListener):

    # Enter a parse tree produced by nerockParser#prog.
    def enterProg(self, ctx:nerockParser.ProgContext):
        pass

    # Exit a parse tree produced by nerockParser#prog.
    def exitProg(self, ctx:nerockParser.ProgContext):
        pass


    # Enter a parse tree produced by nerockParser#command.
    def enterCommand(self, ctx:nerockParser.CommandContext):
        pass

    # Exit a parse tree produced by nerockParser#command.
    def exitCommand(self, ctx:nerockParser.CommandContext):
        pass


    # Enter a parse tree produced by nerockParser#block.
    def enterBlock(self, ctx:nerockParser.BlockContext):
        pass

    # Exit a parse tree produced by nerockParser#block.
    def exitBlock(self, ctx:nerockParser.BlockContext):
        pass


    # Enter a parse tree produced by nerockParser#func_decleration.
    def enterFunc_decleration(self, ctx:nerockParser.Func_declerationContext):
        pass

    # Exit a parse tree produced by nerockParser#func_decleration.
    def exitFunc_decleration(self, ctx:nerockParser.Func_declerationContext):
        pass


    # Enter a parse tree produced by nerockParser#decl_var.
    def enterDecl_var(self, ctx:nerockParser.Decl_varContext):
        pass

    # Exit a parse tree produced by nerockParser#decl_var.
    def exitDecl_var(self, ctx:nerockParser.Decl_varContext):
        pass


    # Enter a parse tree produced by nerockParser#expr.
    def enterExpr(self, ctx:nerockParser.ExprContext):
        pass

    # Exit a parse tree produced by nerockParser#expr.
    def exitExpr(self, ctx:nerockParser.ExprContext):
        pass


    # Enter a parse tree produced by nerockParser#typesKeyword.
    def enterTypesKeyword(self, ctx:nerockParser.TypesKeywordContext):
        pass

    # Exit a parse tree produced by nerockParser#typesKeyword.
    def exitTypesKeyword(self, ctx:nerockParser.TypesKeywordContext):
        pass


    # Enter a parse tree produced by nerockParser#param.
    def enterParam(self, ctx:nerockParser.ParamContext):
        pass

    # Exit a parse tree produced by nerockParser#param.
    def exitParam(self, ctx:nerockParser.ParamContext):
        pass


    # Enter a parse tree produced by nerockParser#paramList.
    def enterParamList(self, ctx:nerockParser.ParamListContext):
        pass

    # Exit a parse tree produced by nerockParser#paramList.
    def exitParamList(self, ctx:nerockParser.ParamListContext):
        pass


    # Enter a parse tree produced by nerockParser#returnFunc.
    def enterReturnFunc(self, ctx:nerockParser.ReturnFuncContext):
        pass

    # Exit a parse tree produced by nerockParser#returnFunc.
    def exitReturnFunc(self, ctx:nerockParser.ReturnFuncContext):
        pass


    # Enter a parse tree produced by nerockParser#atom.
    def enterAtom(self, ctx:nerockParser.AtomContext):
        pass

    # Exit a parse tree produced by nerockParser#atom.
    def exitAtom(self, ctx:nerockParser.AtomContext):
        pass


    # Enter a parse tree produced by nerockParser#return.
    def enterReturn(self, ctx:nerockParser.ReturnContext):
        pass

    # Exit a parse tree produced by nerockParser#return.
    def exitReturn(self, ctx:nerockParser.ReturnContext):
        pass



del nerockParser