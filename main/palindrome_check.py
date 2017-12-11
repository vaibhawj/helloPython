

def isPalindrome(str):
    j = len(str) - 1
    for i in range(int(len(str) / 2)):
        if str[i] != str[j]:
            return False
        j = j - 1
    return True
