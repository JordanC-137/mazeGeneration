from Point import Point

class Connection:
    def __init__(self, point1: Point, point2: Point):
        self.points = {point1, point2}

    def __eq__(self, other_connection):
        if self.points == other_connection.points:
            return True
        else:
            return False
    