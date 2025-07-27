s = {1, 5, 33, 45, 5, 5, 5, "gaurav"}
print(s, type(s))

s.add(455)
print(s, type(s))


# Important sets methods in python.
set.add(elem)
# Adds an element to the set. If the element is already present, it doesn't add it again (as sets do not allow duplicates).
my_set = {1, 2, 3}
my_set.add(4)

2. set.update(iterable)
# Updates the set, adding elements from another set or any iterable (list, tuple, etc.).
my_set.update([4, 5, 6])

3. set.remove(elem)
# Removes the specified element from the set. Raises a KeyError if the element is not found.
my_set.remove(2)

4. set.discard(elem)
# Removes the specified element from the set. Unlike remove(), it doesn’t raise an error if the element is not found.
my_set.discard(5)

5. set.pop()
# Removes and returns a random element from the set. Raises KeyError if the set is empty.
my_set.pop()

6. set.clear()
# Removes all elements from the set.
my_set.clear()

7. set.union(*sets)
# Returns a new set containing all elements from the set and all other sets (union operation).
set1 = {1, 2, 3}
set2 = {3, 4, 5}
result = set1.union(set2)
# result: {1, 2, 3, 4, 5}

8. set.intersection(*sets)
# Returns a new set containing only the elements that are common to all sets (intersection operation).
result = set1.intersection(set2)
# result: {3}

9. set.difference(*sets)
# Returns a new set containing elements that are in the set but not in any of the others (difference operation).
result = set1.difference(set2)
# result: {1, 2}

10. set.symmetric_difference(other)
# Returns a new set containing elements that are in either of the sets but not in both (symmetric difference).
result = set1.symmetric_difference(set2)
# result: {1, 2, 4, 5}

11. set.issubset(other)
# Returns True if all elements of the set are present in the other set.
set1.issubset(set2)

12. set.issuperset(other)
# Returns True if the set contains all elements of the other set.
set1.issuperset(set2)

13. set.isdisjoint(other)
# Returns True if the two sets have no elements in common.
set1.isdisjoint(set2)

14. set.copy()
# Returns a shallow copy of the set.
new_set = my_set.copy()