if __name__ == "__main__":
    #test searches
    nums = [2, 19, 24, 25, 70, 77, 96, 105, 107, 151, 298, 380, 381, 399, 2000]

    print(f"list: {nums}")
    keys = [107, 151, 2, 2000, 1, 2001, 108]
    for key in keys:
        print(f"key: {key:<5} lin:{linear_search(nums, key) :>3} bin:{binary_search(nums, key) :>3}")


    #test sorts:
    nums = [70, 381, 25, 107, 2, 298, 2000, 105, 96, 19, 380, 399, 151, 24, 77]
    bubble_list = nums.copy()
    bubble_sort(bubble_list)
    print(bubble_list)

    select_list = nums.copy()
    selection_sort(select_list)
    print(select_list)
