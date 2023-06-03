# Ask user for input file name
input_file = input("Enter the input file name (include .txt extension): ")

# Read input file
with open(input_file, "r") as f:
    lines = f.readlines()

# Count number of lines
num_lines = len(lines)

# Initialize lists for shortest and longest word lengths per line
shortest_word_lengths = []
longest_word_lengths = []

# Count characters per line
char_count_per_line = []
for i, line in enumerate(lines):
    # Remove leading and trailing whitespace
    line = line.strip()

    # Find shortest and longest word length for this line
    words = line.split()
    if words:
        shortest_word_len = min(len(word) for word in words)
        longest_word_len = max(len(word) for word in words)
    else:
        shortest_word_len = 0
        longest_word_len = 0
    shortest_word_lengths.append(shortest_word_len)
    longest_word_lengths.append(longest_word_len)

    # Count characters per line
    char_count = len(line)
    char_count_per_line.append(f"line{i+1}:{char_count}")

# Write output to file
output_file = input_file.replace(".txt", "-linescounted.txt")
with open(output_file, "w") as f:
    f.write(f"Total line count: {num_lines}\n")
    f.write("Shortest word length per line:\n")
    f.write("\n".join(str(l) for l in shortest_word_lengths) + "\n")
    f.write("Longest word length per line:\n")
    f.write("\n".join(str(l) for l in longest_word_lengths) + "\n")
    f.write("Character count per line:\n")
    f.write("\n".join(char_count_per_line) + "\n")