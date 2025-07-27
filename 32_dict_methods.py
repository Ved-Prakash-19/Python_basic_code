marks = {
    "ved prakash": 100,
    "gaurav": 80,
    "sachin": 90,
    "monu": 100,
    "list": [1,5,9]
}
print(marks.items())
print(marks.keys())
print(marks.values())

print(marks.get("gaurav"))     #if we used marks.get then output is none.
print(marks["gaurav"])         #if we used square bracket syntax then error.if keys     does not exist in the pair of dictionary.

marks.update({"ved prakash":95, "juhi":100})
print(marks)      # This is the real example of python dictionary is mutable. it means it is changed.         

# some more methods of dictionary in python.

dict.clear()
# Removes all the elements from the dictionary.
my_dict.clear()

dict.copy()
# Returns a shallow copy of the dictionary.
new_dict = my_dict.copy()

dict.fromkeys #(seq[, value])
# Creates a new dictionary from a given sequence seq, with all keys set to a specified value (default is None).
keys = ['a', 'b', 'c']
new_dict = dict.fromkeys(keys, 0)

dict.get #(key[, value])
# Returns the value of the specified key. If the key does not exist, it returns the specified default value (or None if not specified).
value = my_dict.get('key', 'default_value')

dict.items()
# Returns a view object containing the key-value pairs (tuples) of the dictionary.
for key, value in my_dict.items():
    print(key, value)

dict.keys()
# Returns a view object containing the dictionary’s keys.
keys = my_dict.keys()

dict.pop #(key[, default])
# Removes and returns the value for the specified key. If the key is not found, the default value is returned (or KeyError if no default is provided).
value = my_dict.pop('key', 'default_value')

dict.popitem()
# Removes and returns the last inserted key-value pair as a tuple.
key, value = my_dict.popitem()

dict.setdefault #(key[, default])
# Returns the value of the specified key. If the key does not exist, it inserts the key with the specified default value.
my_dict.setdefault('key', 'default_value')

dict.update([other])
# Updates the dictionary with elements from another dictionary or an iterable of key-value pairs.
my_dict.update({'new_key': 'new_value'})

dict.values()
# Returns a view object containing the dictionary’s values.
values = my_dict.values()