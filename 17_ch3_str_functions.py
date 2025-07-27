str = "gaurav"
print(len(str))

str = "gaurav"
print(str.endswith("rav"))
print(str.startswith("ga"))
print(str.endswith("ga"))



str = "gaurav"
count = str.count("a")
print(count)

str = "gaurav"
capitalized_string = str.capitalize()
print(capitalized_string)

str = "gaurav"
index = str.find("a")
print(index)

str = "gaurav"
replaced_string = str.replace("g","j")
print(replaced_string)



# 1.len()
# Description: Returns the length (number of characters) of a string.
# Example:
s = "Hello"
print(len(s))  # Output: 5


# 2. lower()
# Description: Converts all characters in the string to lowercase.
# Example:
s = "Hello"
print(s.lower())  # Output: "hello"


# 3. upper()
# Description: Converts all characters in the string to uppercase.
# Example:
s = "Hello"
print(s.upper())  # Output: "HELLO"


# 4. strip()
# Description: Removes any leading and trailing whitespace (or specified characters).
# Example:
s = "  Hello  "
print(s.strip())  # Output: "Hello"


# 5. replace()
# Description: Replaces a substring with another substring.
# Example:
s = "Hello World"
print(s.replace("World", "Python"))  # Output: "Hello Python"


# 6. split()
# Description: Splits a string into a list where each word is a list item, based on a specified separator.
# Example:
s = "Hello,World,Python"
print(s.split(","))  # Output: ['Hello', 'World', 'Python']


# 7. join()
# Description: Joins the elements of a list into a single string with a specified separator.
# Example:
lst = ['Hello', 'World', 'Python']
print(" ".join(lst))  # Output: "Hello World Python"


# 8. startswith()
# Description: Checks if a string starts with a specified substring.
# Example:
s = "Hello"
print(s.startswith("He"))  # Output: True


# 9. endswith()
# Description: Checks if a string ends with a specified substring.
# Example:
s = "Hello"
print(s.endswith("lo"))  # Output: True


# 10. find()
# Description: Returns the index of the first occurrence of a substring, or -1 if not found.
# Example:
s = "Hello World"
print(s.find("World"))  # Output: 6


# 11. count()
# Description: Returns the number of occurrences of a substring in the string.
# Example:
s = "Hello World"
print(s.count("l"))  # Output: 3


# 12. isdigit()
# Description: Checks if all characters in the string are digits.
# Example:
s = "12345"
print(s.isdigit())  # Output: True


# 13. isalpha()
# Description: Checks if all characters in the string are alphabetic.
# Example:
s = "Hello"
print(s.isalpha())  # Output: True


# 14. isalnum()
# Description: Checks if all characters in the string are alphanumeric (either letters or numbers).
# Example:
s = "Hello123"
print(s.isalnum())  # Output: True


# 15. capitalize()
# Description: Capitalizes the first character of the string.
# Example:
s = "hello"
print(s.capitalize())  # Output: "Hello"


# 16. title()
# Description: Converts the first character of each word to uppercase.
# Example:
s = "hello world"
print(s.title())  # Output: "Hello World"