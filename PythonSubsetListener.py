# Generated from PythonSubset.g4 by ANTLR 4.13.2
from antlr4 import *
if "." in __name__:
    from .PythonSubsetParser import PythonSubsetParser
else:
    from PythonSubsetParser import PythonSubsetParser

# This class defines a complete listener for a parse tree produced by PythonSubsetParser.
class PythonSubsetListener(ParseTreeListener):

    # Enter a parse tree produced by PythonSubsetParser#program.
    def enterProgram(self, ctx:PythonSubsetParser.ProgramContext):
        pass

    # Exit a parse tree produced by PythonSubsetParser#program.
    def exitProgram(self, ctx:PythonSubsetParser.ProgramContext):
        pass


    # Enter a parse tree produced by PythonSubsetParser#statement.
    def enterStatement(self, ctx:PythonSubsetParser.StatementContext):
        pass

    # Exit a parse tree produced by PythonSubsetParser#statement.
    def exitStatement(self, ctx:PythonSubsetParser.StatementContext):
        pass


    # Enter a parse tree produced by PythonSubsetParser#assignment.
    def enterAssignment(self, ctx:PythonSubsetParser.AssignmentContext):
        pass

    # Exit a parse tree produced by PythonSubsetParser#assignment.
    def exitAssignment(self, ctx:PythonSubsetParser.AssignmentContext):
        pass


    # Enter a parse tree produced by PythonSubsetParser#ifStatement.
    def enterIfStatement(self, ctx:PythonSubsetParser.IfStatementContext):
        pass

    # Exit a parse tree produced by PythonSubsetParser#ifStatement.
    def exitIfStatement(self, ctx:PythonSubsetParser.IfStatementContext):
        pass


    # Enter a parse tree produced by PythonSubsetParser#expr.
    def enterExpr(self, ctx:PythonSubsetParser.ExprContext):
        pass

    # Exit a parse tree produced by PythonSubsetParser#expr.
    def exitExpr(self, ctx:PythonSubsetParser.ExprContext):
        pass


    # Enter a parse tree produced by PythonSubsetParser#compoundAssign.
    def enterCompoundAssign(self, ctx:PythonSubsetParser.CompoundAssignContext):
        pass

    # Exit a parse tree produced by PythonSubsetParser#compoundAssign.
    def exitCompoundAssign(self, ctx:PythonSubsetParser.CompoundAssignContext):
        pass


    # Enter a parse tree produced by PythonSubsetParser#array.
    def enterArray(self, ctx:PythonSubsetParser.ArrayContext):
        pass

    # Exit a parse tree produced by PythonSubsetParser#array.
    def exitArray(self, ctx:PythonSubsetParser.ArrayContext):
        pass



del PythonSubsetParser