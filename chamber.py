import random
from tunnel import Tunnel
class Chamber:
    tunnels = set([])

    def __init__(self, value):
        self.value = value
    
    def __str__(self):
        return f"[Chamber {self.value}]: {self.list_tunnels}"

    #Adding of tunnel must be reflexive between this and other chamber
    def add_tunnel(self, other):
        if not isinstance(other, Chamber):
            return False
        weight = random.randint(0, 100)
        tunnel = Tunnel(self.value, other, weight)
        self.tunnels.add(tunnel)
        if tunnel not in other.list_tunnels():
            other.add_tunnel(self)
        return True

    
    def list_tunnels(self):
        return self.tunnels

c1 = Chamber((0,1))
c2 = Chamber((0,2))
c1.add_tunnel(c2)
print(c1)
print(c2)