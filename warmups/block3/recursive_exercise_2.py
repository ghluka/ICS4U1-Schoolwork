def iterative_palindrome(s:str) -> bool:
    return NotImplemented

def recursive_palindrome(s:str) -> bool:
    return NotImplemented

if __name__ == "__main__":
    true = "racecar"
    false = "loop"

    test_1a = iterative_palindrome(true)
    test_2a = recursive_palindrome(true)
    test_1b = iterative_palindrome(false)
    test_2b = recursive_palindrome(false)

    print(test_1a==test_2a and test_2a==True)
    print(test_1b==test_2b and test_2b==False)
