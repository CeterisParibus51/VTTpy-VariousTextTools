import string

# Ask user for input file name
input_file = input("Enter the input file name (include .txt extension): ")

# Read input file
with open(input_file, "r") as f:
    lines = f.readlines()

# Count number of lines
num_lines = len(lines)

# Count total number of characters
num_chars = sum(len(line) for line in lines)

# Count total number of words
words = []
for line in lines:
    words.extend(line.strip().split())
num_words = len(words)

# Find shortest and longest word length
shortest_word = min(words, key=len)
longest_word = max(words, key=len)
shortest_word_len = len(shortest_word)
longest_word_len = len(longest_word)

# Count characters per line and unique characters
char_count_per_line = []
unique_char_counts = {}
for i, line in enumerate(lines):
    # Count characters per line
    char_count = len(line)
    char_count_per_line.append(f"line{i+1}:{char_count}")

    # Count unique characters
    for char in line:
        if char not in unique_char_counts:
            unique_char_counts[char] = 1
        else:
            unique_char_counts[char] += 1

# Write output to file
output_file = input_file.replace(".txt", "-counted.txt")
with open(output_file, "w") as f:
    f.write(f"Total line count: {num_lines}\n")
    f.write(f"Total character count: {num_chars}\n")
    f.write(f"Total word count: {num_words}\n")
    f.write(f"Shortest word length: {shortest_word_len}\n")
    f.write(f"Longest word length: {longest_word_len}\n")
    f.write("Character count per line:\n")
    f.write("\n".join(char_count_per_line) + "\n")
    f.write("Unique character counts:\n")
    for char, count in unique_char_counts.items():
        f.write(f"{char}: {count}\n")