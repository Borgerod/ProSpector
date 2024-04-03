from __future__ import print_function
from sys import getsizeof, stderr
from itertools import chain
from collections import deque
try:
    from reprlib import repr
except ImportError:
    pass






class SlotClass:
    __slots__ = "x", "y", "z",
    # __slots__ = ('x', 'y', 'z',)
    __slots__ = 'x', 'y', 'z'

    def __init__(self) -> None:
        self.x = 0
        self.y = "hello"
        self.z = False

    def get_x(self):
        return self.x

    def set_x(self, new_val):
        self.x = new_val


def slotClassExample():

    s = SlotClass()
    print(s.x)

    ''' #! ==> AttributeError: 'SlotClass' object has no attribute '__dict__'. Did you mean: '__dir__'?   
    print(f'NormalClass dict: {s.__dict__}') 
    '''

class Parent:
    b = 56
    
    def __init__(self) -> None:
        self.y = 'hello'       

class NormalClass(Parent):
    a = 42

    def __init__(self) -> None:
        self.x = 'hello'

    def method(self):
        return 

def normalClassExample():
    n = NormalClass()
    print(n.x)
    print(f'NormalClass dict: {n.__dict__}')
    
    print(f'n.a (not found in n, looked up in NormalClass):  {n.a}')
    print(f'n.b (not found in n, looked up in Parent):  {n.b}')
    
    # with pytest.raises(AttributeError):  #! This doesnt work for some reason..
        # n.y
        
    '''#! ==> AttributeError: 'NormalClass' object has no attribute 'y'
    # print(f'n.y: {n.y}')
    '''

if __name__ == '__main__':
    # slotClassExample()
    # normalClassExample()

    s = SlotClass()

    print(NormalClass.__dict__)
    print("_"*60)
    print(SlotClass.__dict__)
 


