#! /usr/bin/env python3

"""
A parser for C++ programming language

This parser generates statistical infomation about the program,
and offers code formatting functionalities.
This parser only implements a subset of the C++ programming language,
and should not be relied on as a full-fledged code analyzer.

Algorithm:
The program is based on regular expression to
parse general infomation of a C++ source file.
It cannot be used to check for syntax error.
If there is syntax error in the C++ source file,
the parsed result is likely to be erroneous

Match all the top level include header, global variable,
function definition, class definition

"""

import re
import sys


# fundamantal types
FUND_TYPES = [
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
    'short',
    'long',
    'const',
    'volatile',
    'restrict',
    'extern'
]


# optional modifier
MODIFIER = '(?:(' + '|'.join(MODIFIERS) + ')\s+)?'

# type name + possible pointer type + possible reference type
TYPE = r'([a-zA-Z_][\w_]*\s*\**\s*&?)'

# identifier
IDENTIFIER = r'([a-zA-Z_][\w_]*)'

# pattern of variable/function declaration(definition)
# capture modifier, type, identifier
VAR_DEF = re.compile(
    ''.join([
        MODIFIER,               # 1 modifier supported
        TYPE + r'\s*',          # match type infomation
        IDENTIFIER,             # identifier
        '.*;'                   # initialization, ended by semicolon
    ])
    , re.X | re.S
)

# pattern of function definition
# capture return type, function name, argument list, function body
FUNC_DEF = re.compile(
    ''.join([
        MODIFIER,               # 1 modifier supported
        TYPE + r'\s*',          # match type infomation
        IDENTIFIER              # identifier
        r'\s*\(',               # left parenthese of argument list
        r'(.*)',                # capture argument list
        r'\)\s*',               # left parenthese of argument list
        r'\{'
    ])
    , re.X | re.S
)

# pattern of class definition
# capture member variables
CLASS_DEF = re.compile(
    ''.join([
        r'(class|struct)\s+',
        IDENTIFIER
    ])
    , re.X | re.S
)

COMMENT = re.compile(r'/\*.*\*/', re.S)

# pattern of include header
# capture the name of the header, user header / system header
INCLUDE_HEADER = re.compile(
    r"""\#include\s*    # include directive
        (\"|<)(.+)(\"|>)"""
    , re.X
)


def parse_func():
    pass


def parse_class():
    pass


def main():
    pass


if __name__ == '__main__':
    main()
