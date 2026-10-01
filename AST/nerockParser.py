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
        4,1,23,114,2,0,7,0,2,1,7,1,2,2,7,2,2,3,7,3,2,4,7,4,2,5,7,5,2,6,7,
        6,2,7,7,7,2,8,7,8,2,9,7,9,2,10,7,10,1,0,4,0,24,8,0,11,0,12,0,25,
        1,0,1,0,1,1,1,1,1,1,3,1,33,8,1,1,2,1,2,5,2,37,8,2,10,2,12,2,40,9,
        2,1,2,1,2,1,3,1,3,1,3,1,3,1,3,1,3,1,4,1,4,1,4,1,4,1,4,1,4,1,5,1,
        5,1,5,1,5,1,5,1,5,5,5,62,8,5,10,5,12,5,65,9,5,3,5,67,8,5,1,5,1,5,
        3,5,71,8,5,1,5,1,5,1,5,1,5,1,5,1,5,1,5,1,5,1,5,1,5,1,5,1,5,5,5,85,
        8,5,10,5,12,5,88,9,5,1,6,1,6,1,7,1,7,1,7,1,8,1,8,1,8,1,8,5,8,99,
        8,8,10,8,12,8,102,9,8,3,8,104,8,8,1,8,1,8,1,9,1,9,3,9,110,8,9,1,
        10,1,10,1,10,0,1,10,11,0,2,4,6,8,10,12,14,16,18,20,0,2,1,0,14,17,
        2,0,18,20,22,22,116,0,23,1,0,0,0,2,32,1,0,0,0,4,34,1,0,0,0,6,43,
        1,0,0,0,8,49,1,0,0,0,10,70,1,0,0,0,12,89,1,0,0,0,14,91,1,0,0,0,16,
        94,1,0,0,0,18,109,1,0,0,0,20,111,1,0,0,0,22,24,3,2,1,0,23,22,1,0,
        0,0,24,25,1,0,0,0,25,23,1,0,0,0,25,26,1,0,0,0,26,27,1,0,0,0,27,28,
        5,0,0,1,28,1,1,0,0,0,29,33,3,6,3,0,30,33,3,10,5,0,31,33,3,8,4,0,
        32,29,1,0,0,0,32,30,1,0,0,0,32,31,1,0,0,0,33,3,1,0,0,0,34,38,5,1,
        0,0,35,37,3,2,1,0,36,35,1,0,0,0,37,40,1,0,0,0,38,36,1,0,0,0,38,39,
        1,0,0,0,39,41,1,0,0,0,40,38,1,0,0,0,41,42,5,2,0,0,42,5,1,0,0,0,43,
        44,5,13,0,0,44,45,5,18,0,0,45,46,3,16,8,0,46,47,3,18,9,0,47,48,3,
        4,2,0,48,7,1,0,0,0,49,50,5,3,0,0,50,51,5,18,0,0,51,52,3,12,6,0,52,
        53,5,4,0,0,53,54,3,10,5,0,54,9,1,0,0,0,55,56,6,5,-1,0,56,57,5,18,
        0,0,57,66,5,5,0,0,58,63,3,10,5,0,59,60,5,6,0,0,60,62,3,10,5,0,61,
        59,1,0,0,0,62,65,1,0,0,0,63,61,1,0,0,0,63,64,1,0,0,0,64,67,1,0,0,
        0,65,63,1,0,0,0,66,58,1,0,0,0,66,67,1,0,0,0,67,68,1,0,0,0,68,71,
        5,7,0,0,69,71,3,20,10,0,70,55,1,0,0,0,70,69,1,0,0,0,71,86,1,0,0,
        0,72,73,10,4,0,0,73,74,5,11,0,0,74,85,3,10,5,5,75,76,10,3,0,0,76,
        77,5,12,0,0,77,85,3,10,5,4,78,79,10,2,0,0,79,80,5,9,0,0,80,85,3,
        10,5,3,81,82,10,1,0,0,82,83,5,10,0,0,83,85,3,10,5,2,84,72,1,0,0,
        0,84,75,1,0,0,0,84,78,1,0,0,0,84,81,1,0,0,0,85,88,1,0,0,0,86,84,
        1,0,0,0,86,87,1,0,0,0,87,11,1,0,0,0,88,86,1,0,0,0,89,90,7,0,0,0,
        90,13,1,0,0,0,91,92,3,12,6,0,92,93,5,18,0,0,93,15,1,0,0,0,94,103,
        5,5,0,0,95,100,3,14,7,0,96,97,5,6,0,0,97,99,3,14,7,0,98,96,1,0,0,
        0,99,102,1,0,0,0,100,98,1,0,0,0,100,101,1,0,0,0,101,104,1,0,0,0,
        102,100,1,0,0,0,103,95,1,0,0,0,103,104,1,0,0,0,104,105,1,0,0,0,105,
        106,5,7,0,0,106,17,1,0,0,0,107,108,5,8,0,0,108,110,3,12,6,0,109,
        107,1,0,0,0,109,110,1,0,0,0,110,19,1,0,0,0,111,112,7,1,0,0,112,21,
        1,0,0,0,11,25,32,38,63,66,70,84,86,100,103,109
    ]

class nerockParser ( Parser ):

    grammarFileName = "nerock.g4"

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    sharedContextCache = PredictionContextCache()

    literalNames = [ "<INVALID>", "'{'", "'}'", "'var'", "'='", "'('", "','", 
                     "')'", "'->'", "'+'", "'-'", "'*'", "'/'", "'decl'", 
                     "'i32'", "'str'", "'f32'", "'v'" ]

    symbolicNames = [ "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "<INVALID>", "PLUS", "MIN", "MUL", "DIV", "DECL_FUNC", 
                      "INT_TYPE", "STRING_TYPE", "FLOAT_TYPE", "VOID_TYPE", 
                      "ID", "FLOAT", "NUM", "COMMENT", "STRING", "WS" ]

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

    ruleNames =  [ "prog", "command", "block", "func_decleration", "decl_var", 
                   "expr", "typesKeyword", "param", "paramList", "returnFunc", 
                   "atom" ]

    EOF = Token.EOF
    T__0=1
    T__1=2
    T__2=3
    T__3=4
    T__4=5
    T__5=6
    T__6=7
    T__7=8
    PLUS=9
    MIN=10
    MUL=11
    DIV=12
    DECL_FUNC=13
    INT_TYPE=14
    STRING_TYPE=15
    FLOAT_TYPE=16
    VOID_TYPE=17
    ID=18
    FLOAT=19
    NUM=20
    COMMENT=21
    STRING=22
    WS=23

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
            self.state = 23 
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while True:
                self.state = 22
                self.command()
                self.state = 25 
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if not ((((_la) & ~0x3f) == 0 and ((1 << _la) & 6037512) != 0)):
                    break

            self.state = 27
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
            self.state = 32
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [13]:
                self.enterOuterAlt(localctx, 1)
                self.state = 29
                self.func_decleration()
                pass
            elif token in [18, 19, 20, 22]:
                self.enterOuterAlt(localctx, 2)
                self.state = 30
                self.expr(0)
                pass
            elif token in [3]:
                self.enterOuterAlt(localctx, 3)
                self.state = 31
                self.decl_var()
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
            self.state = 34
            self.match(nerockParser.T__0)
            self.state = 38
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while (((_la) & ~0x3f) == 0 and ((1 << _la) & 6037512) != 0):
                self.state = 35
                self.command()
                self.state = 40
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 41
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
            self.state = 43
            self.match(nerockParser.DECL_FUNC)
            self.state = 44
            self.match(nerockParser.ID)
            self.state = 45
            self.paramList()
            self.state = 46
            self.returnFunc()
            self.state = 47
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
            self.state = 49
            self.match(nerockParser.T__2)
            self.state = 50
            self.match(nerockParser.ID)
            self.state = 51
            self.typesKeyword()
            self.state = 52
            self.match(nerockParser.T__3)
            self.state = 53
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
            self.state = 70
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,5,self._ctx)
            if la_ == 1:
                self.state = 56
                self.match(nerockParser.ID)
                self.state = 57
                self.match(nerockParser.T__4)
                self.state = 66
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if (((_la) & ~0x3f) == 0 and ((1 << _la) & 6029312) != 0):
                    self.state = 58
                    self.expr(0)
                    self.state = 63
                    self._errHandler.sync(self)
                    _la = self._input.LA(1)
                    while _la==6:
                        self.state = 59
                        self.match(nerockParser.T__5)
                        self.state = 60
                        self.expr(0)
                        self.state = 65
                        self._errHandler.sync(self)
                        _la = self._input.LA(1)



                self.state = 68
                self.match(nerockParser.T__6)
                pass

            elif la_ == 2:
                self.state = 69
                self.atom()
                pass


            self._ctx.stop = self._input.LT(-1)
            self.state = 86
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,7,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    self.state = 84
                    self._errHandler.sync(self)
                    la_ = self._interp.adaptivePredict(self._input,6,self._ctx)
                    if la_ == 1:
                        localctx = nerockParser.ExprContext(self, _parentctx, _parentState)
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_expr)
                        self.state = 72
                        if not self.precpred(self._ctx, 4):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 4)")
                        self.state = 73
                        self.match(nerockParser.MUL)
                        self.state = 74
                        self.expr(5)
                        pass

                    elif la_ == 2:
                        localctx = nerockParser.ExprContext(self, _parentctx, _parentState)
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_expr)
                        self.state = 75
                        if not self.precpred(self._ctx, 3):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 3)")
                        self.state = 76
                        self.match(nerockParser.DIV)
                        self.state = 77
                        self.expr(4)
                        pass

                    elif la_ == 3:
                        localctx = nerockParser.ExprContext(self, _parentctx, _parentState)
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_expr)
                        self.state = 78
                        if not self.precpred(self._ctx, 2):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 2)")
                        self.state = 79
                        self.match(nerockParser.PLUS)
                        self.state = 80
                        self.expr(3)
                        pass

                    elif la_ == 4:
                        localctx = nerockParser.ExprContext(self, _parentctx, _parentState)
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_expr)
                        self.state = 81
                        if not self.precpred(self._ctx, 1):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 1)")
                        self.state = 82
                        self.match(nerockParser.MIN)
                        self.state = 83
                        self.expr(2)
                        pass

             
                self.state = 88
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
            self.state = 89
            _la = self._input.LA(1)
            if not((((_la) & ~0x3f) == 0 and ((1 << _la) & 245760) != 0)):
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
            self.state = 91
            self.typesKeyword()
            self.state = 92
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
            self.state = 94
            self.match(nerockParser.T__4)
            self.state = 103
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if (((_la) & ~0x3f) == 0 and ((1 << _la) & 245760) != 0):
                self.state = 95
                self.param()
                self.state = 100
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                while _la==6:
                    self.state = 96
                    self.match(nerockParser.T__5)
                    self.state = 97
                    self.param()
                    self.state = 102
                    self._errHandler.sync(self)
                    _la = self._input.LA(1)



            self.state = 105
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
            self.state = 109
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==8:
                self.state = 107
                self.match(nerockParser.T__7)
                self.state = 108
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
            self.state = 111
            _la = self._input.LA(1)
            if not((((_la) & ~0x3f) == 0 and ((1 << _la) & 6029312) != 0)):
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
         




