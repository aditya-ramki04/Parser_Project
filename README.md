# **Python Parser Project**

## **Project Overview**
This project focuses on developing a parser for a subset of Python 3.x using Context-Free Grammar (CFG) and tools like ANTLR. The parser processes arithmetic operators, assignment operators, conditional statements (if, elif, else), and loops while adhering to Python’s indentation-sensitive syntax. The final output of the parser is a parse tree that clearly shows the hierarchical structure of the input source code. This project is split into three main deliverables:
1. **Arithmetic and Assignment Operators** — Handles operators like `+`, `-`, `*`, `/`, `%`, `=`, `+=`, `-=`, `*=`, `/=`.
2. **Conditional Statements** — Parses `if`, `elif`, and `else` blocks, ensuring that indentation is respected and reflected in the parse tree.
3. **Loops and Nested Structures** — Supports loops and nested control structures, as well as handling comments in Python code.

The final submission will be uploaded as a ZIP file and GitHub repository link for grading.

---

## **Team Members**
- **Aditya Ramakrishnan** 
- **Jack Scanlan** 
- **Sam Mallet**
- **Ty Hastings** 

---

## **Project Requirements**

### **Setup Instructions**
1. **Install ANTLR**  
   - Download and install **ANTLR 4.9.2** from [ANTLR official website](https://www.antlr.org/download.html).  
   - Add ANTLR to your system's **PATH** for command-line usage.  

2. **Install Required Tools**  
   - **Java JDK 8 or higher** (required for running ANTLR).  
   - **Python 3.x** (for testing the parser).  
   - **ANTLR Python Runtime**:
   - **Graphviz** (to generate SVG of parse tree):

     ```bash
     pip install antlr4-python3-runtime
     ```

3. **Cloning the Repository**  
   - Clone this repository:  
     ```bash
     git clone https://github.com/aditya-ramki04/Parser_Project.git
     ```

4. **Generate the Lexer and Parser Files**  
   - Run the following command to generate the parser and lexer from the grammar file:  
     ```bash
     antlr4 -Dlanguage=Python3 PythonSubset.g4
     ```

5. **Run the Parser**  
   - Compile the ANTLR grammar files, generate the `.py` files, and ensure everything is linked properly.  

---

## **Environment Requirements**
| **Software/Library** | **Version** |
|---------------------|-------------|
| **ANTLR**            | 4.9.2       |
| **Python**           | 3.x (latest)|
| **Java JDK**         | 8 or higher |
| **pip packages**     | antlr4-python3-runtime |

Ensure that your **PATH** variable includes the directory where `antlr4` is installed. 

---
## **How to Use/Run the Parser**

1. **Input Your Python Code**  
   -The code to test is in 'test_parser.py' for the final Deliverable

2. **Run the Parser**  
   - Execute the following command to parse the file:  
     ```bash
     python3 test_parser.py
     ```

3. **View Parse Tree Output**  
   - The output will display a parse tree with nodes corresponding to the if, elif, and else blocks, as well as arithmetic, assignment, and loop structures.  
   - Any errors or missing indentation will also be displayed.  


---

## **Project Demo**
[Link to Video Demo](https://your-link-to-demo-video.com)  


---
