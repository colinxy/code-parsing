
"""
Component of function pattern matching
"""

# left curly brace of the function definition
# goes on the end of line, or on a new line
END_OF_LINE = 0
NEW_LINE    = 1

STYLE       = END_OF_LINE


class Type:
    def __init__(self, type):
        self.type_str = type
        self.major_type = ''
        self.modifier = ''
        self.pointer_ref = ''
    
    def parse_type(self):
        pass


class Func:
    def __init__(self, rtn_type, func_name, arg_str, func_body):
        self.rtn_type  = Type(rtn_type)
        self.func_name = func_name
        self.arg_str   = arg_str
        self.func_body = func_body

    def __str__(self):
        code_format = (
            "{} {}({})%s\{\n"
            "    {}\n"
            "\}"
        ) % (' ' if STYLE == END_OF_LINE else '\n')

        code_str = code_format.format(str(self.rtn_type),
                                      func_name,
                                      arg_str,
                                      func_body)
        return code_str

    def jsonify(self):
        pass


class Class:
    def __init__(self):
        pass
