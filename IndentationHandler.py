from enum import Enum
from dataclasses import dataclass
from typing import List, Optional

class TokenType(Enum):
    INDENT = 'INDENT'
    DEDENT = 'DEDENT'
    NEWLINE = 'NEWLINE'
    OTHER = 'OTHER'
    EOF = 'EOF'

@dataclass
class Token:
    type: TokenType
    value: str
    line: int
    column: int
    
class IndentationLexer:
    def __init__(self, input_text: str):
        self.input = input_text
        self.tokens: List[Token] = []
        self.current_line = 1
        self.current_column = 0
        self.indent_stack = [0]  # Stack to track indentation levels
        self.pending_tokens: List[Token] = []
        
    def tokenize(self) -> List[Token]:
        """Convert input text into tokens, handling Python indentation."""
        lines = self.input.splitlines(keepends=True)
        
        for line in lines:
            self._process_line(line)
            
        # Handle any remaining dedents at EOF
        self._handle_eof()
        
        return self.tokens
    
    def _process_line(self, line: str) -> None:
        """Process a single line of input."""
        # Skip empty lines
        if not line.strip():
            self.current_line += 1
            return
            
        # Calculate indentation level
        indent_level = self._calc_indent_level(line)
        raw_line = line.lstrip()
        
        # Handle indentation changes
        if self.tokens and self.tokens[-1].type != TokenType.NEWLINE:
            self._add_token(TokenType.NEWLINE, '\n')
            
        if indent_level > self.indent_stack[-1]:
            # Add INDENT token
            self._add_token(TokenType.INDENT, '    ')
            self.indent_stack.append(indent_level)
        elif indent_level < self.indent_stack[-1]:
            # Add DEDENT tokens
            while indent_level < self.indent_stack[-1]:
                self.indent_stack.pop()
                self._add_token(TokenType.DEDENT, '')
                
            if indent_level != self.indent_stack[-1]:
                raise IndentationError(
                    f"Unindent does not match any outer indentation level at line {self.current_line}"
                )
        
        # Process the actual content of the line
        self._process_line_content(raw_line)
        self.current_line += 1
        
    def _calc_indent_level(self, line: str) -> int:
        """Calculate the indentation level of a line."""
        indent = len(line) - len(line.lstrip())
        
        # Verify indentation is a multiple of 4 spaces (or single tab)
        if '\t' in line[:indent]:
            # Convert tab to 4 spaces for consistency
            indent = indent * 4
        elif indent % 4 != 0:
            raise IndentationError(
                f"Indent not a multiple of 4 spaces at line {self.current_line}"
            )
            
        return indent // 4  # Convert to indentation level
        
    def _process_line_content(self, content: str) -> None:
        """Process the non-whitespace content of a line."""
        if content:
            self._add_token(TokenType.OTHER, content.rstrip('\n'))
            
    def _handle_eof(self) -> None:
        """Handle end of file by closing all open indentation blocks."""
        while len(self.indent_stack) > 1:
            self.indent_stack.pop()
            self._add_token(TokenType.DEDENT, '')
        self._add_token(TokenType.EOF, '')
        
    def _add_token(self, type_: TokenType, value: str) -> None:
        """Add a token to the token list."""
        token = Token(
            type=type_,
            value=value,
            line=self.current_line,
            column=self.current_column
        )
        self.tokens.append(token)
        self.current_column += len(value)