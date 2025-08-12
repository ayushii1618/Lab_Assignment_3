def n_largest_elements(nums, N):
    """
    Finds N largest elements in a list.
    Assumes len(nums) >= N.
    
    Parameters:
        nums (list): List of numbers.
        N (int): Number of largest elements to find.
    
    Returns:
        list: N largest elements in descending order.
    """
    return sorted(nums, reverse=True)[:N]

# Example usage
numbers = [10, 4, 3, 50, 23, 90]
N = 3
result = n_largest_elements(numbers, N)

print(f"{N} largest elements are: {result}")
