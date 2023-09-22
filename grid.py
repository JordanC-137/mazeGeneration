from . import Chamber, Tunnel

class Grid():
    grid = None
    def __init__(self, height, width):
        self.height = height
        self.width = width
        self.build(height, width)

    #Build by layers
    def build(self, height, width):
        for j in range(height):
            if i == 0:
                grid = [[]]
                for i in range(width):
                    c = Chamber((i,j))
                    if i != 0:
                        c.add_tunnel(grid[i][-1])
                    grid[0].append(c)

