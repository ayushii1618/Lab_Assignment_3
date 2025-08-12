import glob

def extract_characters_from_files(file_list):
    characters = []
    for file_name in file_list:
        try:
            with open(file_name, 'r', encoding='utf-8') as file:
                text = file.read()
                characters.extend(list(text))  # Add each character to list
        except FileNotFoundError:
            print(f"File not found: {file_name}")
    return characters


# Example: get all .txt files in current directory
files = glob.glob("*.txt")

# Extract characters from the files
all_characters = extract_characters_from_files(files)

print("Extracted characters list:")
print(all_characters)
