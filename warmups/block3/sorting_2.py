import tracemalloc
from random import randrange, shuffle
from time import perf_counter

from sorting_1 import *


def mergesort(nums:list) -> list:
    return NotImplemented

def quicksort(nums:list) -> list:
    return NotImplemented

# ==== TESTER ==== #

if __name__ == "__main__":
    print("==== test sorts ====")

    NUM_VALUES = 5000
    print()
    print(f"making lists with {NUM_VALUES} values...")


    '''-----------------
    # LIST METHODS     #
    -----------------'''

    print("""Select which list you want to test:
    1. ALL UNIQUE VALUES, RANDOM ORDER:
    2. ALL UNIQUE VALUES, REVERSED ORDER
    3. ALMOST IN ORDER
    4. FEWER BUT REPEATED VALUES
    5. ALREADY IN ORDER
    """)
    nums = []
    list_type = int(input("> "))
 
    if list_type == 1:
        nums = list(range(1, NUM_VALUES+1))
        print("shuffling....")
        shuffle(nums)

    elif list_type == 2:
        nums = list(range(NUM_VALUES, 0, -1))

    elif list_type == 3:
        nums = list(range(1, NUM_VALUES+1))
        for i in range(NUM_VALUES//100):
            nums[randrange(NUM_VALUES)] = randrange(NUM_VALUES)

    elif list_type == 4:
        nums = [4,5,2,7,9,6,3,2,3,45,6,7,731,3,3,4,76,78,456,23,342,5,58,678,45,3,5,25,54,76]
        nums  = NUM_VALUES//len(nums) * nums
        print(len(nums))

    elif list_type == 5:
        nums = list(range(1, NUM_VALUES+1))


    #equivalent copys, so all sorts are comparable
    nums_copy1 = nums.copy()
    nums_copy2 = nums.copy()
    nums_copy3 = nums.copy()
    nums_copy4 = nums.copy()

    print()
    print("beginning sorts...")

    print()
    print("starting bubble-sort...")
    tracemalloc.start()
    start = perf_counter()
    bubble_sort(nums)
    end = perf_counter()
    current, peak = tracemalloc.get_traced_memory()
    tracemalloc.stop()
    #print(nums)
    print(f"bubble-sort time taken: {end - start:.5f} seconds")
    print(f"Peak memory usage: {peak} bytes")

    print()
    print("starting selection-sort...")
    tracemalloc.start()
    start = perf_counter()
    selection_sort(nums_copy1)
    end = perf_counter()
    current, peak = tracemalloc.get_traced_memory()
    tracemalloc.stop()
    #print(nums_copy1)
    print(f"selection-sort time taken: {end - start:.5f} seconds")
    print(f"Peak memory usage: {peak} bytes")


    print()
    print("starting quick-sort...")
    tracemalloc.start()
    start = perf_counter()
    nums_copy2 = quicksort(nums_copy2)
    end = perf_counter()
    current, peak = tracemalloc.get_traced_memory()
    tracemalloc.stop()
    #print(nums_copy2)
    print(f"quick-sort time taken: {end - start:.5f} seconds")
    print(f"Peak memory usage: {peak} bytes")


    print()
    print("starting merge-sort...")
    start = perf_counter()
    tracemalloc.start()
    nums_copy3 = mergesort(nums_copy3)
    end = perf_counter()
    current, peak = tracemalloc.get_traced_memory()
    tracemalloc.stop()
    #print(nums_copy3)
    print(f"merge-sort time taken: {end - start:.5f} seconds")
    print(f"Peak memory usage: {peak} bytes")

    print()
    print("starting python sort()...")
    tracemalloc.start()
    start = perf_counter()
    nums_copy4.sort()
    end = perf_counter()
    current, peak = tracemalloc.get_traced_memory()
    tracemalloc.stop()
    #print(nums_copy4)
    print(f"python sort() time taken: {end - start:.5f} seconds")
    print(f"Peak memory usage: {peak} bytes")
