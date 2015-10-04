from LinearProbeTable import Dictionary
# from SeparateChainTable import Dictionary
import unittest
import string
import random


class TestDictionary(unittest.TestCase):
    def test_insert(self):
        """
        :var valid_keys:    list of 150 random keys of ascii characters of size 1 - 11
        :var itemsCHAR:     list of 50 random items of ascii characters of size 0 - 9
        :var itemsINT:      list of 50 random integers from 0 - 999
        :var itemsLIST:     50 random lists each with a random mix of integers 0 - 1000 and ascii character strings of size 1 - 11
        """

        valid_keys = [''.join(random.choice(string.ascii_letters) for i in range(random.choice(range(1,12)))) for p in range(150)]

        itemsCHAR = [''.join(random.choice(string.ascii_letters) for i in range(random.choice(range(10)))) for p in range(50)]
        itemsINT = [random.choice(range(1000)) for p in range(50)]
        itemsLIST = [[random.choice((''.join(random.choice(string.ascii_letters) for i in range(random.choice(range(12)))), random.choice(range(1000)))) for p in range(10)] for q in range(50)]
        items = itemsCHAR + itemsINT + itemsLIST

        # create (key, item) tuples as valid test data:
        valid_data = zip(valid_keys, items)

        invalid_data = [(5125, 'teststring'), ([52, 100], 53), ((2, 'key'), 521)]

        test_dict = Dictionary(151, 31907)

        # insertTestData.txt logs random test data
        log = open('insertTestData.txt', 'w')
        log.write('\tKey\t\t\t\titem\n________________________________________\n')

        for key, item in valid_data:
            test_dict[key] = item
            self.assertTrue(test_dict[key] == item)
            log_string = '{:14}'.format(str(key)) + '| ' + str(item) + '\n'
            log.write(log_string)
        for key, item in invalid_data:
            with self.assertRaises(TypeError):
                test_dict[key] = item

        log.close()


if __name__ == '__main__':
    unittest.main()