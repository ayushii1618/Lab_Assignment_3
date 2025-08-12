def invertdict(d):
    """
    Inverts a dictionary by swapping keys and values.
    Assumes all values are unique.
    
    Parameters:
        d (dict): The original dictionary.
    
    Returns:
        dict: A new dictionary with keys and values swapped.
    """
    return {value: key for key, value in d.items()}

# Example usage
original_dict = {'a': 1, 'b': 2, 'c': 3}
inverted = invertdict(original_dict)
print("Original:", original_dict)
print("Inverted:", inverted)
