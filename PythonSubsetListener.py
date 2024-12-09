# Generated from PythonSubset.g4 by ANTLR 4.13.1
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


    # Enter a parse tree produced by PythonSubsetParser#stmt.
    def enterStmt(self, ctx:PythonSubsetParser.StmtContext):
        pass

    # Exit a parse tree produced by PythonSubsetParser#stmt.
    def exitStmt(self, ctx:PythonSubsetParser.StmtContext):
        pass


    # Enter a parse tree produced by PythonSubsetParser#simpleStmt.
    def enterSimpleStmt(self, ctx:PythonSubsetParser.SimpleStmtContext):
        pass

    # Exit a parse tree produced by PythonSubsetParser#simpleStmt.
    def exitSimpleStmt(self, ctx:PythonSubsetParser.SimpleStmtContext):
        pass


    # Enter a parse tree produced by PythonSubsetParser#compoundStmt.
    def enterCompoundStmt(self, ctx:PythonSubsetParser.CompoundStmtContext):
        pass

    # Exit a parse tree produced by PythonSubsetParser#compoundStmt.
    def exitCompoundStmt(self, ctx:PythonSubsetParser.CompoundStmtContext):
        pass


    # Enter a parse tree produced by PythonSubsetParser#if_stmt.
    def enterIf_stmt(self, ctx:PythonSubsetParser.If_stmtContext):
        pass

    # Exit a parse tree produced by PythonSubsetParser#if_stmt.
    def exitIf_stmt(self, ctx:PythonSubsetParser.If_stmtContext):
        pass


    # Enter a parse tree produced by PythonSubsetParser#while_stmt.
    def enterWhile_stmt(self, ctx:PythonSubsetParser.While_stmtContext):
        pass

    # Exit a parse tree produced by PythonSubsetParser#while_stmt.
    def exitWhile_stmt(self, ctx:PythonSubsetParser.While_stmtContext):
        pass


    # Enter a parse tree produced by PythonSubsetParser#for_stmt.
    def enterFor_stmt(self, ctx:PythonSubsetParser.For_stmtContext):
        pass

    # Exit a parse tree produced by PythonSubsetParser#for_stmt.
    def exitFor_stmt(self, ctx:PythonSubsetParser.For_stmtContext):
        pass


    # Enter a parse tree produced by PythonSubsetParser#suite.
    def enterSuite(self, ctx:PythonSubsetParser.SuiteContext):
        pass

    # Exit a parse tree produced by PythonSubsetParser#suite.
    def exitSuite(self, ctx:PythonSubsetParser.SuiteContext):
        pass


    # Enter a parse tree produced by PythonSubsetParser#assignment.
    def enterAssignment(self, ctx:PythonSubsetParser.AssignmentContext):
        pass

    # Exit a parse tree produced by PythonSubsetParser#assignment.
    def exitAssignment(self, ctx:PythonSubsetParser.AssignmentContext):
        pass


    # Enter a parse tree produced by PythonSubsetParser#expr.
    def enterExpr(self, ctx:PythonSubsetParser.ExprContext):
        pass

    # Exit a parse tree produced by PythonSubsetParser#expr.
    def exitExpr(self, ctx:PythonSubsetParser.ExprContext):
        pass


    # Enter a parse tree produced by PythonSubsetParser#atom.
    def enterAtom(self, ctx:PythonSubsetParser.AtomContext):
        pass

    # Exit a parse tree produced by PythonSubsetParser#atom.
    def exitAtom(self, ctx:PythonSubsetParser.AtomContext):
        pass


    # Enter a parse tree produced by PythonSubsetParser#functionCall.
    def enterFunctionCall(self, ctx:PythonSubsetParser.FunctionCallContext):
        pass

    # Exit a parse tree produced by PythonSubsetParser#functionCall.
    def exitFunctionCall(self, ctx:PythonSubsetParser.FunctionCallContext):
        pass


    # Enter a parse tree produced by PythonSubsetParser#array.
    def enterArray(self, ctx:PythonSubsetParser.ArrayContext):
        pass

    # Exit a parse tree produced by PythonSubsetParser#array.
    def exitArray(self, ctx:PythonSubsetParser.ArrayContext):
        pass


    # Enter a parse tree produced by PythonSubsetParser#compoundAssign.
    def enterCompoundAssign(self, ctx:PythonSubsetParser.CompoundAssignContext):
        pass

    # Exit a parse tree produced by PythonSubsetParser#compoundAssign.
    def exitCompoundAssign(self, ctx:PythonSubsetParser.CompoundAssignContext):
        pass



del PythonSubsetParser