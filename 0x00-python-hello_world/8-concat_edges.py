#!/usr/bin/python3

# Original string
str_original = "Python is an interpreted, interactive, object-oriented programming" \
               " language that combines remarkable power with very clear syntax"

# Extract and concatenate substrings
substring1 = str_original[39:67]
substring2 = str_original[107:112]
substring3 = str_original[:6]

result = substring1 + substring2 + substring3

# Print the concatenated result
print(result)

