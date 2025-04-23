def pattern(n:int) -> str:
    s = f"{'#'*n}\n{'#'*n}"
    return pattern_helper(n - 1, s)


def pattern_helper(n:int, s:str) -> str:
    left = s[:(len(s)//2)]
    right = s[(len(s)//2-1):]
    print(">", left.replace("\n", "\\n"), "|", right.replace("\n", "\\n"))
    if n == 1:
        return f"{left}\n#{right}"
    s = f"{left}{'#'*n}\n{'#'*n}{right}"
    return pattern_helper(n - 1, s)

if __name__ == "__main__":
    print(pattern(5))
