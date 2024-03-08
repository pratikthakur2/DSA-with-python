import numpy as np

def binarySearch(my_list,x):
    low = 0
    high = len(my_list)-1

    while low<=high:
        mid = (low+high)//2

        if x == my_list[mid]:
            return mid
        
        elif x>=my_list[mid]:
            low = mid+1

        else:
            high = mid-1

    return -1

list1 = [1,3,4,6]
print(f"Element is present at position {binarySearch(list1,6)}")

