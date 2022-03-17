# Generated from c:\Users\villa\Documents\Compiladores\antlr\marzo.g4 by ANTLR 4.9.3
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
        buf.write("\3\u608b\ua72a\u8133\ub9ed\u417c\u3be7\u7786\u5964\3\31")
        buf.write("Q\4\2\t\2\4\3\t\3\4\4\t\4\3\2\3\2\6\2\13\n\2\r\2\16\2")
        buf.write("\f\3\3\3\3\3\3\3\3\3\3\3\3\3\3\5\3\26\n\3\3\3\3\3\3\3")
        buf.write("\3\3\3\3\3\3\3\3\3\3\3\3\3\3\3\3\3\3\3\3\3\3\3\3\3\3\3")
        buf.write("\3\3\3\3\3\3\3\3\3\3\3\3\3\3\3\3\3\3\3\3\3\3\3\3\3\3\3")
        buf.write("\7\3\66\n\3\f\3\16\39\13\3\3\4\3\4\3\4\3\4\3\4\3\4\3\4")
        buf.write("\3\4\3\4\3\4\3\4\3\4\3\4\3\4\3\4\3\4\3\4\3\4\3\4\3\4\5")
        buf.write("\4O\n\4\3\4\2\3\4\5\2\4\6\2\2\2a\2\n\3\2\2\2\4\25\3\2")
        buf.write("\2\2\6N\3\2\2\2\b\13\5\4\3\2\t\13\5\6\4\2\n\b\3\2\2\2")
        buf.write("\n\t\3\2\2\2\13\f\3\2\2\2\f\n\3\2\2\2\f\r\3\2\2\2\r\3")
        buf.write("\3\2\2\2\16\17\b\3\1\2\17\20\7\3\2\2\20\21\5\4\3\2\21")
        buf.write("\22\7\4\2\2\22\26\3\2\2\2\23\26\7\b\2\2\24\26\7\6\2\2")
        buf.write("\25\16\3\2\2\2\25\23\3\2\2\2\25\24\3\2\2\2\26\67\3\2\2")
        buf.write("\2\27\30\f\17\2\2\30\31\7\17\2\2\31\66\5\4\3\20\32\33")
        buf.write("\f\16\2\2\33\34\7\20\2\2\34\66\5\4\3\17\35\36\f\r\2\2")
        buf.write("\36\37\7\21\2\2\37\66\5\4\3\16 !\f\f\2\2!\"\7\22\2\2\"")
        buf.write("\66\5\4\3\r#$\f\13\2\2$%\7\23\2\2%\66\5\4\3\f&\'\f\n\2")
        buf.write("\2\'(\7\24\2\2(\66\5\4\3\13)*\f\t\2\2*+\7\25\2\2+\66\5")
        buf.write("\4\3\n,-\f\b\2\2-.\7\26\2\2.\66\5\4\3\t/\60\f\7\2\2\60")
        buf.write("\61\7\27\2\2\61\66\5\4\3\b\62\63\f\6\2\2\63\64\7\31\2")
        buf.write("\2\64\66\5\4\3\7\65\27\3\2\2\2\65\32\3\2\2\2\65\35\3\2")
        buf.write("\2\2\65 \3\2\2\2\65#\3\2\2\2\65&\3\2\2\2\65)\3\2\2\2\65")
        buf.write(",\3\2\2\2\65/\3\2\2\2\65\62\3\2\2\2\669\3\2\2\2\67\65")
        buf.write("\3\2\2\2\678\3\2\2\28\5\3\2\2\29\67\3\2\2\2:;\7\6\2\2")
        buf.write(";<\7\n\2\2<O\5\4\3\2=>\7\6\2\2>?\7\t\2\2?O\5\4\3\2@A\7")
        buf.write("\6\2\2AB\7\13\2\2BO\5\4\3\2CD\7\6\2\2DE\7\f\2\2EO\5\4")
        buf.write("\3\2FG\7\6\2\2GH\7\r\2\2HO\5\4\3\2IJ\7\6\2\2JK\7\16\2")
        buf.write("\2KO\5\4\3\2LM\7\5\2\2MO\7\6\2\2N:\3\2\2\2N=\3\2\2\2N")
        buf.write("@\3\2\2\2NC\3\2\2\2NF\3\2\2\2NI\3\2\2\2NL\3\2\2\2O\7\3")
        buf.write("\2\2\2\b\n\f\25\65\67N")
        return buf.getvalue()


class marzoParser ( Parser ):

    grammarFileName = "marzo.g4"

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    sharedContextCache = PredictionContextCache()

    literalNames = [ "<INVALID>", "'('", "')'", "'int'", "<INVALID>", "<INVALID>", 
                     "<INVALID>", "'+='", "'='", "'/='", "'%='", "'*='", 
                     "'^='", "'=='", "'<='", "'<'", "'>='", "'>'", "'+'", 
                     "'/'", "'%'", "'*'", "'^'", "'-'" ]

    symbolicNames = [ "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "VAR", "WS", "INT", "ADD_ASSIGN", "ASSIGN", "DIVIDE_ASSIGN", 
                      "MOD_ASSIGN", "MULTIPLY_ASSIGN", "POWER_ASSIGN", "EQ", 
                      "LE", "LT", "ME", "MT", "ADD", "DIVIDE", "MOD", "MULTIPLY", 
                      "POWER", "SUBSTRACT" ]

    RULE_program = 0
    RULE_expression = 1
    RULE_statement = 2

    ruleNames =  [ "program", "expression", "statement" ]

    EOF = Token.EOF
    T__0=1
    T__1=2
    T__2=3
    VAR=4
    WS=5
    INT=6
    ADD_ASSIGN=7
    ASSIGN=8
    DIVIDE_ASSIGN=9
    MOD_ASSIGN=10
    MULTIPLY_ASSIGN=11
    POWER_ASSIGN=12
    EQ=13
    LE=14
    LT=15
    ME=16
    MT=17
    ADD=18
    DIVIDE=19
    MOD=20
    MULTIPLY=21
    POWER=22
    SUBSTRACT=23

    def __init__(self, input:TokenStream, output:TextIO = sys.stdout):
        super().__init__(input, output)
        self.checkVersion("4.9.3")
        self._interp = ParserATNSimulator(self, self.atn, self.decisionsToDFA, self.sharedContextCache)
        self._predicates = None




    class ProgramContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def expression(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(marzoParser.ExpressionContext)
            else:
                return self.getTypedRuleContext(marzoParser.ExpressionContext,i)


        def statement(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(marzoParser.StatementContext)
            else:
                return self.getTypedRuleContext(marzoParser.StatementContext,i)


        def getRuleIndex(self):
            return marzoParser.RULE_program

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterProgram" ):
                listener.enterProgram(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitProgram" ):
                listener.exitProgram(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitProgram" ):
                return visitor.visitProgram(self)
            else:
                return visitor.visitChildren(self)




    def program(self):

        localctx = marzoParser.ProgramContext(self, self._ctx, self.state)
        self.enterRule(localctx, 0, self.RULE_program)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 8 
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while True:
                self.state = 8
                self._errHandler.sync(self)
                la_ = self._interp.adaptivePredict(self._input,0,self._ctx)
                if la_ == 1:
                    self.state = 6
                    self.expression(0)
                    pass

                elif la_ == 2:
                    self.state = 7
                    self.statement()
                    pass


                self.state = 10 
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if not ((((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << marzoParser.T__0) | (1 << marzoParser.T__2) | (1 << marzoParser.VAR) | (1 << marzoParser.INT))) != 0)):
                    break

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ExpressionContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser


        def getRuleIndex(self):
            return marzoParser.RULE_expression

     
        def copyFrom(self, ctx:ParserRuleContext):
            super().copyFrom(ctx)


    class MoreContext(ExpressionContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a marzoParser.ExpressionContext
            super().__init__(parser)
            self.comparator = None # Token
            self.copyFrom(ctx)

        def expression(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(marzoParser.ExpressionContext)
            else:
                return self.getTypedRuleContext(marzoParser.ExpressionContext,i)

        def MT(self):
            return self.getToken(marzoParser.MT, 0)

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterMore" ):
                listener.enterMore(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitMore" ):
                listener.exitMore(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitMore" ):
                return visitor.visitMore(self)
            else:
                return visitor.visitChildren(self)


    class ModuleContext(ExpressionContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a marzoParser.ExpressionContext
            super().__init__(parser)
            self.operator = None # Token
            self.copyFrom(ctx)

        def expression(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(marzoParser.ExpressionContext)
            else:
                return self.getTypedRuleContext(marzoParser.ExpressionContext,i)

        def MOD(self):
            return self.getToken(marzoParser.MOD, 0)

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterModule" ):
                listener.enterModule(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitModule" ):
                listener.exitModule(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitModule" ):
                return visitor.visitModule(self)
            else:
                return visitor.visitChildren(self)


    class IntegerContext(ExpressionContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a marzoParser.ExpressionContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def INT(self):
            return self.getToken(marzoParser.INT, 0)

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterInteger" ):
                listener.enterInteger(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitInteger" ):
                listener.exitInteger(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitInteger" ):
                return visitor.visitInteger(self)
            else:
                return visitor.visitChildren(self)


    class LessContext(ExpressionContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a marzoParser.ExpressionContext
            super().__init__(parser)
            self.comparator = None # Token
            self.copyFrom(ctx)

        def expression(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(marzoParser.ExpressionContext)
            else:
                return self.getTypedRuleContext(marzoParser.ExpressionContext,i)

        def LT(self):
            return self.getToken(marzoParser.LT, 0)

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterLess" ):
                listener.enterLess(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitLess" ):
                listener.exitLess(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitLess" ):
                return visitor.visitLess(self)
            else:
                return visitor.visitChildren(self)


    class SubstractionContext(ExpressionContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a marzoParser.ExpressionContext
            super().__init__(parser)
            self.operator = None # Token
            self.copyFrom(ctx)

        def expression(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(marzoParser.ExpressionContext)
            else:
                return self.getTypedRuleContext(marzoParser.ExpressionContext,i)

        def SUBSTRACT(self):
            return self.getToken(marzoParser.SUBSTRACT, 0)

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterSubstraction" ):
                listener.enterSubstraction(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitSubstraction" ):
                listener.exitSubstraction(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitSubstraction" ):
                return visitor.visitSubstraction(self)
            else:
                return visitor.visitChildren(self)


    class ParenthesisContext(ExpressionContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a marzoParser.ExpressionContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def expression(self):
            return self.getTypedRuleContext(marzoParser.ExpressionContext,0)


        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterParenthesis" ):
                listener.enterParenthesis(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitParenthesis" ):
                listener.exitParenthesis(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitParenthesis" ):
                return visitor.visitParenthesis(self)
            else:
                return visitor.visitChildren(self)


    class EqualContext(ExpressionContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a marzoParser.ExpressionContext
            super().__init__(parser)
            self.comparator = None # Token
            self.copyFrom(ctx)

        def expression(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(marzoParser.ExpressionContext)
            else:
                return self.getTypedRuleContext(marzoParser.ExpressionContext,i)

        def EQ(self):
            return self.getToken(marzoParser.EQ, 0)

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterEqual" ):
                listener.enterEqual(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitEqual" ):
                listener.exitEqual(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitEqual" ):
                return visitor.visitEqual(self)
            else:
                return visitor.visitChildren(self)


    class DivisionContext(ExpressionContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a marzoParser.ExpressionContext
            super().__init__(parser)
            self.operator = None # Token
            self.copyFrom(ctx)

        def expression(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(marzoParser.ExpressionContext)
            else:
                return self.getTypedRuleContext(marzoParser.ExpressionContext,i)

        def DIVIDE(self):
            return self.getToken(marzoParser.DIVIDE, 0)

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterDivision" ):
                listener.enterDivision(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitDivision" ):
                listener.exitDivision(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitDivision" ):
                return visitor.visitDivision(self)
            else:
                return visitor.visitChildren(self)


    class MoreequalContext(ExpressionContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a marzoParser.ExpressionContext
            super().__init__(parser)
            self.comparator = None # Token
            self.copyFrom(ctx)

        def expression(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(marzoParser.ExpressionContext)
            else:
                return self.getTypedRuleContext(marzoParser.ExpressionContext,i)

        def ME(self):
            return self.getToken(marzoParser.ME, 0)

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterMoreequal" ):
                listener.enterMoreequal(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitMoreequal" ):
                listener.exitMoreequal(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitMoreequal" ):
                return visitor.visitMoreequal(self)
            else:
                return visitor.visitChildren(self)


    class VariableContext(ExpressionContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a marzoParser.ExpressionContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def VAR(self):
            return self.getToken(marzoParser.VAR, 0)

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterVariable" ):
                listener.enterVariable(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitVariable" ):
                listener.exitVariable(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitVariable" ):
                return visitor.visitVariable(self)
            else:
                return visitor.visitChildren(self)


    class LessequalContext(ExpressionContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a marzoParser.ExpressionContext
            super().__init__(parser)
            self.comparator = None # Token
            self.copyFrom(ctx)

        def expression(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(marzoParser.ExpressionContext)
            else:
                return self.getTypedRuleContext(marzoParser.ExpressionContext,i)

        def LE(self):
            return self.getToken(marzoParser.LE, 0)

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterLessequal" ):
                listener.enterLessequal(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitLessequal" ):
                listener.exitLessequal(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitLessequal" ):
                return visitor.visitLessequal(self)
            else:
                return visitor.visitChildren(self)


    class MultiplicationContext(ExpressionContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a marzoParser.ExpressionContext
            super().__init__(parser)
            self.operator = None # Token
            self.copyFrom(ctx)

        def expression(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(marzoParser.ExpressionContext)
            else:
                return self.getTypedRuleContext(marzoParser.ExpressionContext,i)

        def MULTIPLY(self):
            return self.getToken(marzoParser.MULTIPLY, 0)

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterMultiplication" ):
                listener.enterMultiplication(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitMultiplication" ):
                listener.exitMultiplication(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitMultiplication" ):
                return visitor.visitMultiplication(self)
            else:
                return visitor.visitChildren(self)


    class AdditionContext(ExpressionContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a marzoParser.ExpressionContext
            super().__init__(parser)
            self.operator = None # Token
            self.copyFrom(ctx)

        def expression(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(marzoParser.ExpressionContext)
            else:
                return self.getTypedRuleContext(marzoParser.ExpressionContext,i)

        def ADD(self):
            return self.getToken(marzoParser.ADD, 0)

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterAddition" ):
                listener.enterAddition(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitAddition" ):
                listener.exitAddition(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitAddition" ):
                return visitor.visitAddition(self)
            else:
                return visitor.visitChildren(self)



    def expression(self, _p:int=0):
        _parentctx = self._ctx
        _parentState = self.state
        localctx = marzoParser.ExpressionContext(self, self._ctx, _parentState)
        _prevctx = localctx
        _startState = 2
        self.enterRecursionRule(localctx, 2, self.RULE_expression, _p)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 19
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [marzoParser.T__0]:
                localctx = marzoParser.ParenthesisContext(self, localctx)
                self._ctx = localctx
                _prevctx = localctx

                self.state = 13
                self.match(marzoParser.T__0)
                self.state = 14
                self.expression(0)
                self.state = 15
                self.match(marzoParser.T__1)
                pass
            elif token in [marzoParser.INT]:
                localctx = marzoParser.IntegerContext(self, localctx)
                self._ctx = localctx
                _prevctx = localctx
                self.state = 17
                self.match(marzoParser.INT)
                pass
            elif token in [marzoParser.VAR]:
                localctx = marzoParser.VariableContext(self, localctx)
                self._ctx = localctx
                _prevctx = localctx
                self.state = 18
                self.match(marzoParser.VAR)
                pass
            else:
                raise NoViableAltException(self)

            self._ctx.stop = self._input.LT(-1)
            self.state = 53
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,4,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    self.state = 51
                    self._errHandler.sync(self)
                    la_ = self._interp.adaptivePredict(self._input,3,self._ctx)
                    if la_ == 1:
                        localctx = marzoParser.EqualContext(self, marzoParser.ExpressionContext(self, _parentctx, _parentState))
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_expression)
                        self.state = 21
                        if not self.precpred(self._ctx, 13):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 13)")
                        self.state = 22
                        localctx.comparator = self.match(marzoParser.EQ)
                        self.state = 23
                        self.expression(14)
                        pass

                    elif la_ == 2:
                        localctx = marzoParser.LessequalContext(self, marzoParser.ExpressionContext(self, _parentctx, _parentState))
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_expression)
                        self.state = 24
                        if not self.precpred(self._ctx, 12):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 12)")
                        self.state = 25
                        localctx.comparator = self.match(marzoParser.LE)
                        self.state = 26
                        self.expression(13)
                        pass

                    elif la_ == 3:
                        localctx = marzoParser.LessContext(self, marzoParser.ExpressionContext(self, _parentctx, _parentState))
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_expression)
                        self.state = 27
                        if not self.precpred(self._ctx, 11):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 11)")
                        self.state = 28
                        localctx.comparator = self.match(marzoParser.LT)
                        self.state = 29
                        self.expression(12)
                        pass

                    elif la_ == 4:
                        localctx = marzoParser.MoreequalContext(self, marzoParser.ExpressionContext(self, _parentctx, _parentState))
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_expression)
                        self.state = 30
                        if not self.precpred(self._ctx, 10):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 10)")
                        self.state = 31
                        localctx.comparator = self.match(marzoParser.ME)
                        self.state = 32
                        self.expression(11)
                        pass

                    elif la_ == 5:
                        localctx = marzoParser.MoreContext(self, marzoParser.ExpressionContext(self, _parentctx, _parentState))
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_expression)
                        self.state = 33
                        if not self.precpred(self._ctx, 9):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 9)")
                        self.state = 34
                        localctx.comparator = self.match(marzoParser.MT)
                        self.state = 35
                        self.expression(10)
                        pass

                    elif la_ == 6:
                        localctx = marzoParser.AdditionContext(self, marzoParser.ExpressionContext(self, _parentctx, _parentState))
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_expression)
                        self.state = 36
                        if not self.precpred(self._ctx, 8):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 8)")
                        self.state = 37
                        localctx.operator = self.match(marzoParser.ADD)
                        self.state = 38
                        self.expression(9)
                        pass

                    elif la_ == 7:
                        localctx = marzoParser.DivisionContext(self, marzoParser.ExpressionContext(self, _parentctx, _parentState))
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_expression)
                        self.state = 39
                        if not self.precpred(self._ctx, 7):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 7)")
                        self.state = 40
                        localctx.operator = self.match(marzoParser.DIVIDE)
                        self.state = 41
                        self.expression(8)
                        pass

                    elif la_ == 8:
                        localctx = marzoParser.ModuleContext(self, marzoParser.ExpressionContext(self, _parentctx, _parentState))
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_expression)
                        self.state = 42
                        if not self.precpred(self._ctx, 6):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 6)")
                        self.state = 43
                        localctx.operator = self.match(marzoParser.MOD)
                        self.state = 44
                        self.expression(7)
                        pass

                    elif la_ == 9:
                        localctx = marzoParser.MultiplicationContext(self, marzoParser.ExpressionContext(self, _parentctx, _parentState))
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_expression)
                        self.state = 45
                        if not self.precpred(self._ctx, 5):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 5)")
                        self.state = 46
                        localctx.operator = self.match(marzoParser.MULTIPLY)
                        self.state = 47
                        self.expression(6)
                        pass

                    elif la_ == 10:
                        localctx = marzoParser.SubstractionContext(self, marzoParser.ExpressionContext(self, _parentctx, _parentState))
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_expression)
                        self.state = 48
                        if not self.precpred(self._ctx, 4):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 4)")
                        self.state = 49
                        localctx.operator = self.match(marzoParser.SUBSTRACT)
                        self.state = 50
                        self.expression(5)
                        pass

             
                self.state = 55
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,4,self._ctx)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.unrollRecursionContexts(_parentctx)
        return localctx


    class StatementContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser


        def getRuleIndex(self):
            return marzoParser.RULE_statement

     
        def copyFrom(self, ctx:ParserRuleContext):
            super().copyFrom(ctx)



    class Multiply_assignContext(StatementContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a marzoParser.StatementContext
            super().__init__(parser)
            self.assigner = None # Token
            self.copyFrom(ctx)

        def VAR(self):
            return self.getToken(marzoParser.VAR, 0)
        def expression(self):
            return self.getTypedRuleContext(marzoParser.ExpressionContext,0)

        def MULTIPLY_ASSIGN(self):
            return self.getToken(marzoParser.MULTIPLY_ASSIGN, 0)
        def POWER_ASSIGN(self):
            return self.getToken(marzoParser.POWER_ASSIGN, 0)

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterMultiply_assign" ):
                listener.enterMultiply_assign(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitMultiply_assign" ):
                listener.exitMultiply_assign(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitMultiply_assign" ):
                return visitor.visitMultiply_assign(self)
            else:
                return visitor.visitChildren(self)


    class Divide_assignContext(StatementContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a marzoParser.StatementContext
            super().__init__(parser)
            self.assigner = None # Token
            self.copyFrom(ctx)

        def VAR(self):
            return self.getToken(marzoParser.VAR, 0)
        def expression(self):
            return self.getTypedRuleContext(marzoParser.ExpressionContext,0)

        def DIVIDE_ASSIGN(self):
            return self.getToken(marzoParser.DIVIDE_ASSIGN, 0)

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterDivide_assign" ):
                listener.enterDivide_assign(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitDivide_assign" ):
                listener.exitDivide_assign(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitDivide_assign" ):
                return visitor.visitDivide_assign(self)
            else:
                return visitor.visitChildren(self)


    class Add_assignContext(StatementContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a marzoParser.StatementContext
            super().__init__(parser)
            self.assigner = None # Token
            self.copyFrom(ctx)

        def VAR(self):
            return self.getToken(marzoParser.VAR, 0)
        def expression(self):
            return self.getTypedRuleContext(marzoParser.ExpressionContext,0)

        def ADD_ASSIGN(self):
            return self.getToken(marzoParser.ADD_ASSIGN, 0)

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterAdd_assign" ):
                listener.enterAdd_assign(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitAdd_assign" ):
                listener.exitAdd_assign(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitAdd_assign" ):
                return visitor.visitAdd_assign(self)
            else:
                return visitor.visitChildren(self)


    class Mod_assignContext(StatementContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a marzoParser.StatementContext
            super().__init__(parser)
            self.assigner = None # Token
            self.copyFrom(ctx)

        def VAR(self):
            return self.getToken(marzoParser.VAR, 0)
        def expression(self):
            return self.getTypedRuleContext(marzoParser.ExpressionContext,0)

        def MOD_ASSIGN(self):
            return self.getToken(marzoParser.MOD_ASSIGN, 0)

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterMod_assign" ):
                listener.enterMod_assign(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitMod_assign" ):
                listener.exitMod_assign(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitMod_assign" ):
                return visitor.visitMod_assign(self)
            else:
                return visitor.visitChildren(self)


    class Declare_intContext(StatementContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a marzoParser.StatementContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def VAR(self):
            return self.getToken(marzoParser.VAR, 0)

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterDeclare_int" ):
                listener.enterDeclare_int(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitDeclare_int" ):
                listener.exitDeclare_int(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitDeclare_int" ):
                return visitor.visitDeclare_int(self)
            else:
                return visitor.visitChildren(self)


    class AssignContext(StatementContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a marzoParser.StatementContext
            super().__init__(parser)
            self.assigner = None # Token
            self.copyFrom(ctx)

        def VAR(self):
            return self.getToken(marzoParser.VAR, 0)
        def expression(self):
            return self.getTypedRuleContext(marzoParser.ExpressionContext,0)

        def ASSIGN(self):
            return self.getToken(marzoParser.ASSIGN, 0)

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterAssign" ):
                listener.enterAssign(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitAssign" ):
                listener.exitAssign(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitAssign" ):
                return visitor.visitAssign(self)
            else:
                return visitor.visitChildren(self)



    def statement(self):

        localctx = marzoParser.StatementContext(self, self._ctx, self.state)
        self.enterRule(localctx, 4, self.RULE_statement)
        try:
            self.state = 76
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,5,self._ctx)
            if la_ == 1:
                localctx = marzoParser.AssignContext(self, localctx)
                self.enterOuterAlt(localctx, 1)
                self.state = 56
                self.match(marzoParser.VAR)
                self.state = 57
                localctx.assigner = self.match(marzoParser.ASSIGN)
                self.state = 58
                self.expression(0)
                pass

            elif la_ == 2:
                localctx = marzoParser.Add_assignContext(self, localctx)
                self.enterOuterAlt(localctx, 2)
                self.state = 59
                self.match(marzoParser.VAR)
                self.state = 60
                localctx.assigner = self.match(marzoParser.ADD_ASSIGN)
                self.state = 61
                self.expression(0)
                pass

            elif la_ == 3:
                localctx = marzoParser.Divide_assignContext(self, localctx)
                self.enterOuterAlt(localctx, 3)
                self.state = 62
                self.match(marzoParser.VAR)
                self.state = 63
                localctx.assigner = self.match(marzoParser.DIVIDE_ASSIGN)
                self.state = 64
                self.expression(0)
                pass

            elif la_ == 4:
                localctx = marzoParser.Mod_assignContext(self, localctx)
                self.enterOuterAlt(localctx, 4)
                self.state = 65
                self.match(marzoParser.VAR)
                self.state = 66
                localctx.assigner = self.match(marzoParser.MOD_ASSIGN)
                self.state = 67
                self.expression(0)
                pass

            elif la_ == 5:
                localctx = marzoParser.Multiply_assignContext(self, localctx)
                self.enterOuterAlt(localctx, 5)
                self.state = 68
                self.match(marzoParser.VAR)
                self.state = 69
                localctx.assigner = self.match(marzoParser.MULTIPLY_ASSIGN)
                self.state = 70
                self.expression(0)
                pass

            elif la_ == 6:
                localctx = marzoParser.Multiply_assignContext(self, localctx)
                self.enterOuterAlt(localctx, 6)
                self.state = 71
                self.match(marzoParser.VAR)
                self.state = 72
                localctx.assigner = self.match(marzoParser.POWER_ASSIGN)
                self.state = 73
                self.expression(0)
                pass

            elif la_ == 7:
                localctx = marzoParser.Declare_intContext(self, localctx)
                self.enterOuterAlt(localctx, 7)
                self.state = 74
                self.match(marzoParser.T__2)
                self.state = 75
                self.match(marzoParser.VAR)
                pass


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
        self._predicates[1] = self.expression_sempred
        pred = self._predicates.get(ruleIndex, None)
        if pred is None:
            raise Exception("No predicate with index:" + str(ruleIndex))
        else:
            return pred(localctx, predIndex)

    def expression_sempred(self, localctx:ExpressionContext, predIndex:int):
            if predIndex == 0:
                return self.precpred(self._ctx, 13)
         

            if predIndex == 1:
                return self.precpred(self._ctx, 12)
         

            if predIndex == 2:
                return self.precpred(self._ctx, 11)
         

            if predIndex == 3:
                return self.precpred(self._ctx, 10)
         

            if predIndex == 4:
                return self.precpred(self._ctx, 9)
         

            if predIndex == 5:
                return self.precpred(self._ctx, 8)
         

            if predIndex == 6:
                return self.precpred(self._ctx, 7)
         

            if predIndex == 7:
                return self.precpred(self._ctx, 6)
         

            if predIndex == 8:
                return self.precpred(self._ctx, 5)
         

            if predIndex == 9:
                return self.precpred(self._ctx, 4)
         




