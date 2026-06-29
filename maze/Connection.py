from Point import Point

class Connection:
    def __init__(self, point1: Point, point2: Point, weight: int):
        self.weight = weight
        self.points = {point1, point2}

    def __eq__(self, other_connection):
        if self.points == other_connection.points:
            return True
        else:
            return False
    

    def __str__(self):
        p1, p2 = sorted(self.points)
        return f"Connection({p1}-{p2})"

    def __hash__(self):
        sorted_points = sorted(self.points)
        hash1 = hash(sorted_points[0])
        hash2 = hash(sorted_points[1])

        return f"{hash1}{hash2}"