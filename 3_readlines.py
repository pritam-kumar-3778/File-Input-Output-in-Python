# Readlines

# Open the file with read mode.
f = open("sample.txt", "r")

# Read the file as an LIST.
data = f.readlines()
print(data)

# Close the file
f.close()