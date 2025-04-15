import unittest
#from src.palindrome import is_palindrome

class TestPalindrome(unittest.TestCase):
    def test_palindromes_simples(self):
        self.assertTrue(is_palindrome("madam"))
        self.assertTrue(is_palindrome("reconocer"))
        self.assertFalse(is_palindrome("mamadera"))
        self.assertFalse(is_palindrome("computadora"))

if __name__ == '__main__':
    unittest.main()

#from src.palindrome import clean_text

class TestPalindrome(unittest.TestCase):
    def test_text_cleaner(self):
        self.assertEqual(is_palindrome("A man, a plan, a canal: Panama!"), "amanaplanacanalpanama")
        self.assertEqual(is_palindrome("No 'x' in Nixon."), "noxinnixon")
        self.assertEqual(is_palindrome("¡Buen dia!"), "buendia")
    
if __name__ == '__main__':
    unittest.main()
        
