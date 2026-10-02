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
        4,1,25,130,2,0,7,0,2,1,7,1,2,2,7,2,2,3,7,3,2,4,7,4,2,5,7,5,2,6,7,
        6,2,7,7,7,2,8,7,8,2,9,7,9,2,10,7,10,2,11,7,11,2,12,7,12,2,13,7,13,
        1,0,4,0,30,8,0,11,0,12,0,31,1,0,1,0,1,1,1,1,1,1,1,1,1,1,3,1,41,8,
        1,1,2,1,2,5,2,45,8,2,10,2,12,2,48,9,2,1,2,1,2,1,3,1,3,1,3,1,3,1,
        3,1,3,1,4,1,4,1,4,1,4,1,4,1,4,1,5,1,5,1,5,1,5,1,5,5,5,69,8,5,10,
        5,12,5,72,9,5,3,5,74,8,5,1,5,1,5,1,6,1,6,1,6,3,6,81,8,6,1,6,1,6,
        1,6,1,6,1,6,1,6,1,6,1,6,1,6,1,6,1,6,1,6,5,6,95,8,6,10,6,12,6,98,
        9,6,1,7,1,7,1,8,1,8,1,8,1,9,1,9,1,9,1,10,1,10,1,10,1,10,5,10,112,
        8,10,10,10,12,10,115,9,10,3,10,117,8,10,1,10,1,10,1,11,1,11,3,11,
        123,8,11,1,12,1,12,1,13,1,13,1,13,1,13,0,1,12,14,0,2,4,6,8,10,12,
        14,16,18,20,22,24,26,0,2,1,0,16,19,2,0,20,22,24,24,131,0,29,1,0,
        0,0,2,40,1,0,0,0,4,42,1,0,0,0,6,51,1,0,0,0,8,57,1,0,0,0,10,63,1,
        0,0,0,12,80,1,0,0,0,14,99,1,0,0,0,16,101,1,0,0,0,18,104,1,0,0,0,
        20,107,1,0,0,0,22,122,1,0,0,0,24,124,1,0,0,0,26,126,1,0,0,0,28,30,
        3,2,1,0,29,28,1,0,0,0,30,31,1,0,0,0,31,29,1,0,0,0,31,32,1,0,0,0,
        32,33,1,0,0,0,33,34,5,0,0,1,34,1,1,0,0,0,35,41,3,6,3,0,36,41,3,12,
        6,0,37,41,3,8,4,0,38,41,3,26,13,0,39,41,3,16,8,0,40,35,1,0,0,0,40,
        36,1,0,0,0,40,37,1,0,0,0,40,38,1,0,0,0,40,39,1,0,0,0,41,3,1,0,0,
        0,42,46,5,1,0,0,43,45,3,2,1,0,44,43,1,0,0,0,45,48,1,0,0,0,46,44,
        1,0,0,0,46,47,1,0,0,0,47,49,1,0,0,0,48,46,1,0,0,0,49,50,5,2,0,0,
        50,5,1,0,0,0,51,52,5,15,0,0,52,53,5,20,0,0,53,54,3,20,10,0,54,55,
        3,22,11,0,55,56,3,4,2,0,56,7,1,0,0,0,57,58,5,3,0,0,58,59,5,20,0,
        0,59,60,3,14,7,0,60,61,5,4,0,0,61,62,3,12,6,0,62,9,1,0,0,0,63,64,
        5,20,0,0,64,73,5,5,0,0,65,70,3,12,6,0,66,67,5,6,0,0,67,69,3,12,6,
        0,68,66,1,0,0,0,69,72,1,0,0,0,70,68,1,0,0,0,70,71,1,0,0,0,71,74,
        1,0,0,0,72,70,1,0,0,0,73,65,1,0,0,0,73,74,1,0,0,0,74,75,1,0,0,0,
        75,76,5,7,0,0,76,11,1,0,0,0,77,78,6,6,-1,0,78,81,3,10,5,0,79,81,
        3,24,12,0,80,77,1,0,0,0,80,79,1,0,0,0,81,96,1,0,0,0,82,83,10,4,0,
        0,83,84,5,13,0,0,84,95,3,12,6,5,85,86,10,3,0,0,86,87,5,14,0,0,87,
        95,3,12,6,4,88,89,10,2,0,0,89,90,5,11,0,0,90,95,3,12,6,3,91,92,10,
        1,0,0,92,93,5,12,0,0,93,95,3,12,6,2,94,82,1,0,0,0,94,85,1,0,0,0,
        94,88,1,0,0,0,94,91,1,0,0,0,95,98,1,0,0,0,96,94,1,0,0,0,96,97,1,
        0,0,0,97,13,1,0,0,0,98,96,1,0,0,0,99,100,7,0,0,0,100,15,1,0,0,0,
        101,102,5,8,0,0,102,103,5,20,0,0,103,17,1,0,0,0,104,105,3,14,7,0,
        105,106,5,20,0,0,106,19,1,0,0,0,107,116,5,5,0,0,108,113,3,18,9,0,
        109,110,5,6,0,0,110,112,3,18,9,0,111,109,1,0,0,0,112,115,1,0,0,0,
        113,111,1,0,0,0,113,114,1,0,0,0,114,117,1,0,0,0,115,113,1,0,0,0,
        116,108,1,0,0,0,116,117,1,0,0,0,117,118,1,0,0,0,118,119,5,7,0,0,
        119,21,1,0,0,0,120,121,5,9,0,0,121,123,3,14,7,0,122,120,1,0,0,0,
        122,123,1,0,0,0,123,23,1,0,0,0,124,125,7,1,0,0,125,25,1,0,0,0,126,
        127,5,10,0,0,127,128,3,12,6,0,128,27,1,0,0,0,11,31,40,46,70,73,80,
        94,96,113,116,122
    ]

class nerockParser ( Parser ):

    grammarFileName = "nerock.g4"

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    sharedContextCache = PredictionContextCache()

    literalNames = [ "<INVALID>", "'{'", "'}'", "'var'", "'='", "'('", "','", 
                     "')'", "'declare'", "'->'", "'return'", "'+'", "'-'", 
                     "'*'", "'/'", "'decl'", "'i32'", "'str'", "'f32'", 
                     "'v'" ]

    symbolicNames = [ "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "<INVALID>", "<INVALID>", "<INVALID>", "PLUS", "MIN", 
                      "MUL", "DIV", "DECL_FUNC", "INT_TYPE", "STRING_TYPE", 
                      "FLOAT_TYPE", "VOID_TYPE", "ID", "FLOAT", "NUM", "COMMENT", 
                      "STRING", "WS" ]

    RULE_prog = 0
    RULE_command = 1
    RULE_block = 2
    RULE_func_decleration = 3
    RULE_decl_var = 4
    RULE_call = 5
    RULE_expr = 6
    RULE_typesKeyword = 7
    RULE_importScript = 8
    RULE_param = 9
    RULE_paramList = 10
    RULE_returnFunc = 11
    RULE_atom = 12
    RULE_return = 13

    ruleNames =  [ "prog", "command", "block", "func_decleration", "decl_var", 
                   "call", "expr", "typesKeyword", "importScript", "param", 
                   "paramList", "returnFunc", "atom", "return" ]

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
    PLUS=11
    MIN=12
    MUL=13
    DIV=14
    DECL_FUNC=15
    INT_TYPE=16
    STRING_TYPE=17
    FLOAT_TYPE=18
    VOID_TYPE=19
    ID=20
    FLOAT=21
    NUM=22
    COMMENT=23
    STRING=24
    WS=25

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
            self.state = 29 
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while True:
                self.state = 28
                self.command()
                self.state = 31 
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if not ((((_la) & ~0x3f) == 0 and ((1 << _la) & 24151304) != 0)):
                    break

            self.state = 33
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
            self.state = 40
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [15]:
                self.enterOuterAlt(localctx, 1)
                self.state = 35
                self.func_decleration()
                pass
            elif token in [20, 21, 22, 24]:
                self.enterOuterAlt(localctx, 2)
                self.state = 36
                self.expr(0)
                pass
            elif token in [3]:
                self.enterOuterAlt(localctx, 3)
                self.state = 37
                self.decl_var()
                pass
            elif token in [10]:
                self.enterOuterAlt(localctx, 4)
                self.state = 38
                self.return_()
                pass
            elif token in [8]:
                self.enterOuterAlt(localctx, 5)
                self.state = 39
                self.importScript()
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
            self.state = 42
            self.match(nerockParser.T__0)
            self.state = 46
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while (((_la) & ~0x3f) == 0 and ((1 << _la) & 24151304) != 0):
                self.state = 43
                self.command()
                self.state = 48
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 49
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
            self.state = 51
            self.match(nerockParser.DECL_FUNC)
            self.state = 52
            self.match(nerockParser.ID)
            self.state = 53
            self.paramList()
            self.state = 54
            self.returnFunc()
            self.state = 55
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
            self.state = 57
            self.match(nerockParser.T__2)
            self.state = 58
            self.match(nerockParser.ID)
            self.state = 59
            self.typesKeyword()
            self.state = 60
            self.match(nerockParser.T__3)
            self.state = 61
            self.expr(0)
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
        self.enterRule(localctx, 10, self.RULE_call)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 63
            self.match(nerockParser.ID)
            self.state = 64
            self.match(nerockParser.T__4)
            self.state = 73
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if (((_la) & ~0x3f) == 0 and ((1 << _la) & 24117248) != 0):
                self.state = 65
                self.expr(0)
                self.state = 70
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                while _la==6:
                    self.state = 66
                    self.match(nerockParser.T__5)
                    self.state = 67
                    self.expr(0)
                    self.state = 72
                    self._errHandler.sync(self)
                    _la = self._input.LA(1)



            self.state = 75
            self.match(nerockParser.T__6)
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


        def expr(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(nerockParser.ExprContext)
            else:
                return self.getTypedRuleContext(nerockParser.ExprContext,i)


        def MUL(self):
            return self.getToken(nerockParser.MUL, 0)

        def DIV(self):
            return self.getToken(nerockParser.DIV, 0)

        def PLUS(self):
            return self.getToken(nerockParser.PLUS, 0)

        def MIN(self):
            return self.getToken(nerockParser.MIN, 0)

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
        _startState = 12
        self.enterRecursionRule(localctx, 12, self.RULE_expr, _p)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 80
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,5,self._ctx)
            if la_ == 1:
                self.state = 78
                self.call()
                pass

            elif la_ == 2:
                self.state = 79
                self.atom()
                pass


            self._ctx.stop = self._input.LT(-1)
            self.state = 96
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,7,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    self.state = 94
                    self._errHandler.sync(self)
                    la_ = self._interp.adaptivePredict(self._input,6,self._ctx)
                    if la_ == 1:
                        localctx = nerockParser.ExprContext(self, _parentctx, _parentState)
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_expr)
                        self.state = 82
                        if not self.precpred(self._ctx, 4):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 4)")
                        self.state = 83
                        self.match(nerockParser.MUL)
                        self.state = 84
                        self.expr(5)
                        pass

                    elif la_ == 2:
                        localctx = nerockParser.ExprContext(self, _parentctx, _parentState)
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_expr)
                        self.state = 85
                        if not self.precpred(self._ctx, 3):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 3)")
                        self.state = 86
                        self.match(nerockParser.DIV)
                        self.state = 87
                        self.expr(4)
                        pass

                    elif la_ == 3:
                        localctx = nerockParser.ExprContext(self, _parentctx, _parentState)
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_expr)
                        self.state = 88
                        if not self.precpred(self._ctx, 2):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 2)")
                        self.state = 89
                        self.match(nerockParser.PLUS)
                        self.state = 90
                        self.expr(3)
                        pass

                    elif la_ == 4:
                        localctx = nerockParser.ExprContext(self, _parentctx, _parentState)
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_expr)
                        self.state = 91
                        if not self.precpred(self._ctx, 1):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 1)")
                        self.state = 92
                        self.match(nerockParser.MIN)
                        self.state = 93
                        self.expr(2)
                        pass

             
                self.state = 98
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,7,self._ctx)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.unrollRecursionContexts(_parentctx)
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
        self.enterRule(localctx, 14, self.RULE_typesKeyword)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 99
            _la = self._input.LA(1)
            if not((((_la) & ~0x3f) == 0 and ((1 << _la) & 983040) != 0)):
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
        self.enterRule(localctx, 16, self.RULE_importScript)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 101
            self.match(nerockParser.T__7)
            self.state = 102
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
        self.enterRule(localctx, 18, self.RULE_param)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 104
            self.typesKeyword()
            self.state = 105
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
        self.enterRule(localctx, 20, self.RULE_paramList)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 107
            self.match(nerockParser.T__4)
            self.state = 116
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if (((_la) & ~0x3f) == 0 and ((1 << _la) & 983040) != 0):
                self.state = 108
                self.param()
                self.state = 113
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                while _la==6:
                    self.state = 109
                    self.match(nerockParser.T__5)
                    self.state = 110
                    self.param()
                    self.state = 115
                    self._errHandler.sync(self)
                    _la = self._input.LA(1)



            self.state = 118
            self.match(nerockParser.T__6)
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
        self.enterRule(localctx, 22, self.RULE_returnFunc)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 122
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==9:
                self.state = 120
                self.match(nerockParser.T__8)
                self.state = 121
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
        self.enterRule(localctx, 24, self.RULE_atom)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 124
            _la = self._input.LA(1)
            if not((((_la) & ~0x3f) == 0 and ((1 << _la) & 24117248) != 0)):
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
        self.enterRule(localctx, 26, self.RULE_return)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 126
            self.match(nerockParser.T__9)
            self.state = 127
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
        self._predicates[6] = self.expr_sempred
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
         




