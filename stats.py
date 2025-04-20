def count_words(text):
    words = text.split()
    return len(words)

def count_characters(text):
    character_dict = {}
    for char in text:
        char_lower = char.lower()
        if char_lower in character_dict:
            character_dict[char_lower] += 1
        else:
            character_dict[char_lower] = 1
    return character_dict

def ordered_dict(character_dict):
    # Create an empty list to store dictionaries
    char_list = []
    
    # Loop through the character dictionary and create a new dictionary for each character
    for char, count in character_dict.items():
        # What should each dictionary in the list contain?
        # Hint: It needs a key for the character and a key for the count
        char_info = {"character": char, "count": count}
        char_list.append(char_info)
    
    # Now we need to sort the list based on the count value
    # We can use the hint from the instructions about using .sort()
    
    # Define a helper function that returns the value to sort by
    def sort_on(dict):
        return dict["count"]
    
    # Sort the list in descending order (reverse=True)
    char_list.sort(reverse=True, key=sort_on)
    
    # Return the sorted list
    return char_list