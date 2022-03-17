# Generated from c:\Users\villa\Documents\Compiladores\antlr\marzo.g4 by ANTLR 4.9.3
from antlr4 import *
if __name__ is not None and "." in __name__:
    from .marzoParser import marzoParser
else:
    from marzoParser import marzoParser

# This class defines a complete generic visitor for a parse tree produced by marzoParser.

class marzoVisitor(ParseTreeVisitor):

    # Visit a parse tree produced by marzoParser#program.
    def visitProgram(self, ctx:marzoParser.ProgramContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by marzoParser#more.
    def visitMore(self, ctx:marzoParser.MoreContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by marzoParser#module.
    def visitModule(self, ctx:marzoParser.ModuleContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by marzoParser#integer.
    def visitInteger(self, ctx:marzoParser.IntegerContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by marzoParser#less.
    def visitLess(self, ctx:marzoParser.LessContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by marzoParser#substraction.
    def visitSubstraction(self, ctx:marzoParser.SubstractionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by marzoParser#parenthesis.
    def visitParenthesis(self, ctx:marzoParser.ParenthesisContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by marzoParser#equal.
    def visitEqual(self, ctx:marzoParser.EqualContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by marzoParser#division.
    def visitDivision(self, ctx:marzoParser.DivisionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by marzoParser#moreequal.
    def visitMoreequal(self, ctx:marzoParser.MoreequalContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by marzoParser#variable.
    def visitVariable(self, ctx:marzoParser.VariableContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by marzoParser#lessequal.
    def visitLessequal(self, ctx:marzoParser.LessequalContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by marzoParser#multiplication.
    def visitMultiplication(self, ctx:marzoParser.MultiplicationContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by marzoParser#addition.
    def visitAddition(self, ctx:marzoParser.AdditionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by marzoParser#assign.
    def visitAssign(self, ctx:marzoParser.AssignContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by marzoParser#add_assign.
    def visitAdd_assign(self, ctx:marzoParser.Add_assignContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by marzoParser#divide_assign.
    def visitDivide_assign(self, ctx:marzoParser.Divide_assignContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by marzoParser#mod_assign.
    def visitMod_assign(self, ctx:marzoParser.Mod_assignContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by marzoParser#multiply_assign.
    def visitMultiply_assign(self, ctx:marzoParser.Multiply_assignContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by marzoParser#declare_int.
    def visitDeclare_int(self, ctx:marzoParser.Declare_intContext):
        return self.visitChildren(ctx)



del marzoParser