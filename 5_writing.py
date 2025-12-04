# Writing mode : It appends at the end.

# Open the file with read mode.
f = open("sample.txt", "a")

# Write
f.write(" Also AI/ML Engineer")
# Previouslly the file have content 
# Pritam Kumar patel
# A Data Scientist
# After Writing mode
# Pritam Kumar patel.
# A Data ScientistAlso AI/ML Engineer Also AI/ML Engineer


# Close the file
f.close()