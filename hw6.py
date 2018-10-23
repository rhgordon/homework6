

import re
import unittest
inFile = open('regex_sum_42.txt', 'r')
data = inFile.read()
inFile.close()

def sumNums(fileName):
    inFile = open(fileName, 'r')
    read_file = inFile.read()
    inFile.close()
    nums = re.findall(r'[0-9]+', read_file)
    ints = [int(x) for x in nums]
    return sum(ints)
    
def countWord(fileName, word):
    inFile = open(fileName, 'r')
    read_file = inFile.read()
    inFile.close()
    first_let = word[0]
    words = re.findall(r"(?i)" + str(word) + "(?!\w+)", data)
    return len(words)


def listURLs(fileName):
    inFile = open(fileName, 'r')
    read_file = inFile.read()
    inFile.close()
    URL = re.findall(r'www\.[a-zA-Z0-9]+\.[a-z]', read_file)
    return URL


class TestHW6(unittest.TestCase):
    """ Class to test this homework """

    def test_sumNums1(self):
        """ test sumNums on the first file """
        self.assertEqual(sumNums("regex_sum_42.txt"), 445833)

    def test_sumNums2(self):
        """ test sumNums on the second file """
        self.assertEqual(sumNums("regex_sum_132198.txt"), 374566)

    def test_countWord(self):
        """ test count word on the first file """
        self.assertEqual(countWord("regex_sum_42.txt", "computer"),21)

    def test_listURLs(self):
        """ test list URLs on the first file """
        self.assertEqual(len(listURLs("regex_sum_42.txt")), 3)

# run the tests
unittest.main(verbosity=2)
