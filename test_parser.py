from antlr4 import *
from anytree import Node, RenderTree
from PythonSubsetLexer import PythonSubsetLexer
from PythonSubsetParser import PythonSubsetParser


# Recursive function to build the tree using anytree
def build_tree(node, parent=None):
    # Create a new anytree Node for the current parse tree node
    tree_node = Node(node.getText() if node.getChildCount() == 0 else PythonSubsetParser.ruleNames[node.getRuleIndex()],
                     parent=parent)

    # Recursively add children
    for i in range(node.getChildCount()):
        build_tree(node.getChild(i), tree_node)

    return tree_node


def main():
    # Sample input code
    code = """
    assign1 = "20"
    assign2 = 123
    assign3 = 1.23
    assign4 = assign1
    arith_op1 = 1 + 2
    arith_op2 = 13 - 3
    arith_op3 = 10 / arith_op1
    arith_op4 = 4.2 * 10
    arith_op5 = arith_op1 % arith_op2
    arith_op1 += arith_op2
    arith_op2 -= arith_op3
    arith_op3 *= arith_op4
    arith_op4 /= arith_op5
    array1 = [1, 2, 3, 4, 5]
    array2 = ['a', 'b', 'c']
    array3 = [1.6, 2.7, 3.8, 4.9, 5.0]
    var1 = 10
    var2 = var1/2 + 5
    var3 = var2 % 2
    var4 = 1
    flag = True
    """

    # Setup ANTLR lexer and parser
    input_stream = InputStream(code)
    lexer = PythonSubsetLexer(input_stream)
    token_stream = CommonTokenStream(lexer)
    parser = PythonSubsetParser(token_stream)

    # Parse the input starting from the 'program' rule
    tree = parser.program()

    # Build the tree structure using anytree
    root = build_tree(tree)

    # Print the tree
    for pre, fill, node in RenderTree(root):
        print(f"{pre}{node.name}")


if __name__ == "__main__":
    main()
