# Generated from AST/nerock.g4 by ANTLR 4.13.2
# encoding: utf-8
from antlr4 import *
from io import StringIO
import sys
if sys.version_info[1] > 5:
	from typing import TextIO
else:
	from typing.io import TextIO

def serializedATN():
    return [
        4,1,35,169,2,0,7,0,2,1,7,1,2,2,7,2,2,3,7,3,2,4,7,4,2,5,7,5,2,6,7,
        6,2,7,7,7,2,8,7,8,2,9,7,9,2,10,7,10,2,11,7,11,2,12,7,12,2,13,7,13,
        2,14,7,14,2,15,7,15,2,16,7,16,2,17,7,17,1,0,4,0,38,8,0,11,0,12,0,
        39,1,0,1,0,1,1,1,1,1,1,1,1,1,1,1,1,1,1,3,1,51,8,1,1,2,1,2,5,2,55,
        8,2,10,2,12,2,58,9,2,1,2,1,2,1,3,1,3,1,3,1,3,1,3,1,3,1,4,1,4,1,4,
        1,4,1,4,1,4,1,5,1,5,1,5,1,5,1,5,1,5,1,5,1,5,1,6,1,6,1,6,1,6,1,6,
        5,6,87,8,6,10,6,12,6,90,9,6,3,6,92,8,6,1,6,1,6,1,7,1,7,1,7,1,7,1,
        7,3,7,101,8,7,1,7,1,7,1,7,1,7,1,7,1,7,1,7,1,7,1,7,1,7,1,7,1,7,5,
        7,115,8,7,10,7,12,7,118,9,7,1,8,1,8,1,8,1,8,5,8,124,8,8,10,8,12,
        8,127,9,8,1,8,3,8,130,8,8,1,9,1,9,1,9,1,9,1,10,1,10,1,10,1,11,1,
        11,1,12,1,12,1,12,1,13,1,13,1,13,1,14,1,14,1,14,1,14,5,14,151,8,
        14,10,14,12,14,154,9,14,3,14,156,8,14,1,14,1,14,1,15,1,15,3,15,162,
        8,15,1,16,1,16,1,17,1,17,1,17,1,17,0,1,14,18,0,2,4,6,8,10,12,14,
        16,18,20,22,24,26,28,30,32,34,0,5,1,0,19,20,1,0,17,18,1,0,21,22,
        1,0,25,29,2,0,30,32,34,34,171,0,37,1,0,0,0,2,50,1,0,0,0,4,52,1,0,
        0,0,6,61,1,0,0,0,8,67,1,0,0,0,10,73,1,0,0,0,12,81,1,0,0,0,14,100,
        1,0,0,0,16,119,1,0,0,0,18,131,1,0,0,0,20,135,1,0,0,0,22,138,1,0,
        0,0,24,140,1,0,0,0,26,143,1,0,0,0,28,146,1,0,0,0,30,161,1,0,0,0,
        32,163,1,0,0,0,34,165,1,0,0,0,36,38,3,2,1,0,37,36,1,0,0,0,38,39,
        1,0,0,0,39,37,1,0,0,0,39,40,1,0,0,0,40,41,1,0,0,0,41,42,5,0,0,1,
        42,1,1,0,0,0,43,51,3,6,3,0,44,51,3,14,7,0,45,51,3,8,4,0,46,51,3,
        34,17,0,47,51,3,24,12,0,48,51,3,10,5,0,49,51,3,16,8,0,50,43,1,0,
        0,0,50,44,1,0,0,0,50,45,1,0,0,0,50,46,1,0,0,0,50,47,1,0,0,0,50,48,
        1,0,0,0,50,49,1,0,0,0,51,3,1,0,0,0,52,56,5,1,0,0,53,55,3,2,1,0,54,
        53,1,0,0,0,55,58,1,0,0,0,56,54,1,0,0,0,56,57,1,0,0,0,57,59,1,0,0,
        0,58,56,1,0,0,0,59,60,5,2,0,0,60,5,1,0,0,0,61,62,5,24,0,0,62,63,
        5,30,0,0,63,64,3,28,14,0,64,65,3,30,15,0,65,66,3,4,2,0,66,7,1,0,
        0,0,67,68,5,3,0,0,68,69,5,30,0,0,69,70,3,22,11,0,70,71,5,4,0,0,71,
        72,3,14,7,0,72,9,1,0,0,0,73,74,5,5,0,0,74,75,5,6,0,0,75,76,5,7,0,
        0,76,77,3,14,7,0,77,78,5,8,0,0,78,79,5,9,0,0,79,80,5,30,0,0,80,11,
        1,0,0,0,81,82,5,30,0,0,82,91,5,7,0,0,83,88,3,14,7,0,84,85,5,10,0,
        0,85,87,3,14,7,0,86,84,1,0,0,0,87,90,1,0,0,0,88,86,1,0,0,0,88,89,
        1,0,0,0,89,92,1,0,0,0,90,88,1,0,0,0,91,83,1,0,0,0,91,92,1,0,0,0,
        92,93,1,0,0,0,93,94,5,8,0,0,94,13,1,0,0,0,95,96,6,7,-1,0,96,101,
        3,12,6,0,97,101,3,32,16,0,98,99,5,18,0,0,99,101,3,14,7,5,100,95,
        1,0,0,0,100,97,1,0,0,0,100,98,1,0,0,0,101,116,1,0,0,0,102,103,10,
        4,0,0,103,104,7,0,0,0,104,115,3,14,7,5,105,106,10,3,0,0,106,107,
        7,1,0,0,107,115,3,14,7,4,108,109,10,2,0,0,109,110,7,2,0,0,110,115,
        3,14,7,3,111,112,10,1,0,0,112,113,5,23,0,0,113,115,3,14,7,2,114,
        102,1,0,0,0,114,105,1,0,0,0,114,108,1,0,0,0,114,111,1,0,0,0,115,
        118,1,0,0,0,116,114,1,0,0,0,116,117,1,0,0,0,117,15,1,0,0,0,118,116,
        1,0,0,0,119,120,5,11,0,0,120,121,3,14,7,0,121,125,3,4,2,0,122,124,
        3,18,9,0,123,122,1,0,0,0,124,127,1,0,0,0,125,123,1,0,0,0,125,126,
        1,0,0,0,126,129,1,0,0,0,127,125,1,0,0,0,128,130,3,20,10,0,129,128,
        1,0,0,0,129,130,1,0,0,0,130,17,1,0,0,0,131,132,5,12,0,0,132,133,
        3,14,7,0,133,134,3,4,2,0,134,19,1,0,0,0,135,136,5,13,0,0,136,137,
        3,4,2,0,137,21,1,0,0,0,138,139,7,3,0,0,139,23,1,0,0,0,140,141,5,
        14,0,0,141,142,5,30,0,0,142,25,1,0,0,0,143,144,3,22,11,0,144,145,
        5,30,0,0,145,27,1,0,0,0,146,155,5,7,0,0,147,152,3,26,13,0,148,149,
        5,10,0,0,149,151,3,26,13,0,150,148,1,0,0,0,151,154,1,0,0,0,152,150,
        1,0,0,0,152,153,1,0,0,0,153,156,1,0,0,0,154,152,1,0,0,0,155,147,
        1,0,0,0,155,156,1,0,0,0,156,157,1,0,0,0,157,158,5,8,0,0,158,29,1,
        0,0,0,159,160,5,15,0,0,160,162,3,22,11,0,161,159,1,0,0,0,161,162,
        1,0,0,0,162,31,1,0,0,0,163,164,7,4,0,0,164,33,1,0,0,0,165,166,5,
        16,0,0,166,167,3,14,7,0,167,35,1,0,0,0,13,39,50,56,88,91,100,114,
        116,125,129,152,155,161
    ]

class nerockParser ( Parser ):

    grammarFileName = "nerock.g4"

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    sharedContextCache = PredictionContextCache()

    literalNames = [ "<INVALID>", "'{'", "'}'", "'var'", "'='", "'manual'", 
                     "'malloc'", "'('", "')'", "':'", "','", "'if'", "'elif'", 
                     "'else'", "'declare'", "'->'", "'return'", "'+'", "'-'", 
                     "'*'", "'/'", "'>'", "'<'", "'=='", "'decl'", "'i32'", 
                     "'str'", "'f32'", "'i1'", "'v'" ]

    symbolicNames = [ "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "<INVALID>", "PLUS", "MIN", "MUL", "DIV", "BIGGER_L", 
                      "LOWER_L", "EQUAL_C", "DECL_FUNC", "INT_TYPE", "STRING_TYPE", 
                      "FLOAT_TYPE", "BOOL_TYPE", "VOID_TYPE", "ID", "FLOAT", 
                      "NUM", "COMMENT", "STRING", "WS" ]

    RULE_prog = 0
    RULE_command = 1
    RULE_block = 2
    RULE_func_decleration = 3
    RULE_decl_var = 4
    RULE_decl_malloc = 5
    RULE_call = 6
    RULE_expr = 7
    RULE_if_decl = 8
    RULE_elif = 9
    RULE_else = 10
    RULE_typesKeyword = 11
    RULE_importScript = 12
    RULE_param = 13
    RULE_paramList = 14
    RULE_returnFunc = 15
    RULE_atom = 16
    RULE_return = 17

    ruleNames =  [ "prog", "command", "block", "func_decleration", "decl_var", 
                   "decl_malloc", "call", "expr", "if_decl", "elif", "else", 
                   "typesKeyword", "importScript", "param", "paramList", 
                   "returnFunc", "atom", "return" ]

    EOF = Token.EOF
    T__0=1
    T__1=2
    T__2=3
    T__3=4
    T__4=5
    T__5=6
    T__6=7
    T__7=8
    T__8=9
    T__9=10
    T__10=11
    T__11=12
    T__12=13
    T__13=14
    T__14=15
    T__15=16
    PLUS=17
    MIN=18
    MUL=19
    DIV=20
    BIGGER_L=21
    LOWER_L=22
    EQUAL_C=23
    DECL_FUNC=24
    INT_TYPE=25
    STRING_TYPE=26
    FLOAT_TYPE=27
    BOOL_TYPE=28
    VOID_TYPE=29
    ID=30
    FLOAT=31
    NUM=32
    COMMENT=33
    STRING=34
    WS=35

    def __init__(self, input:TokenStream, output:TextIO = sys.stdout):
        super().__init__(input, output)
        self.checkVersion("4.13.2")
        self._interp = ParserATNSimulator(self, self.atn, self.decisionsToDFA, self.sharedContextCache)
        self._predicates = None




    class ProgContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def EOF(self):
            return self.getToken(nerockParser.EOF, 0)

        def command(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(nerockParser.CommandContext)
            else:
                return self.getTypedRuleContext(nerockParser.CommandContext,i)


        def getRuleIndex(self):
            return nerockParser.RULE_prog

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterProg" ):
                listener.enterProg(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitProg" ):
                listener.exitProg(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitProg" ):
                return visitor.visitProg(self)
            else:
                return visitor.visitChildren(self)




    def prog(self):

        localctx = nerockParser.ProgContext(self, self._ctx, self.state)
        self.enterRule(localctx, 0, self.RULE_prog)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 37 
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while True:
                self.state = 36
                self.command()
                self.state = 39 
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if not ((((_la) & ~0x3f) == 0 and ((1 << _la) & 24713185320) != 0)):
                    break

            self.state = 41
            self.match(nerockParser.EOF)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class CommandContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def func_decleration(self):
            return self.getTypedRuleContext(nerockParser.Func_declerationContext,0)


        def expr(self):
            return self.getTypedRuleContext(nerockParser.ExprContext,0)


        def decl_var(self):
            return self.getTypedRuleContext(nerockParser.Decl_varContext,0)


        def return_(self):
            return self.getTypedRuleContext(nerockParser.ReturnContext,0)


        def importScript(self):
            return self.getTypedRuleContext(nerockParser.ImportScriptContext,0)


        def decl_malloc(self):
            return self.getTypedRuleContext(nerockParser.Decl_mallocContext,0)


        def if_decl(self):
            return self.getTypedRuleContext(nerockParser.If_declContext,0)


        def getRuleIndex(self):
            return nerockParser.RULE_command

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterCommand" ):
                listener.enterCommand(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitCommand" ):
                listener.exitCommand(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitCommand" ):
                return visitor.visitCommand(self)
            else:
                return visitor.visitChildren(self)




    def command(self):

        localctx = nerockParser.CommandContext(self, self._ctx, self.state)
        self.enterRule(localctx, 2, self.RULE_command)
        try:
            self.state = 50
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [24]:
                self.enterOuterAlt(localctx, 1)
                self.state = 43
                self.func_decleration()
                pass
            elif token in [18, 30, 31, 32, 34]:
                self.enterOuterAlt(localctx, 2)
                self.state = 44
                self.expr(0)
                pass
            elif token in [3]:
                self.enterOuterAlt(localctx, 3)
                self.state = 45
                self.decl_var()
                pass
            elif token in [16]:
                self.enterOuterAlt(localctx, 4)
                self.state = 46
                self.return_()
                pass
            elif token in [14]:
                self.enterOuterAlt(localctx, 5)
                self.state = 47
                self.importScript()
                pass
            elif token in [5]:
                self.enterOuterAlt(localctx, 6)
                self.state = 48
                self.decl_malloc()
                pass
            elif token in [11]:
                self.enterOuterAlt(localctx, 7)
                self.state = 49
                self.if_decl()
                pass
            else:
                raise NoViableAltException(self)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class BlockContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def command(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(nerockParser.CommandContext)
            else:
                return self.getTypedRuleContext(nerockParser.CommandContext,i)


        def getRuleIndex(self):
            return nerockParser.RULE_block

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterBlock" ):
                listener.enterBlock(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitBlock" ):
                listener.exitBlock(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitBlock" ):
                return visitor.visitBlock(self)
            else:
                return visitor.visitChildren(self)




    def block(self):

        localctx = nerockParser.BlockContext(self, self._ctx, self.state)
        self.enterRule(localctx, 4, self.RULE_block)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 52
            self.match(nerockParser.T__0)
            self.state = 56
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while (((_la) & ~0x3f) == 0 and ((1 << _la) & 24713185320) != 0):
                self.state = 53
                self.command()
                self.state = 58
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 59
            self.match(nerockParser.T__1)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Func_declerationContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def DECL_FUNC(self):
            return self.getToken(nerockParser.DECL_FUNC, 0)

        def ID(self):
            return self.getToken(nerockParser.ID, 0)

        def paramList(self):
            return self.getTypedRuleContext(nerockParser.ParamListContext,0)


        def returnFunc(self):
            return self.getTypedRuleContext(nerockParser.ReturnFuncContext,0)


        def block(self):
            return self.getTypedRuleContext(nerockParser.BlockContext,0)


        def getRuleIndex(self):
            return nerockParser.RULE_func_decleration

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterFunc_decleration" ):
                listener.enterFunc_decleration(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitFunc_decleration" ):
                listener.exitFunc_decleration(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitFunc_decleration" ):
                return visitor.visitFunc_decleration(self)
            else:
                return visitor.visitChildren(self)




    def func_decleration(self):

        localctx = nerockParser.Func_declerationContext(self, self._ctx, self.state)
        self.enterRule(localctx, 6, self.RULE_func_decleration)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 61
            self.match(nerockParser.DECL_FUNC)
            self.state = 62
            self.match(nerockParser.ID)
            self.state = 63
            self.paramList()
            self.state = 64
            self.returnFunc()
            self.state = 65
            self.block()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Decl_varContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def ID(self):
            return self.getToken(nerockParser.ID, 0)

        def typesKeyword(self):
            return self.getTypedRuleContext(nerockParser.TypesKeywordContext,0)


        def expr(self):
            return self.getTypedRuleContext(nerockParser.ExprContext,0)


        def getRuleIndex(self):
            return nerockParser.RULE_decl_var

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterDecl_var" ):
                listener.enterDecl_var(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitDecl_var" ):
                listener.exitDecl_var(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitDecl_var" ):
                return visitor.visitDecl_var(self)
            else:
                return visitor.visitChildren(self)




    def decl_var(self):

        localctx = nerockParser.Decl_varContext(self, self._ctx, self.state)
        self.enterRule(localctx, 8, self.RULE_decl_var)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 67
            self.match(nerockParser.T__2)
            self.state = 68
            self.match(nerockParser.ID)
            self.state = 69
            self.typesKeyword()
            self.state = 70
            self.match(nerockParser.T__3)
            self.state = 71
            self.expr(0)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Decl_mallocContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def expr(self):
            return self.getTypedRuleContext(nerockParser.ExprContext,0)


        def ID(self):
            return self.getToken(nerockParser.ID, 0)

        def getRuleIndex(self):
            return nerockParser.RULE_decl_malloc

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterDecl_malloc" ):
                listener.enterDecl_malloc(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitDecl_malloc" ):
                listener.exitDecl_malloc(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitDecl_malloc" ):
                return visitor.visitDecl_malloc(self)
            else:
                return visitor.visitChildren(self)




    def decl_malloc(self):

        localctx = nerockParser.Decl_mallocContext(self, self._ctx, self.state)
        self.enterRule(localctx, 10, self.RULE_decl_malloc)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 73
            self.match(nerockParser.T__4)
            self.state = 74
            self.match(nerockParser.T__5)
            self.state = 75
            self.match(nerockParser.T__6)
            self.state = 76
            self.expr(0)
            self.state = 77
            self.match(nerockParser.T__7)
            self.state = 78
            self.match(nerockParser.T__8)
            self.state = 79
            self.match(nerockParser.ID)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class CallContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def ID(self):
            return self.getToken(nerockParser.ID, 0)

        def expr(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(nerockParser.ExprContext)
            else:
                return self.getTypedRuleContext(nerockParser.ExprContext,i)


        def getRuleIndex(self):
            return nerockParser.RULE_call

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterCall" ):
                listener.enterCall(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitCall" ):
                listener.exitCall(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitCall" ):
                return visitor.visitCall(self)
            else:
                return visitor.visitChildren(self)




    def call(self):

        localctx = nerockParser.CallContext(self, self._ctx, self.state)
        self.enterRule(localctx, 12, self.RULE_call)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 81
            self.match(nerockParser.ID)
            self.state = 82
            self.match(nerockParser.T__6)
            self.state = 91
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if (((_la) & ~0x3f) == 0 and ((1 << _la) & 24696324096) != 0):
                self.state = 83
                self.expr(0)
                self.state = 88
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                while _la==10:
                    self.state = 84
                    self.match(nerockParser.T__9)
                    self.state = 85
                    self.expr(0)
                    self.state = 90
                    self._errHandler.sync(self)
                    _la = self._input.LA(1)



            self.state = 93
            self.match(nerockParser.T__7)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ExprContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def call(self):
            return self.getTypedRuleContext(nerockParser.CallContext,0)


        def atom(self):
            return self.getTypedRuleContext(nerockParser.AtomContext,0)


        def MIN(self):
            return self.getToken(nerockParser.MIN, 0)

        def expr(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(nerockParser.ExprContext)
            else:
                return self.getTypedRuleContext(nerockParser.ExprContext,i)


        def DIV(self):
            return self.getToken(nerockParser.DIV, 0)

        def MUL(self):
            return self.getToken(nerockParser.MUL, 0)

        def PLUS(self):
            return self.getToken(nerockParser.PLUS, 0)

        def BIGGER_L(self):
            return self.getToken(nerockParser.BIGGER_L, 0)

        def LOWER_L(self):
            return self.getToken(nerockParser.LOWER_L, 0)

        def EQUAL_C(self):
            return self.getToken(nerockParser.EQUAL_C, 0)

        def getRuleIndex(self):
            return nerockParser.RULE_expr

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterExpr" ):
                listener.enterExpr(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitExpr" ):
                listener.exitExpr(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitExpr" ):
                return visitor.visitExpr(self)
            else:
                return visitor.visitChildren(self)



    def expr(self, _p:int=0):
        _parentctx = self._ctx
        _parentState = self.state
        localctx = nerockParser.ExprContext(self, self._ctx, _parentState)
        _prevctx = localctx
        _startState = 14
        self.enterRecursionRule(localctx, 14, self.RULE_expr, _p)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 100
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,5,self._ctx)
            if la_ == 1:
                self.state = 96
                self.call()
                pass

            elif la_ == 2:
                self.state = 97
                self.atom()
                pass

            elif la_ == 3:
                self.state = 98
                self.match(nerockParser.MIN)
                self.state = 99
                self.expr(5)
                pass


            self._ctx.stop = self._input.LT(-1)
            self.state = 116
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,7,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    self.state = 114
                    self._errHandler.sync(self)
                    la_ = self._interp.adaptivePredict(self._input,6,self._ctx)
                    if la_ == 1:
                        localctx = nerockParser.ExprContext(self, _parentctx, _parentState)
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_expr)
                        self.state = 102
                        if not self.precpred(self._ctx, 4):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 4)")
                        self.state = 103
                        _la = self._input.LA(1)
                        if not(_la==19 or _la==20):
                            self._errHandler.recoverInline(self)
                        else:
                            self._errHandler.reportMatch(self)
                            self.consume()
                        self.state = 104
                        self.expr(5)
                        pass

                    elif la_ == 2:
                        localctx = nerockParser.ExprContext(self, _parentctx, _parentState)
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_expr)
                        self.state = 105
                        if not self.precpred(self._ctx, 3):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 3)")
                        self.state = 106
                        _la = self._input.LA(1)
                        if not(_la==17 or _la==18):
                            self._errHandler.recoverInline(self)
                        else:
                            self._errHandler.reportMatch(self)
                            self.consume()
                        self.state = 107
                        self.expr(4)
                        pass

                    elif la_ == 3:
                        localctx = nerockParser.ExprContext(self, _parentctx, _parentState)
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_expr)
                        self.state = 108
                        if not self.precpred(self._ctx, 2):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 2)")
                        self.state = 109
                        _la = self._input.LA(1)
                        if not(_la==21 or _la==22):
                            self._errHandler.recoverInline(self)
                        else:
                            self._errHandler.reportMatch(self)
                            self.consume()
                        self.state = 110
                        self.expr(3)
                        pass

                    elif la_ == 4:
                        localctx = nerockParser.ExprContext(self, _parentctx, _parentState)
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_expr)
                        self.state = 111
                        if not self.precpred(self._ctx, 1):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 1)")
                        self.state = 112
                        self.match(nerockParser.EQUAL_C)
                        self.state = 113
                        self.expr(2)
                        pass

             
                self.state = 118
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,7,self._ctx)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.unrollRecursionContexts(_parentctx)
        return localctx


    class If_declContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def expr(self):
            return self.getTypedRuleContext(nerockParser.ExprContext,0)


        def block(self):
            return self.getTypedRuleContext(nerockParser.BlockContext,0)


        def elif_(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(nerockParser.ElifContext)
            else:
                return self.getTypedRuleContext(nerockParser.ElifContext,i)


        def else_(self):
            return self.getTypedRuleContext(nerockParser.ElseContext,0)


        def getRuleIndex(self):
            return nerockParser.RULE_if_decl

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterIf_decl" ):
                listener.enterIf_decl(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitIf_decl" ):
                listener.exitIf_decl(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitIf_decl" ):
                return visitor.visitIf_decl(self)
            else:
                return visitor.visitChildren(self)




    def if_decl(self):

        localctx = nerockParser.If_declContext(self, self._ctx, self.state)
        self.enterRule(localctx, 16, self.RULE_if_decl)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 119
            self.match(nerockParser.T__10)
            self.state = 120
            self.expr(0)
            self.state = 121
            self.block()
            self.state = 125
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==12:
                self.state = 122
                self.elif_()
                self.state = 127
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 129
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==13:
                self.state = 128
                self.else_()


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ElifContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def expr(self):
            return self.getTypedRuleContext(nerockParser.ExprContext,0)


        def block(self):
            return self.getTypedRuleContext(nerockParser.BlockContext,0)


        def getRuleIndex(self):
            return nerockParser.RULE_elif

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterElif" ):
                listener.enterElif(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitElif" ):
                listener.exitElif(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitElif" ):
                return visitor.visitElif(self)
            else:
                return visitor.visitChildren(self)




    def elif_(self):

        localctx = nerockParser.ElifContext(self, self._ctx, self.state)
        self.enterRule(localctx, 18, self.RULE_elif)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 131
            self.match(nerockParser.T__11)
            self.state = 132
            self.expr(0)
            self.state = 133
            self.block()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ElseContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def block(self):
            return self.getTypedRuleContext(nerockParser.BlockContext,0)


        def getRuleIndex(self):
            return nerockParser.RULE_else

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterElse" ):
                listener.enterElse(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitElse" ):
                listener.exitElse(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitElse" ):
                return visitor.visitElse(self)
            else:
                return visitor.visitChildren(self)




    def else_(self):

        localctx = nerockParser.ElseContext(self, self._ctx, self.state)
        self.enterRule(localctx, 20, self.RULE_else)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 135
            self.match(nerockParser.T__12)
            self.state = 136
            self.block()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class TypesKeywordContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def INT_TYPE(self):
            return self.getToken(nerockParser.INT_TYPE, 0)

        def STRING_TYPE(self):
            return self.getToken(nerockParser.STRING_TYPE, 0)

        def FLOAT_TYPE(self):
            return self.getToken(nerockParser.FLOAT_TYPE, 0)

        def VOID_TYPE(self):
            return self.getToken(nerockParser.VOID_TYPE, 0)

        def BOOL_TYPE(self):
            return self.getToken(nerockParser.BOOL_TYPE, 0)

        def getRuleIndex(self):
            return nerockParser.RULE_typesKeyword

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterTypesKeyword" ):
                listener.enterTypesKeyword(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitTypesKeyword" ):
                listener.exitTypesKeyword(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitTypesKeyword" ):
                return visitor.visitTypesKeyword(self)
            else:
                return visitor.visitChildren(self)




    def typesKeyword(self):

        localctx = nerockParser.TypesKeywordContext(self, self._ctx, self.state)
        self.enterRule(localctx, 22, self.RULE_typesKeyword)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 138
            _la = self._input.LA(1)
            if not((((_la) & ~0x3f) == 0 and ((1 << _la) & 1040187392) != 0)):
                self._errHandler.recoverInline(self)
            else:
                self._errHandler.reportMatch(self)
                self.consume()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ImportScriptContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def ID(self):
            return self.getToken(nerockParser.ID, 0)

        def getRuleIndex(self):
            return nerockParser.RULE_importScript

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterImportScript" ):
                listener.enterImportScript(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitImportScript" ):
                listener.exitImportScript(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitImportScript" ):
                return visitor.visitImportScript(self)
            else:
                return visitor.visitChildren(self)




    def importScript(self):

        localctx = nerockParser.ImportScriptContext(self, self._ctx, self.state)
        self.enterRule(localctx, 24, self.RULE_importScript)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 140
            self.match(nerockParser.T__13)
            self.state = 141
            self.match(nerockParser.ID)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ParamContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def typesKeyword(self):
            return self.getTypedRuleContext(nerockParser.TypesKeywordContext,0)


        def ID(self):
            return self.getToken(nerockParser.ID, 0)

        def getRuleIndex(self):
            return nerockParser.RULE_param

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterParam" ):
                listener.enterParam(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitParam" ):
                listener.exitParam(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitParam" ):
                return visitor.visitParam(self)
            else:
                return visitor.visitChildren(self)




    def param(self):

        localctx = nerockParser.ParamContext(self, self._ctx, self.state)
        self.enterRule(localctx, 26, self.RULE_param)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 143
            self.typesKeyword()
            self.state = 144
            self.match(nerockParser.ID)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ParamListContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def param(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(nerockParser.ParamContext)
            else:
                return self.getTypedRuleContext(nerockParser.ParamContext,i)


        def getRuleIndex(self):
            return nerockParser.RULE_paramList

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterParamList" ):
                listener.enterParamList(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitParamList" ):
                listener.exitParamList(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitParamList" ):
                return visitor.visitParamList(self)
            else:
                return visitor.visitChildren(self)




    def paramList(self):

        localctx = nerockParser.ParamListContext(self, self._ctx, self.state)
        self.enterRule(localctx, 28, self.RULE_paramList)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 146
            self.match(nerockParser.T__6)
            self.state = 155
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if (((_la) & ~0x3f) == 0 and ((1 << _la) & 1040187392) != 0):
                self.state = 147
                self.param()
                self.state = 152
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                while _la==10:
                    self.state = 148
                    self.match(nerockParser.T__9)
                    self.state = 149
                    self.param()
                    self.state = 154
                    self._errHandler.sync(self)
                    _la = self._input.LA(1)



            self.state = 157
            self.match(nerockParser.T__7)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ReturnFuncContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def typesKeyword(self):
            return self.getTypedRuleContext(nerockParser.TypesKeywordContext,0)


        def getRuleIndex(self):
            return nerockParser.RULE_returnFunc

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterReturnFunc" ):
                listener.enterReturnFunc(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitReturnFunc" ):
                listener.exitReturnFunc(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitReturnFunc" ):
                return visitor.visitReturnFunc(self)
            else:
                return visitor.visitChildren(self)




    def returnFunc(self):

        localctx = nerockParser.ReturnFuncContext(self, self._ctx, self.state)
        self.enterRule(localctx, 30, self.RULE_returnFunc)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 161
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==15:
                self.state = 159
                self.match(nerockParser.T__14)
                self.state = 160
                self.typesKeyword()


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class AtomContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def NUM(self):
            return self.getToken(nerockParser.NUM, 0)

        def FLOAT(self):
            return self.getToken(nerockParser.FLOAT, 0)

        def STRING(self):
            return self.getToken(nerockParser.STRING, 0)

        def ID(self):
            return self.getToken(nerockParser.ID, 0)

        def getRuleIndex(self):
            return nerockParser.RULE_atom

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterAtom" ):
                listener.enterAtom(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitAtom" ):
                listener.exitAtom(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitAtom" ):
                return visitor.visitAtom(self)
            else:
                return visitor.visitChildren(self)




    def atom(self):

        localctx = nerockParser.AtomContext(self, self._ctx, self.state)
        self.enterRule(localctx, 32, self.RULE_atom)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 163
            _la = self._input.LA(1)
            if not((((_la) & ~0x3f) == 0 and ((1 << _la) & 24696061952) != 0)):
                self._errHandler.recoverInline(self)
            else:
                self._errHandler.reportMatch(self)
                self.consume()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ReturnContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def expr(self):
            return self.getTypedRuleContext(nerockParser.ExprContext,0)


        def getRuleIndex(self):
            return nerockParser.RULE_return

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterReturn" ):
                listener.enterReturn(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitReturn" ):
                listener.exitReturn(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitReturn" ):
                return visitor.visitReturn(self)
            else:
                return visitor.visitChildren(self)




    def return_(self):

        localctx = nerockParser.ReturnContext(self, self._ctx, self.state)
        self.enterRule(localctx, 34, self.RULE_return)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 165
            self.match(nerockParser.T__15)
            self.state = 166
            self.expr(0)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx



    def sempred(self, localctx:RuleContext, ruleIndex:int, predIndex:int):
        if self._predicates == None:
            self._predicates = dict()
        self._predicates[7] = self.expr_sempred
        pred = self._predicates.get(ruleIndex, None)
        if pred is None:
            raise Exception("No predicate with index:" + str(ruleIndex))
        else:
            return pred(localctx, predIndex)

    def expr_sempred(self, localctx:ExprContext, predIndex:int):
            if predIndex == 0:
                return self.precpred(self._ctx, 4)
         

            if predIndex == 1:
                return self.precpred(self._ctx, 3)
         

            if predIndex == 2:
                return self.precpred(self._ctx, 2)
         

            if predIndex == 3:
                return self.precpred(self._ctx, 1)
         




