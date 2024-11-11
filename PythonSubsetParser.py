# Generated from PythonSubset.g4 by ANTLR 4.9.2
# encoding: utf-8
from antlr4 import *
from io import StringIO
import sys
if sys.version_info[1] > 5:
	from typing import TextIO
else:
	from typing.io import TextIO


def serializedATN():
    with StringIO() as buf:
        buf.write("\3\u608b\ua72a\u8133\ub9ed\u417c\u3be7\u7786\u5964\3\26")
        buf.write("I\4\2\t\2\4\3\t\3\4\4\t\4\4\5\t\5\4\6\t\6\4\7\t\7\3\2")
        buf.write("\6\2\20\n\2\r\2\16\2\21\3\2\3\2\3\3\3\3\5\3\30\n\3\3\4")
        buf.write("\3\4\3\4\3\4\3\4\3\4\3\4\5\4!\n\4\3\5\3\5\3\5\3\5\3\5")
        buf.write("\3\5\3\5\3\5\3\5\3\5\5\5-\n\5\3\5\3\5\3\5\3\5\3\5\3\5")
        buf.write("\7\5\65\n\5\f\5\16\58\13\5\3\6\3\6\3\7\3\7\3\7\3\7\7\7")
        buf.write("@\n\7\f\7\16\7C\13\7\5\7E\n\7\3\7\3\7\3\7\2\3\b\b\2\4")
        buf.write("\6\b\n\f\2\5\3\2\3\5\3\2\6\7\3\2\n\r\2N\2\17\3\2\2\2\4")
        buf.write("\27\3\2\2\2\6 \3\2\2\2\b,\3\2\2\2\n9\3\2\2\2\f;\3\2\2")
        buf.write("\2\16\20\5\4\3\2\17\16\3\2\2\2\20\21\3\2\2\2\21\17\3\2")
        buf.write("\2\2\21\22\3\2\2\2\22\23\3\2\2\2\23\24\7\2\2\3\24\3\3")
        buf.write("\2\2\2\25\30\5\6\4\2\26\30\5\b\5\2\27\25\3\2\2\2\27\26")
        buf.write("\3\2\2\2\30\5\3\2\2\2\31\32\7\22\2\2\32\33\7\21\2\2\33")
        buf.write("!\5\b\5\2\34\35\7\22\2\2\35\36\5\n\6\2\36\37\5\b\5\2\37")
        buf.write("!\3\2\2\2 \31\3\2\2\2 \34\3\2\2\2!\7\3\2\2\2\"#\b\5\1")
        buf.write("\2#$\7\b\2\2$%\5\b\5\2%&\7\t\2\2&-\3\2\2\2\'-\7\22\2\2")
        buf.write("(-\7\23\2\2)-\7\24\2\2*-\7\25\2\2+-\5\f\7\2,\"\3\2\2\2")
        buf.write(",\'\3\2\2\2,(\3\2\2\2,)\3\2\2\2,*\3\2\2\2,+\3\2\2\2-\66")
        buf.write("\3\2\2\2./\f\n\2\2/\60\t\2\2\2\60\65\5\b\5\13\61\62\f")
        buf.write("\t\2\2\62\63\t\3\2\2\63\65\5\b\5\n\64.\3\2\2\2\64\61\3")
        buf.write("\2\2\2\658\3\2\2\2\66\64\3\2\2\2\66\67\3\2\2\2\67\t\3")
        buf.write("\2\2\28\66\3\2\2\29:\t\4\2\2:\13\3\2\2\2;D\7\16\2\2<A")
        buf.write("\5\b\5\2=>\7\17\2\2>@\5\b\5\2?=\3\2\2\2@C\3\2\2\2A?\3")
        buf.write("\2\2\2AB\3\2\2\2BE\3\2\2\2CA\3\2\2\2D<\3\2\2\2DE\3\2\2")
        buf.write("\2EF\3\2\2\2FG\7\20\2\2G\r\3\2\2\2\n\21\27 ,\64\66AD")
        return buf.getvalue()


class PythonSubsetParser ( Parser ):

    grammarFileName = "PythonSubset.g4"

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    sharedContextCache = PredictionContextCache()

    literalNames = [ "<INVALID>", "'*'", "'/'", "'%'", "'+'", "'-'", "'('", 
                     "')'", "'+='", "'-='", "'*='", "'/='", "'['", "','", 
                     "']'", "'='" ]

    symbolicNames = [ "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "<INVALID>", "<INVALID>", "<INVALID>", "ASSIGN", "IDENTIFIER", 
                      "INT", "FLOAT", "STRING", "WS" ]

    RULE_program = 0
    RULE_statement = 1
    RULE_assignment = 2
    RULE_expr = 3
    RULE_compoundAssign = 4
    RULE_array = 5

    ruleNames =  [ "program", "statement", "assignment", "expr", "compoundAssign", 
                   "array" ]

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
    ASSIGN=15
    IDENTIFIER=16
    INT=17
    FLOAT=18
    STRING=19
    WS=20

    def __init__(self, input:TokenStream, output:TextIO = sys.stdout):
        super().__init__(input, output)
        self.checkVersion("4.9.2")
        self._interp = ParserATNSimulator(self, self.atn, self.decisionsToDFA, self.sharedContextCache)
        self._predicates = None




    class ProgramContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def EOF(self):
            return self.getToken(PythonSubsetParser.EOF, 0)

        def statement(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(PythonSubsetParser.StatementContext)
            else:
                return self.getTypedRuleContext(PythonSubsetParser.StatementContext,i)


        def getRuleIndex(self):
            return PythonSubsetParser.RULE_program

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterProgram" ):
                listener.enterProgram(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitProgram" ):
                listener.exitProgram(self)




    def program(self):

        localctx = PythonSubsetParser.ProgramContext(self, self._ctx, self.state)
        self.enterRule(localctx, 0, self.RULE_program)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 13 
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while True:
                self.state = 12
                self.statement()
                self.state = 15 
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if not ((((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << PythonSubsetParser.T__5) | (1 << PythonSubsetParser.T__11) | (1 << PythonSubsetParser.IDENTIFIER) | (1 << PythonSubsetParser.INT) | (1 << PythonSubsetParser.FLOAT) | (1 << PythonSubsetParser.STRING))) != 0)):
                    break

            self.state = 17
            self.match(PythonSubsetParser.EOF)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class StatementContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def assignment(self):
            return self.getTypedRuleContext(PythonSubsetParser.AssignmentContext,0)


        def expr(self):
            return self.getTypedRuleContext(PythonSubsetParser.ExprContext,0)


        def getRuleIndex(self):
            return PythonSubsetParser.RULE_statement

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterStatement" ):
                listener.enterStatement(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitStatement" ):
                listener.exitStatement(self)




    def statement(self):

        localctx = PythonSubsetParser.StatementContext(self, self._ctx, self.state)
        self.enterRule(localctx, 2, self.RULE_statement)
        try:
            self.state = 21
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,1,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 19
                self.assignment()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 20
                self.expr(0)
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class AssignmentContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def IDENTIFIER(self):
            return self.getToken(PythonSubsetParser.IDENTIFIER, 0)

        def ASSIGN(self):
            return self.getToken(PythonSubsetParser.ASSIGN, 0)

        def expr(self):
            return self.getTypedRuleContext(PythonSubsetParser.ExprContext,0)


        def compoundAssign(self):
            return self.getTypedRuleContext(PythonSubsetParser.CompoundAssignContext,0)


        def getRuleIndex(self):
            return PythonSubsetParser.RULE_assignment

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterAssignment" ):
                listener.enterAssignment(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitAssignment" ):
                listener.exitAssignment(self)




    def assignment(self):

        localctx = PythonSubsetParser.AssignmentContext(self, self._ctx, self.state)
        self.enterRule(localctx, 4, self.RULE_assignment)
        try:
            self.state = 30
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,2,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 23
                self.match(PythonSubsetParser.IDENTIFIER)
                self.state = 24
                self.match(PythonSubsetParser.ASSIGN)
                self.state = 25
                self.expr(0)
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 26
                self.match(PythonSubsetParser.IDENTIFIER)
                self.state = 27
                self.compoundAssign()
                self.state = 28
                self.expr(0)
                pass


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
            self.op = None # Token

        def expr(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(PythonSubsetParser.ExprContext)
            else:
                return self.getTypedRuleContext(PythonSubsetParser.ExprContext,i)


        def IDENTIFIER(self):
            return self.getToken(PythonSubsetParser.IDENTIFIER, 0)

        def INT(self):
            return self.getToken(PythonSubsetParser.INT, 0)

        def FLOAT(self):
            return self.getToken(PythonSubsetParser.FLOAT, 0)

        def STRING(self):
            return self.getToken(PythonSubsetParser.STRING, 0)

        def array(self):
            return self.getTypedRuleContext(PythonSubsetParser.ArrayContext,0)


        def getRuleIndex(self):
            return PythonSubsetParser.RULE_expr

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterExpr" ):
                listener.enterExpr(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitExpr" ):
                listener.exitExpr(self)



    def expr(self, _p:int=0):
        _parentctx = self._ctx
        _parentState = self.state
        localctx = PythonSubsetParser.ExprContext(self, self._ctx, _parentState)
        _prevctx = localctx
        _startState = 6
        self.enterRecursionRule(localctx, 6, self.RULE_expr, _p)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 42
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [PythonSubsetParser.T__5]:
                self.state = 33
                self.match(PythonSubsetParser.T__5)
                self.state = 34
                self.expr(0)
                self.state = 35
                self.match(PythonSubsetParser.T__6)
                pass
            elif token in [PythonSubsetParser.IDENTIFIER]:
                self.state = 37
                self.match(PythonSubsetParser.IDENTIFIER)
                pass
            elif token in [PythonSubsetParser.INT]:
                self.state = 38
                self.match(PythonSubsetParser.INT)
                pass
            elif token in [PythonSubsetParser.FLOAT]:
                self.state = 39
                self.match(PythonSubsetParser.FLOAT)
                pass
            elif token in [PythonSubsetParser.STRING]:
                self.state = 40
                self.match(PythonSubsetParser.STRING)
                pass
            elif token in [PythonSubsetParser.T__11]:
                self.state = 41
                self.array()
                pass
            else:
                raise NoViableAltException(self)

            self._ctx.stop = self._input.LT(-1)
            self.state = 52
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,5,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    self.state = 50
                    self._errHandler.sync(self)
                    la_ = self._interp.adaptivePredict(self._input,4,self._ctx)
                    if la_ == 1:
                        localctx = PythonSubsetParser.ExprContext(self, _parentctx, _parentState)
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_expr)
                        self.state = 44
                        if not self.precpred(self._ctx, 8):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 8)")
                        self.state = 45
                        localctx.op = self._input.LT(1)
                        _la = self._input.LA(1)
                        if not((((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << PythonSubsetParser.T__0) | (1 << PythonSubsetParser.T__1) | (1 << PythonSubsetParser.T__2))) != 0)):
                            localctx.op = self._errHandler.recoverInline(self)
                        else:
                            self._errHandler.reportMatch(self)
                            self.consume()
                        self.state = 46
                        self.expr(9)
                        pass

                    elif la_ == 2:
                        localctx = PythonSubsetParser.ExprContext(self, _parentctx, _parentState)
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_expr)
                        self.state = 47
                        if not self.precpred(self._ctx, 7):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 7)")
                        self.state = 48
                        localctx.op = self._input.LT(1)
                        _la = self._input.LA(1)
                        if not(_la==PythonSubsetParser.T__3 or _la==PythonSubsetParser.T__4):
                            localctx.op = self._errHandler.recoverInline(self)
                        else:
                            self._errHandler.reportMatch(self)
                            self.consume()
                        self.state = 49
                        self.expr(8)
                        pass

             
                self.state = 54
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,5,self._ctx)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.unrollRecursionContexts(_parentctx)
        return localctx


    class CompoundAssignContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser


        def getRuleIndex(self):
            return PythonSubsetParser.RULE_compoundAssign

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterCompoundAssign" ):
                listener.enterCompoundAssign(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitCompoundAssign" ):
                listener.exitCompoundAssign(self)




    def compoundAssign(self):

        localctx = PythonSubsetParser.CompoundAssignContext(self, self._ctx, self.state)
        self.enterRule(localctx, 8, self.RULE_compoundAssign)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 55
            _la = self._input.LA(1)
            if not((((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << PythonSubsetParser.T__7) | (1 << PythonSubsetParser.T__8) | (1 << PythonSubsetParser.T__9) | (1 << PythonSubsetParser.T__10))) != 0)):
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


    class ArrayContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def expr(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(PythonSubsetParser.ExprContext)
            else:
                return self.getTypedRuleContext(PythonSubsetParser.ExprContext,i)


        def getRuleIndex(self):
            return PythonSubsetParser.RULE_array

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterArray" ):
                listener.enterArray(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitArray" ):
                listener.exitArray(self)




    def array(self):

        localctx = PythonSubsetParser.ArrayContext(self, self._ctx, self.state)
        self.enterRule(localctx, 10, self.RULE_array)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 57
            self.match(PythonSubsetParser.T__11)
            self.state = 66
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if (((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << PythonSubsetParser.T__5) | (1 << PythonSubsetParser.T__11) | (1 << PythonSubsetParser.IDENTIFIER) | (1 << PythonSubsetParser.INT) | (1 << PythonSubsetParser.FLOAT) | (1 << PythonSubsetParser.STRING))) != 0):
                self.state = 58
                self.expr(0)
                self.state = 63
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                while _la==PythonSubsetParser.T__12:
                    self.state = 59
                    self.match(PythonSubsetParser.T__12)
                    self.state = 60
                    self.expr(0)
                    self.state = 65
                    self._errHandler.sync(self)
                    _la = self._input.LA(1)



            self.state = 68
            self.match(PythonSubsetParser.T__13)
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
        self._predicates[3] = self.expr_sempred
        pred = self._predicates.get(ruleIndex, None)
        if pred is None:
            raise Exception("No predicate with index:" + str(ruleIndex))
        else:
            return pred(localctx, predIndex)

    def expr_sempred(self, localctx:ExprContext, predIndex:int):
            if predIndex == 0:
                return self.precpred(self._ctx, 8)
         

            if predIndex == 1:
                return self.precpred(self._ctx, 7)
         




