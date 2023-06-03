# Open the file
with open("input.txt", "r") as input_file:
    lines = input_file.readlines()

# Remove duplicates
unique_lines = list(set(lines))

# Open the file for writing and save the unique lines
with open("output.txt", "w") as output_file:
    output_file.writelines(unique_lines)
