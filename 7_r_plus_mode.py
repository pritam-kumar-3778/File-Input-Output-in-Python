# r+ mode : Pointer starts from first
# Over write test from first.

f = open("sample3.txt", "r+")

f.write("123")

# Previously file contain
# abc
# Pritam
# Kumar
# Patel
# After using r+ mode
# 123
# Pritam
# Kumar
# Patel

f.close()