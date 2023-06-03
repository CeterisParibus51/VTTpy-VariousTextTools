# Open the input text file for reading
with open('input.txt', 'r') as infile:
    # Read in all the lines of the file
    lines = infile.readlines()

# Sort the lines alphabetically
sorted_lines = sorted(lines)

# Open the output text file for writing
with open('output.txt', 'w') as outfile:
    # Write the sorted lines to the output file
    outfile.writelines(sorted_lines)
