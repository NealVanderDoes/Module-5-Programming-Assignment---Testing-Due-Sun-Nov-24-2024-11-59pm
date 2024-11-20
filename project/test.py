import unittest

from my_sum import sum


class TestSum(unittest.TestCase):
    def test_list_int(self):
        """
        Test that it can sum a list of integers
        """
        data = [1, 2, 3]
        result = sum(data)
        self.assertEqual(result, 6)

if __name__ == '__main__':
    unittest.main()


"""
I think this was a pretty simple test to run for a piece of code.
Testing in general gives projects an extra element of thoroughness that strengthens your code. 
For the test results themselves, I think they're a useful tool to check your code for oversights while it's being made 
and to see if future updates break anything.
"""