import unittest
from src.palindrome import is_palindrome

class TestPalindrome(unittest.TestCase):
    def test_palindromes_simples(self):
        self.assertTrue(is_palindrome("madam"))
        self.assertTrue(is_palindrome("reconocer"))
        self.assertFalse(is_palindrome("mamadera"))
        self.assertFalse(is_palindrome("computadora"))
    
    def test_frases_palindromes(self):
        self.assertTrue(is_palindrome("anita lava la tina"))
        self.assertTrue(is_palindrome("a santa at nasa"))
        self.assertTrue(is_palindrome("amo la pacifica paloma"))
    
    def test_frases_no_palindromes(self):
        self.assertFalse(is_palindrome("hola, como estas?"))
        self.assertFalse(is_palindrome("hoy hace frio"))
        self.assertFalse(is_palindrome("amo la buena paloma"))
    
    def test_casos_edge(self):
        self.assertTrue(is_palindrome(""))
        self.assertTrue(is_palindrome("a"))
        self.assertTrue(is_palindrome("ReCoNoCeR"))
        self.assertTrue(is_palindrome("No 'x' in Nixon?"))
        self.assertTrue(is_palindrome("12321"))

if __name__ == '__main__':
    unittest.main()




    

        
