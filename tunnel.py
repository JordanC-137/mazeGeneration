class Tunnel:
    def __init__(self, a, b, value):
        self.a = a
        self.b = b
        self.value = value
        
    def connects(self):
        if self.a < self.b:
            return (self.a, self.b)
        else:
            return (self.b,self.a)
        

    def __str__(self):
        return str(self.connects())


t = Tunnel((1, 1), (1,0))

print(t)
