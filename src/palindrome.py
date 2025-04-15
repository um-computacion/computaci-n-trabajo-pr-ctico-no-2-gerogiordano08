import string

def is_palindrome(word):

    word = word.lower()
    replace = str.maketrans('', '', string.punctuation + string.whitespace + '¡')
    return word.translate(replace) == word.translate(replace)[::-1] 
    
