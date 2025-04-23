def recursive_palindrome(s:str) -> bool:
    s = s.strip().lower()
    if len(s) <= 1:
        return True
    elif s[0] == s[-1]:
        return recursive_palindrome(s[1:-1])
    return False

if __name__ == "__main__":
    true = "a man a plan a canal panama"
    false = "loop"

    test_1 = recursive_palindrome(true)
    test_2 = recursive_palindrome(false)

    print("  recursive_palindrome():")
    print(f"\t> \"{true}\"\n\t   is a palindrome?", test_1, "\n")
    print(f"\t> \"{false}\"\n\t   is a palindrome?", test_2)
