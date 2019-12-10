from functools import partial

class Func():
    '''convenience class for parsing excel functions
        without having to do tons of string formatting'''
    def __init__(self, name, *args):
        self.name = name
        self.args = args

    def __repr__(self):
        return self.name + "(" + ", ".join(str(arg) for arg in self.args) + ")"      

    def __lt__(self, other):
        return LESSTHAN(self, other)

    def __le__(self, other):
        return LESSTHANEQ(self, other)

    def __gt__(self, other):
        return GREATERTHAN(self, other)

    def __ge__(self, other):
        return GREATERTHANEQ(self, other)

    def __eq__(self, other):
        return EQUAL(self, other)

    def __ne__(self, other):
        return NOTEQUAL(self, other)

    def __add__(self, other):
        return ADD(self, other)

    def __radd__(self, other):
        return ADD(other, self)

    def __sub__(self, other):
        return SUB(self, other)

    def __rsub__(self, other):
        return SUB(other, self)

    def __mul__(self, other):
        return MUL(self, other)
    
    def __rmul__(self, other):
        return MUL(other, self)

    def __truediv__(self, other):
        return DIV(self, other)

    def __rtruediv__(self, other):
        return DIV(other, self)

    def parse(self):
        return "=" + str(self)


class Infix(Func):
    '''convenience for infix functions'''
    def __init__(self, sign, a,b):
        super().__init__(sign, a,b)
        
    def __repr__(self):
        return "{} {} {}".format(self.args[0], self.name, self.args[1])

##comparison Infixs
LESSTHAN = partial(Infix, "<")
LESSTHANEQ = partial(Infix, "<=")
GREATERTHAN = partial(Infix, ">")
GREATERTHANEQ = partial(Infix, ">=")
EQUAL = partial(Infix, "=")
NOTEQUAL = partial(Infix, "<>")

##calculation Infixs
ADD = partial(Infix, '+')
SUB = partial(Infix, '-')
MUL = partial(Infix, '*')
DIV = partial(Infix, '/')

##utility functions
PAREN = partial(Func, '')

##functions
SUM = partial(Func, 'SUM')
COUNT = partial(Func, 'COUNT')
IF = partial(Func, 'IF')
AND = partial(Func, 'AND')
IFERROR = partial(Func, 'IFERROR')
ISNUMBER = partial(Func, 'ISNUMBER')
