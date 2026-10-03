class Team:
    def __init__(self, name, points):
        self.name = name
        self.points = points
    
    def __add__(self, other):
        return self.points + other.points
    
team1 = Team("Red", 38)
team2 = Team("Blue", 45)

print(team1+team2)