a = (1, 45, 18, 33, 4141, False, 93, 45, "rohit")
print(a)

i = a.index(45)
print(i)            #o/p -1 b/c 1 one mil jane ke baad aage find nahi karega  

b = a.count(45)
print(b)

i = a.index(4141)
print(i)

# len()
# Description: Returns the length (number of elements) of the tuple.
t = (1, 2, 3, 4)
print(len(t))  # Output: 4


# count()
# Description: Returns the number of times a specified value appears in the tuple.
t = (1, 2, 3, 2, 2, 4)
print(t.count(2))  # Output: 3


# index()
# Description: Returns the index of the first occurrence of a specified value.
t = (1, 2, 3, 4)
print(t.index(3))  # Output: 2


# tuple Unpacking
# Description: You can assign elements of a tuple to variables.
t = (1, 2, 3)
a, b, c = t
print(a, b, c)  # Output: 1 2 3


# in operator
# Description: Used to check if a value is present in the tuple.
t = (1, 2, 3, 4)
print(2 in t)  # Output: True


# + operator (Concatenation)
# Description: Concatenates two or more tuples.
t1 = (1, 2, 3)
t2 = (4, 5, 6)
concantenated = t1+t2
print(concantenated)  # Output: (1, 2, 3, 4)


# * operator (Repetition)
# Description: Repeats the tuple a specified number of times.
t = (1, 2, 3)
repeated = t*3
print(repeated)  # Output: (1, 2, 1, 2, 1, 2)


# 8. min() and max()
# Description: Returns the minimum and maximum values from the tuple.
t = (1, 2, 3, 4)
print(min(t))  # Output: 1
print(max(t))  # Output: 4


# 9. sorted()
# Description: Returns a sorted list of the elements in the tuple (it doesn’t modify the original tuple).
t = (3, 1, 2)
print(sorted(t))  # Output: [1, 2, 3]