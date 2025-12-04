# Readline

# Open the file with read mode.
f = open("sample.txt", "r")

# Read the file line b y line
data = f.readline()
print(data)

data = f.readline()
print(data)


# Close the file
f.close()