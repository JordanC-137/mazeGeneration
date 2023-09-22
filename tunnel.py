import re


class Tunnel:
    def __init__(self, a, b, value):
        self.a = a
        self.b = b
        self.value = value
        
    def connection(self):
        if self.a < self.b:
            return (self.a, self.b)
        else:
            return (self.b,self.a)
        

    def __eq__(self, other):
        if isinstance(other, Tunnel):
            if self.connection() == other.connection():
                return True
        else:
            return False

    def __str__(self):
        return str(self.connection())

    def __hash__(self):
        return self.connection()

"""
t1 = Tunnel((1, 1), (1,0))
t2 = Tunnel((1, 0), (1,1))
t3 = Tunnel((1, 0), (1,2))
t4 = Tunnel((1, 0), (1,3))

tunnel_list = [t3, t2, t4]
if t1 in tunnel_list:
    print("Tunnel")
"""