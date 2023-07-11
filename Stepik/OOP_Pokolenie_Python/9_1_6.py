class HighScoreTable:
    def __init__(self, max_records):
        self.max_records = max_records
        self.scores = []

    def update(self, score):
        if len(self.scores) < self.max_records or score > self.scores[-1]:
            self.scores.append(score)
            self.scores.sort(reverse=True)
            self.scores = self.scores[:self.max_records]

    def reset(self):
        self.scores = []
