
# Prompt the user to enter a word
word = input("Please enter a word: ")

def stutter(word):
    # Get the first two characters of the word
    first_part = word[:2]
    
    # Create the stuttering effect (e.g., "he... ")
    stutter_part = first_part + "..."
    
    # Repeat the stutter twice and add the full word with a question mark
    result = (stutter_part * 2) + word + "?"
    
    # Return the final result
    return result 

# Call the function and print the result
print(stutter(word))

