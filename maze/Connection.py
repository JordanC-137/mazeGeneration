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
    

    def ordered_interpretation():
        pass

    def __hash__(self):
        sorted_points = sorted(self.points)
        hash1 = hash(sorted_points[0])
        hash2 = hash(sorted_points[1])
        #Ordered interpretation so consistency 
        return f"{hash1}{hash2}"