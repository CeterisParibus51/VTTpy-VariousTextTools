import random

# Ask the user for the number of iterations
iterations = int(input("Enter the number of iterations: "))

# Ask the user for the amount and filenames of the input files
file_names = []
num_files = int(input("Enter the number of input files: "))
for i in range(num_files):
    file_name = input(f"Enter the name of input file {i + 1}: ")
    file_names.append(file_name)

# Open the input files for reading
input_files = []
for file_name in file_names:
    input_file = open(file_name, "r")
    input_files.append(input_file)

# Read the contents of the files and split them by commas
entries = []
for input_file in input_files:
    file_entries = input_file.read().split(",")
    entries.append(file_entries)
    
# Open the output file for writing
with open("output.txt", "w") as fout:
    # For each iteration, select one random entry from each file and write the combined entries to the output file
    for i in range(iterations):
        combined_entry = ""
        for file_entries in entries:
            entry = random.choice(file_entries).strip()
            combined_entry += f"{entry} "
        combined_entry += "\n"
        fout.write(combined_entry)

# Close the input files
for input_file in input_files:
    input_file.close()

# Print the results to the terminal
print(f"Combined entries written to output.txt for {iterations} iterations:")
with open("output.txt", "r") as f:
    print(f.read())