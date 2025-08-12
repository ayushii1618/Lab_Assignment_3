string_maps = {
    "1": "abc",
    "2": "def",
    "3": "ghi",
    "4": "jkl",
    "5": "mno",
    "6": "pqrs",
    "7": "tuv",
    "8": "wxy",
    "9": "z"
}

def two_digit_combinations(digits):
    """
    Generates all possible letter combinations for a given two-digit string
    based on the mapping.
    
    Parameters:
        digits (str): A string containing digits from 1 to 9.
    
    Returns:
        list: All possible two-letter combinations.
    """
    if len(digits) != 2:
        raise ValueError("Input must be exactly two digits long.")
    
    first_letters = string_maps.get(digits[0], "")
    second_letters = string_maps.get(digits[1], "")
    
    combinations = [a + b for a in first_letters for b in second_letters]
    return combinations

# Example usage
digit_str = "23"
result = two_digit_combinations(digit_str)
print(f"Two-digit letter combinations for '{digit_str}': {result}")
