# def binary_search(arr, target):
#     low = 0
#     high = len(arr) - 1

#     while low <= high:
#         mid = (low + high) // 2

#         if arr[mid] == target:
#             return mid
#         elif arr[mid] < target:
#             low = mid + 1
#         else:
#             high = mid - 1

#     return -1

# # Take array input from user
# arr = list(map(int, input("Enter space separated integers: ").split()))

# # Ask for index value to search
# target = int(input("Enter the value to search: "))

# # Call binary search function
# result = binary_search(arr, target)

# # Check if result is valid
# if result != -1:
#     print(f"Target value {target} found at index {result}.")
# else:
#     print(f"Target value {target} not found in the array.")

def binary(num_list, target):
    start = 0
    end = len(num_list)-1
    while start <= end:
        mid = (start + end)//2
        if num_list[mid] > target:
            end = mid - 1
        elif num_list[mid] < target:
            start = mid + 1
        else:
            return mid
        return None
try:       
    number = [11, 23, 14, 20, 24, 44]
    target_1 = (20)
    target_2 = (88)
    sorted_number = sorted(number)
    mine = binary(sorted_number,target_1)
    print(f"the index for target_1 is {mine}")
    mine2 = binary(sorted_number,target_2)
    print(f"the index for target_1 is {mine2}")
except Exception as err:
    print(f"error:{err}" )