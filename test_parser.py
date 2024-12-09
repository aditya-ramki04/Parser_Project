from antlr4 import *
from anytree import Node, RenderTree
from IndentationHandler import IndentationLexer, TokenType
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

def safe_get_token_type(lexer, token):
    """Safely get token type name"""
    try:
        if token.type >= 0 and token.type < len(lexer.symbolicNames):
            return lexer.symbolicNames[token.type]
        return f"<Unknown:{token.type}>"
    except Exception:
        return f"<Error:{token.type}>"

def process_indentation(code: str) -> str:
    """Process the code through the indentation lexer and convert to ANTLR-compatible format"""
    indent_lexer = IndentationLexer(code)
    tokens = indent_lexer.tokenize()
    
    processed_lines = []
    
    for token in tokens:
        if token.type == TokenType.INDENT:
            processed_lines.append('INDENT ')  # Use INDENT token instead of \t
        elif token.type == TokenType.DEDENT:
            processed_lines.append('DEDENT ')  # Space after DEDENT for separation
        elif token.type == TokenType.NEWLINE:
            processed_lines.append('\n')
        elif token.type == TokenType.OTHER:
            content = token.value.rstrip('\n')
            if content.startswith(('#', "'''")):
                # Handle comments
                processed_lines.append(f"{content}\n")
            else:
                # Regular code without tabs
                processed_lines.append(f"{content}\n")
    
    # Join all tokens
    result = ''.join(processed_lines)
    
    # Clean up the result
    result = result.replace('\n\n\n', '\n\n')  # Remove extra newlines
    result = result.replace('DEDENT DEDENT', 'DEDENT\nDEDENT')  # Separate multiple DEDENTs
    result = result.replace('INDENT\nINDENT', 'INDENT INDENT')  # Handle multiple INDENTs
    
    # Ensure proper spacing around control structures
    result = result.replace(':\nINDENT', ':\n INDENT')  # Space after colon
    result = result.replace('DEDENT\nelse', 'DEDENT\n else')  # Space before else
    result = result.replace('DEDENT\nelif', 'DEDENT\n elif')  # Space before elif
    
    print("Processed code:")
    print(result)
    return result
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
# Deliverable 1
arith_op4 = 4.2 * 10
arith_op5 = arith_op1

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

assign1 = ""

# Deliverable 2

if var1 > var2:
	arith_op1 = 1 + 2
	assign1 = "text data"

if var1 <= var2 and var3 == var4:
	arith_op1 = 1 + 2
	assign1 = "text data"
else:
	arith_op4 = 4.2 * 10
	arith_op3 *= arith_op4
	
data = 0

if var1 != var2 or var3 >= var4:
	flag = True
elif (not flag) and var3 > 10:
	flag = False
else:
	data = -1

# Deliverable 3

## comment test 1

''' 
	comment test 2
	adding more comments
	and more...
'''

while data > 0 or data != 0:
	data = data - 1
	if True:
		a = "This is the weirdest code I have ever written"

for data in array1:
	if data < 0:
		while(data != 0):
			b = "This code doesn't make any sense"
			data = data + 1
	elif data > 0:
		while(data != 0):
			c = "I feel like I have no purpose..."
			data = data - 1

for i in range(0,5):
	data = data * 2
	data = data - 1

''' I need help, this code shouldn't even exist '''
while True:
	data = 30
	data = data - 1
    """


    try:
        # Preprocess the code
        processed_code = process_indentation(code)
        
        # Setup ANTLR pipeline
        input_stream = InputStream(processed_code)
        lexer = PythonSubsetLexer(input_stream)
        
        # Debug: Print all tokens safely
        print("\nTokens:")
        tokens = list(lexer.getAllTokens())
        for token in tokens:
            token_type = safe_get_token_type(lexer, token)
            line_num = token.line
            col_num = token.column
        
        # Reset lexer for parsing
        lexer.reset()
        token_stream = CommonTokenStream(lexer)
        parser = PythonSubsetParser(token_stream)
        
        # Parse and build tree
        tree = parser.program()
        root = build_tree(tree)
        
        print("\nParse tree:")
        for pre, fill, node in RenderTree(root):
            print(f"{pre}{node.name}")
            
    except Exception as e:
        print(f"Error during parsing: {str(e)}")
        import traceback
        traceback.print_exc()

if __name__ == "__main__":
    main()
