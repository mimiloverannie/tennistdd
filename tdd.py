class TennisScore(object):
    SCORE_MAP = {
        0: "Love",
        1: "Fifteen",
        2: "Thirty",
        3: "Forty"
    }

    def __init__(self, a, b):
        # player name
        self.a = a
        self.b = b
        # score
        self.a_score = 0
        self.b_score = 0
 
    def get_score(self):
        if self.a_score == self.b_score:  # same score
            if self.a_score >= 3:  # if score bigger than 3 and the smae => deuce
                return "Deuce"
            else:
                return "{} All".format(self.SCORE_MAP[self.a_score])
        else:
            if self.a_score > 3 or self.b_score > 3:  # in adv state
                lead = self.a if self.a_score > self.b_score else self.b
                if abs(self.a_score - self.b_score) == 1:  # at game point
                    return "{} adv".format(lead)
                else:  # someone win
                    return "{} win".format(lead)
            else:
                return "{} {}".format(*map(lambda x: self.SCORE_MAP[x], (self.a_score, self.b_score)))

    def a_scored(self): 
        self.a_score += 1

    def b_scored(self):
        self.b_score += 1
