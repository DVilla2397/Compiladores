# Generated from c:\Users\villa\Documents\Compiladores\antlr\marzo.g4 by ANTLR 4.9.3
from antlr4 import *
from io import StringIO
import sys
if sys.version_info[1] > 5:
    from typing import TextIO
else:
    from typing.io import TextIO



def serializedATN():
    with StringIO() as buf:
        buf.write("\3\u608b\ua72a\u8133\ub9ed\u417c\u3be7\u7786\u5964\2\24")
        buf.write("Y\b\1\4\2\t\2\4\3\t\3\4\4\t\4\4\5\t\5\4\6\t\6\4\7\t\7")
        buf.write("\4\b\t\b\4\t\t\t\4\n\t\n\4\13\t\13\4\f\t\f\4\r\t\r\4\16")
        buf.write("\t\16\4\17\t\17\4\20\t\20\4\21\t\21\4\22\t\22\4\23\t\23")
        buf.write("\3\2\3\2\3\3\3\3\3\4\3\4\3\4\3\4\3\5\3\5\6\5\62\n\5\r")
        buf.write("\5\16\5\63\3\6\6\6\67\n\6\r\6\16\68\3\7\3\7\3\7\3\b\3")
        buf.write("\b\3\t\3\t\3\n\3\n\3\13\3\13\3\f\3\f\3\r\3\r\3\16\3\16")
        buf.write("\3\17\3\17\3\20\3\20\3\20\3\21\3\21\3\21\3\22\3\22\3\22")
        buf.write("\3\23\3\23\3\23\2\2\24\3\3\5\4\7\5\t\6\13\7\r\b\17\t\21")
        buf.write("\n\23\13\25\f\27\r\31\16\33\17\35\20\37\21!\22#\23%\24")
        buf.write("\3\2\5\4\2aac|\4\2\62;C|\3\2\62;\2Z\2\3\3\2\2\2\2\5\3")
        buf.write("\2\2\2\2\7\3\2\2\2\2\t\3\2\2\2\2\13\3\2\2\2\2\r\3\2\2")
        buf.write("\2\2\17\3\2\2\2\2\21\3\2\2\2\2\23\3\2\2\2\2\25\3\2\2\2")
        buf.write("\2\27\3\2\2\2\2\31\3\2\2\2\2\33\3\2\2\2\2\35\3\2\2\2\2")
        buf.write("\37\3\2\2\2\2!\3\2\2\2\2#\3\2\2\2\2%\3\2\2\2\3\'\3\2\2")
        buf.write("\2\5)\3\2\2\2\7+\3\2\2\2\t/\3\2\2\2\13\66\3\2\2\2\r:\3")
        buf.write("\2\2\2\17=\3\2\2\2\21?\3\2\2\2\23A\3\2\2\2\25C\3\2\2\2")
        buf.write("\27E\3\2\2\2\31G\3\2\2\2\33I\3\2\2\2\35K\3\2\2\2\37M\3")
        buf.write("\2\2\2!P\3\2\2\2#S\3\2\2\2%V\3\2\2\2\'(\7*\2\2(\4\3\2")
        buf.write("\2\2)*\7+\2\2*\6\3\2\2\2+,\7k\2\2,-\7p\2\2-.\7v\2\2.\b")
        buf.write("\3\2\2\2/\61\t\2\2\2\60\62\t\3\2\2\61\60\3\2\2\2\62\63")
        buf.write("\3\2\2\2\63\61\3\2\2\2\63\64\3\2\2\2\64\n\3\2\2\2\65\67")
        buf.write("\t\4\2\2\66\65\3\2\2\2\678\3\2\2\28\66\3\2\2\289\3\2\2")
        buf.write("\29\f\3\2\2\2:;\7?\2\2;<\7?\2\2<\16\3\2\2\2=>\7@\2\2>")
        buf.write("\20\3\2\2\2?@\7>\2\2@\22\3\2\2\2AB\7-\2\2B\24\3\2\2\2")
        buf.write("CD\7,\2\2D\26\3\2\2\2EF\7/\2\2F\30\3\2\2\2GH\7\61\2\2")
        buf.write("H\32\3\2\2\2IJ\7\'\2\2J\34\3\2\2\2KL\7?\2\2L\36\3\2\2")
        buf.write("\2MN\7-\2\2NO\7?\2\2O \3\2\2\2PQ\7\61\2\2QR\7?\2\2R\"")
        buf.write("\3\2\2\2ST\7\'\2\2TU\7?\2\2U$\3\2\2\2VW\7,\2\2WX\7?\2")
        buf.write("\2X&\3\2\2\2\5\2\638\2")
        return buf.getvalue()


class marzoLexer(Lexer):

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    T__0 = 1
    T__1 = 2
    T__2 = 3
    VAR = 4
    INT = 5
    IGUAL = 6
    MAYOR = 7
    MENOR = 8
    SUMAR = 9
    MULTIPLICAR = 10
    RESTAR = 11
    DIVIDIR = 12
    PORCENTAJE = 13
    AS = 14
    SUMAR_AS = 15
    DIVIDIR_AS = 16
    MODULO_AS = 17
    MULTIPLICAR_AS = 18

    channelNames = [ u"DEFAULT_TOKEN_CHANNEL", u"HIDDEN" ]

    modeNames = [ "DEFAULT_MODE" ]

    literalNames = [ "<INVALID>",
            "'('", "')'", "'int'", "'=='", "'>'", "'<'", "'+'", "'*'", "'-'", 
            "'/'", "'%'", "'='", "'+='", "'/='", "'%='", "'*='" ]

    symbolicNames = [ "<INVALID>",
            "VAR", "INT", "IGUAL", "MAYOR", "MENOR", "SUMAR", "MULTIPLICAR", 
            "RESTAR", "DIVIDIR", "PORCENTAJE", "AS", "SUMAR_AS", "DIVIDIR_AS", 
            "MODULO_AS", "MULTIPLICAR_AS" ]

    ruleNames = [ "T__0", "T__1", "T__2", "VAR", "INT", "IGUAL", "MAYOR", 
                  "MENOR", "SUMAR", "MULTIPLICAR", "RESTAR", "DIVIDIR", 
                  "PORCENTAJE", "AS", "SUMAR_AS", "DIVIDIR_AS", "MODULO_AS", 
                  "MULTIPLICAR_AS" ]

    grammarFileName = "marzo.g4"

    def __init__(self, input=None, output:TextIO = sys.stdout):
        super().__init__(input, output)
        self.checkVersion("4.9.3")
        self._interp = LexerATNSimulator(self, self.atn, self.decisionsToDFA, PredictionContextCache())
        self._actions = None
        self._predicates = None


