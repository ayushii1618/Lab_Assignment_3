from collections import OrderedDict

def first_non_repeating_char(s):
    char_count = OrderedDict()
    
    # Count occurrences in order
    for char in s:
        char_count[char] = char_count.get(char, 0) + 1
    
    # Find first char with count 1
    for char, count in char_count.items():
        if count == 1:
            return char
    return None

# Example usage
input_str = "swiss"
result = first_non_repeating_char(input_str)
if result:
    print(f"First non-repeating character: '{result}'")
else:
    print("No non-repeating character found.")
