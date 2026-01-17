# rules.py
class CaveRule:
    def __init__(self, death_threshold=4):
        self.death_threshold = death_threshold

    def apply(self, is_wall, wall_neighbors):
        """
        Returns new cell state:
        1 = wall
        0 = empty
        """
        if wall_neighbors < self.death_threshold:
            return 0
        return 1
    
class TwoPhaseCaveRule:
    def __init__(self, survival_min=3, birth_min=4):
        self.survival_min = survival_min
        self.birth_min = birth_min

    def apply(self, is_wall, wall_neighbors):
        if is_wall:
            if wall_neighbors < self.survival_min:
                return 0
            return 1
        else:
            if wall_neighbors > self.birth_min:
                return 1
            return 0