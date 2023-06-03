import random

# Get user input
array = input("Enter array of characters: ")
length = int(input("Enter length of hash: "))

# Generate random hash
hash = ''.join(random.choices(array, k=length))

# Write hash to file
with open("randomhash.txt", "w") as f:
    f.write(hash)
    
print(f"Generated random hash: {hash}")
