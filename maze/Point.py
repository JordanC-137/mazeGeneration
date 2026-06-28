class Point():
    def __init__(self, x, y):
        self.x = x
        self.y = y
    
    def __init__(self, coordinate):
        self.x = coordinate[0]
        self.y = coordinate[1]

    def get_tuple_representation(self):
        return (self.x, self.y)
    
    def __eq__(self, other_point):
        return self.x == other_point.x and self.y == other_point.y

    def __hash__(self):
        return(hash(f"{self.x}.{self.y}"))
    
    def __lt__(self, other_point):
        return self.get_tuple_representation() < other_point.get_tuple_representation()