def iterative_sum(l:list) -> int:
    sum = 0

    for i in l:
        sum += i

    return sum

def recursive_sum(l:list) -> int:
    if len(l) == 0:
        return 0

    sum = l[0]
    l = l.copy()
    l.pop(0)

    return sum + recursive_sum(l)

if __name__ == "__main__":
    numbers = [7, 6, 5, 1, 3] # sum: 22

    test_1 = iterative_sum(numbers)
    test_2 = recursive_sum(numbers)

    print("iterative_sum():", test_1)
    print("recursive_sum():", test_2)
