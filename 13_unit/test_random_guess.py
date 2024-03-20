import unittest

from random_guess import random_answer, guess_answer


class TestRandomGuess(unittest.TestCase):
    def test_random_answer_with_valid_range(self):
        result = random_answer("1", "10")
        self.assertTrue(1 <= result <= 10)

    def test_random_answer_with_invalid_start(self):
        result = random_answer("a", "10")
        self.assertEqual(result, "Start number must be an integer!")

    def test_random_answer_with_invalid_end(self):
        result = random_answer("1", "b")
        self.assertEqual(result, "End number must be an integer!")

    def test_guess_answer_with_correct_guess(self):
        """Test if the guess_answer function returns True when the answer and guess are the same"""
        self.assertTrue(guess_answer(5, 5))

    def test_guess_answer_with_incorrect_guess(self):
        self.assertFalse(guess_answer(5, 4))


"""
对于 unittest ，必须主动调用 unittest.main() 才能运行测试用例，否则不会执行测试用例。
使用 pytest ，则不需要调用 unittest.main() ，只需要运行 pytest 即可。
"""
if __name__ == "__main__":
    unittest.main()
