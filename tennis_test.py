import unittest
from tdd import TennisScore

class TSTest(unittest.TestCase):
    def setUp(self):
        self.ts = TennisScore("player1", "player2")

    def test_love_all(self):
        self._is_score("Love All")

    def test_fifteen_love(self):
        self._player1_scored(1)
        self._is_score("Fifteen Love")

    def test_thirty_love(self):
        self._player1_scored(2)
        self._is_score("Thirty Love")

    def test_forty_love(self):
        self._player1_scored(3)
        self._is_score("Forty Love")

    def test_love_fifteen(self):
        self._player2_scored(1)
        self._is_score("Love Fifteen")

    def test_love_thirty(self):
        self._player2_scored(2)
        self._is_score("Love Thirty")

    def test_love_forty(self):
        self._player2_scored(3)
        self._is_score("Love Forty")

    def test_fifteen_all(self):
        self._player1_scored(1)
        self._player2_scored(1)
        self._is_score("Fifteen All")

    def test_deuce(self):
        self._deuce()
        self._is_score("Deuce")

    def test_player1_adv(self):
        self._deuce()
        self._player1_scored(1)
        self._is_score("player1 adv")

    def test_player2_adv(self):
        self._deuce()
        self._player2_scored(1)
        self._is_score("player2 adv")

    def test_player1_win(self):
        self._deuce()
        self._player1_scored(2)
        self._is_score("player1 win")

    def test_player2_win(self):
        self._player1_scored(4)
        self._player2_scored(2)
        self._is_score("player1 win")



    # utils func
    def _is_score(self, score):
        self.assertEqual(
            score,
            self.ts.get_score()
        )

    def _player1_scored(self, times):
        for _ in range(times):
            self.ts.a_scored()

    def _player2_scored(self, times):
        for _ in range(times):
            self.ts.b_scored()

    def _deuce(self):
        self._player1_scored(3)
        self._player2_scored(3)




if __name__== "__main__":
    unittest.main()
