# Generated from AST/nerock.g4 by ANTLR 4.13.2
from antlr4 import *
if "." in __name__:
    from .nerockParser import nerockParser
else:
    from nerockParser import nerockParser

# This class defines a complete generic visitor for a parse tree produced by nerockParser.

class nerockVisitor(ParseTreeVisitor):

    # Visit a parse tree produced by nerockParser#prog.
    def visitProg(self, ctx:nerockParser.ProgContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by nerockParser#command.
    def visitCommand(self, ctx:nerockParser.CommandContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by nerockParser#block.
    def visitBlock(self, ctx:nerockParser.BlockContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by nerockParser#func_decleration.
    def visitFunc_decleration(self, ctx:nerockParser.Func_declerationContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by nerockParser#decl_var.
    def visitDecl_var(self, ctx:nerockParser.Decl_varContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by nerockParser#expr.
    def visitExpr(self, ctx:nerockParser.ExprContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by nerockParser#typesKeyword.
    def visitTypesKeyword(self, ctx:nerockParser.TypesKeywordContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by nerockParser#param.
    def visitParam(self, ctx:nerockParser.ParamContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by nerockParser#paramList.
    def visitParamList(self, ctx:nerockParser.ParamListContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by nerockParser#returnFunc.
    def visitReturnFunc(self, ctx:nerockParser.ReturnFuncContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by nerockParser#atom.
    def visitAtom(self, ctx:nerockParser.AtomContext):
        return self.visitChildren(ctx)



del nerockParser