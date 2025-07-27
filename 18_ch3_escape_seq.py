a = "ved prakash is a good boy \nbut not so \"good\" "

print(a)


# NOTES :- 

# In Python, escape sequences are used to represent certain special characters within a string. Here are the most commonly used escape sequences:

# 1. \\n (Newline)
# Inserts a new line.
# Example:
print("Hello\nWorld")
# Output:
# Hello
# World


# 2. \\t (Tab)
# Inserts a horizontal tab.
# Example:
print("Hello\tWorld")
# Output: Hello   World


# 3. \\\' (Single Quote)
# Inserts a single quote character within a string.
# Example:
print('It\'s a sunny day')
# Output: It's a sunny day


# 4. \\\" (Double Quote)
# Inserts a double quote character within a string.
# Example:
print("He said, \"Hello!\"")
# Output: He said, "Hello!"


# 5. \\\\ (Backslash)
# Inserts a backslash character.
# Example:
print("This is a backslash: \\")
# Output: This is a backslash: \
    
    
# 6. \\r (Carriage Return)
# Moves the cursor to the beginning of the line (overwriting subsequent text).
# Example:
print("Hello\rWorld")
# Output: World


# 7. \\b (Backspace)
# Removes the previous character (backspace).
# Example:
print("Helloo\b World")
# Output: Hello World


# 8. \\f (Form Feed)
# Inserts a form feed (used in some text processing systems).
# Example:
print("Hello\fWorld")


# 9. \\v (Vertical Tab)
# Inserts a vertical tab.
# Example:
print("Hello\vWorld")


# 10. \\uXXXX (Unicode Character)
# Represents a Unicode character using a 16-bit hexadecimal code.
# Example:
print("\u03A9")
# Output: Ω (Greek letter Omega)


# 11. \\UXXXXXXXX (Unicode Character with 32-bit code)
# Represents a Unicode character using a 32-bit hexadecimal code.
# Example:
print("\U0001F600")
# Output: 😀 (Unicode emoji for smiley face)


# 12. \\xXX (ASCII Character)
# Represents an ASCII character using a 2-digit hexadecimal code.
# Example:
print("\x41")
# Output: A (ASCII value for 'A' is 65, which is 41 in hex)


# 13. \\a (Bell or Alert)
# Makes a sound (bell alert) in some systems.
# Example:
print("\a")