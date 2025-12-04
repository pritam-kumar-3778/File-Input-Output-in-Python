# w+ mode : Truncate previous text and start reading and writing from first.

f = open("sample5.txt", "w+")

f.write("123")

# Previously file contain
# Pritam
# Kumar
# Patel
# After using w+ mode
# 123

f.close()