# a+ mode : Pointer starts from end

f = open("sample4.txt", "a+")

f.write("123")

# Previously file contain
# Pritam
# Kumar
# Patel
# After using a+ mode
# Pritam
# Kumar
# Patel
# 123

f.close()