import random
from . import Tunnel
class Chamber:
    tunnels = set([])

    def __init__(self, value):
        self.value = value

    def add_tunnel(self, b):
        weight = random.randint(100)
        tunnel = Tunnel(self.value, b, weight)
        self.tunnels.add(tunnel)
    
    def list_tunnels(self):
        return self.tunnels

