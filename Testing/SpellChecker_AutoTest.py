import unittest
from SpellChecker import SpellChecker

class TestSpellChecker(unittest.TestCase):
    def test_query(self):
        checker = SpellChecker()
        validTestData = [('hello', 'Rare'), ('fantastic', 'Rare'), ('order', 'Common'),
                         ('absolute', 'Uncommon'), ('smartphone', 'Unknown'), ('aksfjalsf', 'Unknown')]

        invalidTestData = [315, 0, -4]

        for query, response in validTestData:
            self.assertTrue(checker.query(query) == response)

        for invalidQuery in invalidTestData:
            with self.assertRaises(TypeError):
                checker.query(invalidQuery)

    def test_class_count(self):
        checker = SpellChecker()
        self.assertTrue(checker.class_count('class_countTESTFILE.txt') == (5, 2, 3, 3, 13))



if __name__ == '__main__':
    unittest.main()