# Open the file with read mode.
f = open("sample.txt", "r")

# Read the file
data = f.read()
print(data)

# Type of data in sample.txt file
print(type(data)) # Str

# Close the file
f.close()