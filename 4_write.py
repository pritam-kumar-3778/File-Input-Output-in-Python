# Write Operation : It overwrite the entire file.

# Open the file with read mode.
f = open("sample.txt", "w")

# Write
f.write("Pritam Kumar patel. \n A Data Scientist.")
# Previouslly the file have content
# Pritam Kumar Patel
# A AI/ML Engineer
# By write now It over write to 
# Pritam Kumar patel
# A Data Scientist

# Close the file
f.close()