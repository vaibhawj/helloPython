from main.palindrome_check import isPalindrome

def test_should_return_true():
    assert True == isPalindrome("wow")

def test_should_return_false():
    assert False == isPalindrome("waa")

def test_should_return_true_for_even_length():
    assert True == isPalindrome("woow")

def test_should_return_false_for_even_length():
    assert False == isPalindrome("woaw")