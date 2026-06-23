class Point():
    def __init__(self, x, y):
        self.x = x
        self.y = y
    
    def __eq__(self, other_point):
        return self.x == other_point.x and self.y == other_point.y