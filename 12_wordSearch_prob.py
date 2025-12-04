# Word search
# file : word_search.txt
# data : I am Pritam
# I am learning Python now
# I am learning AI/Ml
# Search word Python with line number

data = True
line_number = 1
word = "Python"

with open("word_search.txt", "r") as f:
    # As we have to find line number, we process data line by line by using readline.
    while data:
        data = f.readline()
        if(word in data):
            print(f"{word} found at line number {line_number}")
            break

        print(data)
        line_number += 1
