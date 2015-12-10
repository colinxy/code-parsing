#! /usr/bin/env python

"""
A parser for C++ programming language

Algorithm:
The program is based on regular expression to
parse general infomation of a C++ source file.
It cannot be used to check for syntax error.
If there is syntax error in the C++ source file,
the parsed result is likely to be erroneous

Match all the top level include header, global variable, 
function definition, class definition

NOTICE: This module assumes many coding conventions,
and should not be used as a reliable code analyzer.
The following coding conventions were assumed:

- All the headers files are put at the top of the file
- No parentheses in function perimeter list
"""

import re
import sys


# fundamantal types
TYPES = [
    'void',
    'bool',
    'char',
    'short',
    'int',
    'long',
    'long long',
    'float',
    'double'
]

MODIFIERS = [
    'signed',
    'unsigned',
    'long'
]


IDENTIFIER = r'([\w]+)'

# pattern of global variable
# capture type, variable name
GLOBAL_VAR = re.compile(r"""

\s*
([\w]+)
;
()
""", re.X | re.S)

# pattern of include header
# capture the name of the header, user header / system header
INCLUDE_HEADER = re.compile(r"""
\#\s*include\s*(\"|<)(.*)\1
""", re.X | re.S)

# pattern of function definition
# capture return type, function name, argument list, function body
FUNC_DEF = re.compile(r"""
([\w]+)         # capture function name, identifier 
\s*             # optional space
\(([^\(\)])\)   # capture argument list, DID NOT DEAL WITH POSSIBLE PARENTHESES
\s*             # optional space
\{              # start of function
\}              # end of function
""", re.X | re.S)

FUNC  = IDENTIFIER + r'\s*' + r'\(([^\(\)])\)\s*\{\}'
MAIN  = r'\s+(main)\W'
CLASS = r'\s+(class|struct)\W'


def main():
    pass


if __name__ == '__main__':
    main()
