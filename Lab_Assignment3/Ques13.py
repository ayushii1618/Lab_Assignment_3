import re

def remove_parenthesis_area(strings):
    result = []
    for s in strings:
        # Remove anything in parentheses along with preceding space
        cleaned = re.sub(r"\s*\(.*?\)", "", s)
        result.append(cleaned)
    return result

# Sample data
data = ["example (.com)", "w3resource", "github (.com)", "stackoverflow (.com)"]

# Process and print each cleaned string
cleaned_strings = remove_parenthesis_area(data)
for item in cleaned_strings:
    print(item)
