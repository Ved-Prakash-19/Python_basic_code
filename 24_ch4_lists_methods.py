friends = ["apple", "orange", "5", "345.6", "false", "gaurav", "ved prakash"]
print(friends)

friends.append("juhu")
print(friends)

l1 = [1, 34, 62, 2, 6, 11]
l1.sort()
print(l1)

l1.append("45")
print(l1)

l1.reverse()
print(l1)          #this print value is return value of l1.reverse


l1 = [1, 34, 62, 2, 6, 11]
l1.insert(3,18)    #insert 18 such that its index in the place of list 3.
print(l1)


l1 = [1, 34, 62, 2, 6, 11]
value = l1.pop(2)
print(value)
print(l1)


l1 = [1, 34, 62, 2, 6, 11]
l1.remove(62)
print(l1)


#notes:--
# extend(iterable)
my_list = [1, 2, 3]
my_list.extend([4, 5])
print(my_list)  # Output: [1, 2, 3, 4, 5]


# clear()
my_list = [1, 2, 3]
my_list.clear()
print(my_list)  # Output: []


# index(item, start, end)
my_list = [1, 2, 3, 2]
print(my_list.index(2))  # Output: 1


# count(item)
my_list = [1, 2, 2, 3]
print(my_list.count(2))  # Output: 2


# sort(key=None, reverse=False)
my_list = [3, 1, 2]
my_list.sort()
print(my_list)  # Output: [1, 2, 3]


# copy()
my_list = [1, 2, 3]
new_list = my_list.copy()
print(new_list)  # Output: [1, 2, 3]


