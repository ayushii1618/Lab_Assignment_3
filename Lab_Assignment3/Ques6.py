# Read input string
input_str = input("Enter comma-separated integers: ")

# Split by comma, strip spaces, convert to integers, and double
numbers = [int(num.strip()) * 2 for num in input_str.split(",")]

# Print result as a list of integers
print(numbers)
