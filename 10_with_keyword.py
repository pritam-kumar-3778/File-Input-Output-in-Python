# with keyword : No need to close file explictly, It's close automatically

with open("sample.txt", "r") as f:

    data = f.read()
    print(data)
    print(f"The length of data in sample.txt file is : {len(data)}")