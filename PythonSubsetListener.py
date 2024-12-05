# Generated from PythonSubset.g4 by ANTLR 4.13.1
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


    # Enter a parse tree produced by PythonSubsetParser#simpleStatement.
    def enterSimpleStatement(self, ctx:PythonSubsetParser.SimpleStatementContext):
        pass

    # Exit a parse tree produced by PythonSubsetParser#simpleStatement.
    def exitSimpleStatement(self, ctx:PythonSubsetParser.SimpleStatementContext):
        pass


    # Enter a parse tree produced by PythonSubsetParser#compoundStatement.
    def enterCompoundStatement(self, ctx:PythonSubsetParser.CompoundStatementContext):
        pass

    # Exit a parse tree produced by PythonSubsetParser#compoundStatement.
    def exitCompoundStatement(self, ctx:PythonSubsetParser.CompoundStatementContext):
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


    # Enter a parse tree produced by PythonSubsetParser#whileStatement.
    def enterWhileStatement(self, ctx:PythonSubsetParser.WhileStatementContext):
        pass

    # Exit a parse tree produced by PythonSubsetParser#whileStatement.
    def exitWhileStatement(self, ctx:PythonSubsetParser.WhileStatementContext):
        pass


    # Enter a parse tree produced by PythonSubsetParser#forStatement.
    def enterForStatement(self, ctx:PythonSubsetParser.ForStatementContext):
        pass

    # Exit a parse tree produced by PythonSubsetParser#forStatement.
    def exitForStatement(self, ctx:PythonSubsetParser.ForStatementContext):
        pass


    # Enter a parse tree produced by PythonSubsetParser#suite.
    def enterSuite(self, ctx:PythonSubsetParser.SuiteContext):
        pass

    # Exit a parse tree produced by PythonSubsetParser#suite.
    def exitSuite(self, ctx:PythonSubsetParser.SuiteContext):
        pass


    # Enter a parse tree produced by PythonSubsetParser#condition.
    def enterCondition(self, ctx:PythonSubsetParser.ConditionContext):
        pass

    # Exit a parse tree produced by PythonSubsetParser#condition.
    def exitCondition(self, ctx:PythonSubsetParser.ConditionContext):
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