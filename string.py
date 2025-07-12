n = "Nitish Choudhary"

# Access first character
first_char = n[0]
print(first_char)

# Slicing string
nm = n[0:6]
print(nm)

# Negative indexing
print(n[-1])  # Last character

# More slicing examples
num_list = "0123456789"
print(num_list[:])           # Full string
print(num_list[3:])          # From index 3 to end
print(num_list[:7])          # From start to index 6
print(num_list[0:7:2])       # From 0 to 6 with step 2
print(num_list[0:7:3])       # From 0 to 6 with step 3

# String case conversions
print(n.lower())
print(n.upper())

# Strip leading and trailing whitespace
n = "  Nitish Choudhary  "
print(n)
print(n.strip())

# Replace and immutability
n = "Naina Roy"
print(n)
print(n.replace("Roy", "Choudhary"))
print(n)  # Original remains unchanged

# Convert string to list
n = "Naina, Nitish, Choudhary, Roy"
print(n.split())         # Default split on whitespace
print(n.split(", "))     # Split on comma + space

# Find substring
n = "Nitish Choudhary"
print(n.find("Choudhary"))   # Index of substring
print(n.find("nitish"))      # Case-sensitive; returns -1 if not found

# Count occurrences
n = "Nitish Choudhary Choudhary Choudhary"
print(n.count("Choudhary"))

# String formatting with placeholders
n_type = "Nitish"
quantity = 2
order = "I meet {} two of {} chy"
print(order)
print(order.format(quantity, n_type))  # Order matters

# Convert list to string
s_list = ["Nitish", "Naina", "Choudhary"]
print(s_list)
print(" ".join(s_list))    # Join with space
print(",".join(s_list))    # Join with comma

# Length of string
n = "Nitish Choudhary"
print(len(n))

# Print each character using loop
for letter in n:
    print(letter)

# Using escape characters
str_quote = "He said, \"Nitish is a good student\""
print(str_quote)

# Raw strings
str_raw = r"Nitish\nChoudhary"
print(str_raw)

str_path = r"c:\user\pwd"
print(str_path)

# Substring existence
n = "Nitish Choudhary"
print("Nitish" in n)     # True
print("Neetish" in n)    # False

