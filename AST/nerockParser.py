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
        4,1,24,120,2,0,7,0,2,1,7,1,2,2,7,2,2,3,7,3,2,4,7,4,2,5,7,5,2,6,7,
        6,2,7,7,7,2,8,7,8,2,9,7,9,2,10,7,10,2,11,7,11,1,0,4,0,26,8,0,11,
        0,12,0,27,1,0,1,0,1,1,1,1,1,1,1,1,3,1,36,8,1,1,2,1,2,5,2,40,8,2,
        10,2,12,2,43,9,2,1,2,1,2,1,3,1,3,1,3,1,3,1,3,1,3,1,4,1,4,1,4,1,4,
        1,4,1,4,1,5,1,5,1,5,1,5,1,5,1,5,5,5,65,8,5,10,5,12,5,68,9,5,3,5,
        70,8,5,1,5,1,5,3,5,74,8,5,1,5,1,5,1,5,1,5,1,5,1,5,1,5,1,5,1,5,1,
        5,1,5,1,5,5,5,88,8,5,10,5,12,5,91,9,5,1,6,1,6,1,7,1,7,1,7,1,8,1,
        8,1,8,1,8,5,8,102,8,8,10,8,12,8,105,9,8,3,8,107,8,8,1,8,1,8,1,9,
        1,9,3,9,113,8,9,1,10,1,10,1,11,1,11,1,11,1,11,0,1,10,12,0,2,4,6,
        8,10,12,14,16,18,20,22,0,2,1,0,15,18,2,0,19,21,23,23,122,0,25,1,
        0,0,0,2,35,1,0,0,0,4,37,1,0,0,0,6,46,1,0,0,0,8,52,1,0,0,0,10,73,
        1,0,0,0,12,92,1,0,0,0,14,94,1,0,0,0,16,97,1,0,0,0,18,112,1,0,0,0,
        20,114,1,0,0,0,22,116,1,0,0,0,24,26,3,2,1,0,25,24,1,0,0,0,26,27,
        1,0,0,0,27,25,1,0,0,0,27,28,1,0,0,0,28,29,1,0,0,0,29,30,5,0,0,1,
        30,1,1,0,0,0,31,36,3,6,3,0,32,36,3,10,5,0,33,36,3,8,4,0,34,36,3,
        22,11,0,35,31,1,0,0,0,35,32,1,0,0,0,35,33,1,0,0,0,35,34,1,0,0,0,
        36,3,1,0,0,0,37,41,5,1,0,0,38,40,3,2,1,0,39,38,1,0,0,0,40,43,1,0,
        0,0,41,39,1,0,0,0,41,42,1,0,0,0,42,44,1,0,0,0,43,41,1,0,0,0,44,45,
        5,2,0,0,45,5,1,0,0,0,46,47,5,14,0,0,47,48,5,19,0,0,48,49,3,16,8,
        0,49,50,3,18,9,0,50,51,3,4,2,0,51,7,1,0,0,0,52,53,5,3,0,0,53,54,
        5,19,0,0,54,55,3,12,6,0,55,56,5,4,0,0,56,57,3,10,5,0,57,9,1,0,0,
        0,58,59,6,5,-1,0,59,60,5,19,0,0,60,69,5,5,0,0,61,66,3,10,5,0,62,
        63,5,6,0,0,63,65,3,10,5,0,64,62,1,0,0,0,65,68,1,0,0,0,66,64,1,0,
        0,0,66,67,1,0,0,0,67,70,1,0,0,0,68,66,1,0,0,0,69,61,1,0,0,0,69,70,
        1,0,0,0,70,71,1,0,0,0,71,74,5,7,0,0,72,74,3,20,10,0,73,58,1,0,0,
        0,73,72,1,0,0,0,74,89,1,0,0,0,75,76,10,4,0,0,76,77,5,12,0,0,77,88,
        3,10,5,5,78,79,10,3,0,0,79,80,5,13,0,0,80,88,3,10,5,4,81,82,10,2,
        0,0,82,83,5,10,0,0,83,88,3,10,5,3,84,85,10,1,0,0,85,86,5,11,0,0,
        86,88,3,10,5,2,87,75,1,0,0,0,87,78,1,0,0,0,87,81,1,0,0,0,87,84,1,
        0,0,0,88,91,1,0,0,0,89,87,1,0,0,0,89,90,1,0,0,0,90,11,1,0,0,0,91,
        89,1,0,0,0,92,93,7,0,0,0,93,13,1,0,0,0,94,95,3,12,6,0,95,96,5,19,
        0,0,96,15,1,0,0,0,97,106,5,5,0,0,98,103,3,14,7,0,99,100,5,6,0,0,
        100,102,3,14,7,0,101,99,1,0,0,0,102,105,1,0,0,0,103,101,1,0,0,0,
        103,104,1,0,0,0,104,107,1,0,0,0,105,103,1,0,0,0,106,98,1,0,0,0,106,
        107,1,0,0,0,107,108,1,0,0,0,108,109,5,7,0,0,109,17,1,0,0,0,110,111,
        5,8,0,0,111,113,3,12,6,0,112,110,1,0,0,0,112,113,1,0,0,0,113,19,
        1,0,0,0,114,115,7,1,0,0,115,21,1,0,0,0,116,117,5,9,0,0,117,118,3,
        20,10,0,118,23,1,0,0,0,11,27,35,41,66,69,73,87,89,103,106,112
    ]

class nerockParser ( Parser ):

    grammarFileName = "nerock.g4"

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    sharedContextCache = PredictionContextCache()

    literalNames = [ "<INVALID>", "'{'", "'}'", "'var'", "'='", "'('", "','", 
                     "')'", "'->'", "'return'", "'+'", "'-'", "'*'", "'/'", 
                     "'decl'", "'i32'", "'str'", "'f32'", "'v'" ]

    symbolicNames = [ "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "<INVALID>", "<INVALID>", "PLUS", "MIN", "MUL", "DIV", 
                      "DECL_FUNC", "INT_TYPE", "STRING_TYPE", "FLOAT_TYPE", 
                      "VOID_TYPE", "ID", "FLOAT", "NUM", "COMMENT", "STRING", 
                      "WS" ]

    RULE_prog = 0
    RULE_command = 1
    RULE_block = 2
    RULE_func_decleration = 3
    RULE_decl_var = 4
    RULE_expr = 5
    RULE_typesKeyword = 6
    RULE_param = 7
    RULE_paramList = 8
    RULE_returnFunc = 9
    RULE_atom = 10
    RULE_return = 11

    ruleNames =  [ "prog", "command", "block", "func_decleration", "decl_var", 
                   "expr", "typesKeyword", "param", "paramList", "returnFunc", 
                   "atom", "return" ]

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
    PLUS=10
    MIN=11
    MUL=12
    DIV=13
    DECL_FUNC=14
    INT_TYPE=15
    STRING_TYPE=16
    FLOAT_TYPE=17
    VOID_TYPE=18
    ID=19
    FLOAT=20
    NUM=21
    COMMENT=22
    STRING=23
    WS=24

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
            self.state = 25 
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while True:
                self.state = 24
                self.command()
                self.state = 27 
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if not ((((_la) & ~0x3f) == 0 and ((1 << _la) & 12075528) != 0)):
                    break

            self.state = 29
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
            self.state = 35
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [14]:
                self.enterOuterAlt(localctx, 1)
                self.state = 31
                self.func_decleration()
                pass
            elif token in [19, 20, 21, 23]:
                self.enterOuterAlt(localctx, 2)
                self.state = 32
                self.expr(0)
                pass
            elif token in [3]:
                self.enterOuterAlt(localctx, 3)
                self.state = 33
                self.decl_var()
                pass
            elif token in [9]:
                self.enterOuterAlt(localctx, 4)
                self.state = 34
                self.return_()
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
            self.state = 37
            self.match(nerockParser.T__0)
            self.state = 41
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while (((_la) & ~0x3f) == 0 and ((1 << _la) & 12075528) != 0):
                self.state = 38
                self.command()
                self.state = 43
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 44
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
            self.state = 46
            self.match(nerockParser.DECL_FUNC)
            self.state = 47
            self.match(nerockParser.ID)
            self.state = 48
            self.paramList()
            self.state = 49
            self.returnFunc()
            self.state = 50
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
            self.state = 52
            self.match(nerockParser.T__2)
            self.state = 53
            self.match(nerockParser.ID)
            self.state = 54
            self.typesKeyword()
            self.state = 55
            self.match(nerockParser.T__3)
            self.state = 56
            self.expr(0)
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

        def ID(self):
            return self.getToken(nerockParser.ID, 0)

        def expr(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(nerockParser.ExprContext)
            else:
                return self.getTypedRuleContext(nerockParser.ExprContext,i)


        def atom(self):
            return self.getTypedRuleContext(nerockParser.AtomContext,0)


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
        _startState = 10
        self.enterRecursionRule(localctx, 10, self.RULE_expr, _p)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 73
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,5,self._ctx)
            if la_ == 1:
                self.state = 59
                self.match(nerockParser.ID)
                self.state = 60
                self.match(nerockParser.T__4)
                self.state = 69
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if (((_la) & ~0x3f) == 0 and ((1 << _la) & 12058624) != 0):
                    self.state = 61
                    self.expr(0)
                    self.state = 66
                    self._errHandler.sync(self)
                    _la = self._input.LA(1)
                    while _la==6:
                        self.state = 62
                        self.match(nerockParser.T__5)
                        self.state = 63
                        self.expr(0)
                        self.state = 68
                        self._errHandler.sync(self)
                        _la = self._input.LA(1)



                self.state = 71
                self.match(nerockParser.T__6)
                pass

            elif la_ == 2:
                self.state = 72
                self.atom()
                pass


            self._ctx.stop = self._input.LT(-1)
            self.state = 89
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,7,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    self.state = 87
                    self._errHandler.sync(self)
                    la_ = self._interp.adaptivePredict(self._input,6,self._ctx)
                    if la_ == 1:
                        localctx = nerockParser.ExprContext(self, _parentctx, _parentState)
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_expr)
                        self.state = 75
                        if not self.precpred(self._ctx, 4):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 4)")
                        self.state = 76
                        self.match(nerockParser.MUL)
                        self.state = 77
                        self.expr(5)
                        pass

                    elif la_ == 2:
                        localctx = nerockParser.ExprContext(self, _parentctx, _parentState)
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_expr)
                        self.state = 78
                        if not self.precpred(self._ctx, 3):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 3)")
                        self.state = 79
                        self.match(nerockParser.DIV)
                        self.state = 80
                        self.expr(4)
                        pass

                    elif la_ == 3:
                        localctx = nerockParser.ExprContext(self, _parentctx, _parentState)
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_expr)
                        self.state = 81
                        if not self.precpred(self._ctx, 2):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 2)")
                        self.state = 82
                        self.match(nerockParser.PLUS)
                        self.state = 83
                        self.expr(3)
                        pass

                    elif la_ == 4:
                        localctx = nerockParser.ExprContext(self, _parentctx, _parentState)
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_expr)
                        self.state = 84
                        if not self.precpred(self._ctx, 1):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 1)")
                        self.state = 85
                        self.match(nerockParser.MIN)
                        self.state = 86
                        self.expr(2)
                        pass

             
                self.state = 91
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
        self.enterRule(localctx, 12, self.RULE_typesKeyword)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 92
            _la = self._input.LA(1)
            if not((((_la) & ~0x3f) == 0 and ((1 << _la) & 491520) != 0)):
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
        self.enterRule(localctx, 14, self.RULE_param)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 94
            self.typesKeyword()
            self.state = 95
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
        self.enterRule(localctx, 16, self.RULE_paramList)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 97
            self.match(nerockParser.T__4)
            self.state = 106
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if (((_la) & ~0x3f) == 0 and ((1 << _la) & 491520) != 0):
                self.state = 98
                self.param()
                self.state = 103
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                while _la==6:
                    self.state = 99
                    self.match(nerockParser.T__5)
                    self.state = 100
                    self.param()
                    self.state = 105
                    self._errHandler.sync(self)
                    _la = self._input.LA(1)



            self.state = 108
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
        self.enterRule(localctx, 18, self.RULE_returnFunc)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 112
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==8:
                self.state = 110
                self.match(nerockParser.T__7)
                self.state = 111
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
        self.enterRule(localctx, 20, self.RULE_atom)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 114
            _la = self._input.LA(1)
            if not((((_la) & ~0x3f) == 0 and ((1 << _la) & 12058624) != 0)):
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

        def atom(self):
            return self.getTypedRuleContext(nerockParser.AtomContext,0)


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
        self.enterRule(localctx, 22, self.RULE_return)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 116
            self.match(nerockParser.T__8)
            self.state = 117
            self.atom()
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
        self._predicates[5] = self.expr_sempred
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
         




