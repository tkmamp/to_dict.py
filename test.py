from to_dict.code import toDict
from test2 import test_instantiate



class A():
    def __init__(self):
        self.primitive_1 = 'string'
        self.primitive_2 = 123
        self.primitive_3 = 1.010
        self.d = dict(a=1, b='1', c=1.0)
        self.b = B()


class B():
    def __init__(self):
        self.attr1 = 1
        self.d_1 = dict(th='is', i='s', bull='shit')
        self.l = [C(i) for i in range(10)]
        

class C():
    def __init__(self, j):
        self.attrC_1 = '1'
        self.attrC_2 = 'json'
        self.j = j
        



a = A()
td = toDict()


d, classlist = td.to_dict(a)

d['classes'] = classlist

ar = td.reconstruct(d, [eval(c) for c in classlist])

l = []

pass