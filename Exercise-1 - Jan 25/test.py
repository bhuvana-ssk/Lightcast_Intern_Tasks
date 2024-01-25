import unittest
from palindrome import isPalindrome
class TestIsPalindrome(unittest.TestCase):

    def test_one(self):
        self.assertTrue(isPalindrome("madam"))

    def test_two(self):
        self.assertTrue(isPalindrome("Do geese see God"))

    def test_three(self):
        self.assertTrue(isPalindrome(1221))

    def test_four(self):
        self.assertFalse(isPalindrome("hello"))

    def test_five(self):
        self.assertTrue(isPalindrome(""))

    def test_six(self):
        self.assertTrue(isPalindrome("a"))

    def test_seven(self):
        self.assertFalse(isPalindrome("Not a palindrome"))
      
    def test_eight(self):
        self.assertFalse(isPalindrome(123456))
        
    def test_nine(self):
        self.assertTrue(isPalindrome("Able was I ere I saw Elba"))

    def test_ten(self):
        self.assertFalse(isPalindrome("A man, a plan, a canal, Panama!"))

if __name__ == '__main__':
    unittest.main()