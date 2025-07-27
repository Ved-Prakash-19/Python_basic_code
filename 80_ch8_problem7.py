# Q. write a python functions to remove a given word from a list ad strip it at the same time.

def remove_and_strip(word_list, word_to_remove):
    # Strip whitespace and remove the word to remove
    return [word.strip() for word in word_list if word.strip() != word_to_remove]

# Example usage
words = ["  Gaurav  ", " Ved ", " python  ", "Dev prakash", "  world  "]
word_to_remove = "world"

result = remove_and_strip(words, word_to_remove)
print(result)  
