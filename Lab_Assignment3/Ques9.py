# Recursive Binary Search
def binary_search_recursive(arr, low, high, target):
    if low <= high:
        mid = (low + high) // 2
        if arr[mid] == target:
            return mid
        elif arr[mid] > target:
            return binary_search_recursive(arr, low, mid - 1, target)
        else:
            return binary_search_recursive(arr, mid + 1, high, target)
    return -1

# Iterative Binary Search
def binary_search_iterative(arr, target):
    low, high = 0, len(arr) - 1
    while low <= high:
        mid = (low + high) // 2
        if arr[mid] == target:
            return mid
        elif arr[mid] > target:
            high = mid - 1
        else:
            low = mid + 1
    return -1

# Example usage
arr = [2, 4, 6, 8, 10, 12, 14, 16]
target = int(input("Enter the number to search: "))

# Recursive method
rec_index = binary_search_recursive(arr, 0, len(arr) - 1, target)
print("Recursive Search: ", "Found at index" if rec_index != -1 else "Not found", rec_index if rec_index != -1 else "")

# Iterative method
iter_index = binary_search_iterative(arr, target)
print("Iterative Search: ", "Found at index" if iter_index != -1 else "Not found", iter_index if iter_index != -1 else "")
