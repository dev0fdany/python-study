class Student:
    def __init__(self, score=None):
        self._score = None
        if score is not None:
            self.score = score
    
    @property
    def score(self):
        return self._score
    
    @score.setter
    def score(self, value):
        if value > 0 and value < 100:
            self._score = value
        else:
            raise ValueError("Range Error.")
    
s = Student(20)
s.score = 85
s.score = 120