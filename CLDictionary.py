import json
import difflib

# import our dataset as a variable named "data"
data = json.load(open("/Users/User/Desktop/PythonPrograms/data.json"))

# main function to search through dictionary after user specifies the word
def translate(w):
    w = w.lower() # format user input. 
    
    if w in data:
        return data[w]
    elif w.title() in data: # incase user enters "Texas" or "Paris"
        return data[w.title()]
    elif w.upper() in data: # incase user enters "USA" or "NATO"
        return data[w.upper()]
   
    # if user misspells, get close matches and check for confirmation
    elif len(difflib.get_close_matches(w, data.keys())) > 0:
        # ask yes or no, did they mean ". . ." instead? wait for a yes or no response.
        yn = input("Did you mean %s instead? Enter y/n: " % difflib.get_close_matches(w, data.keys())[0])
        if yn == "y":
            return data[difflib.get_close_matches(w, data.keys())[0]]
        elif yn == "n":
            return "The word doesn't exist. Please double check it."
        else:
            return "We didn't understand your entry"
   
    # if no word is found, report error
    else:
        return "The word doesn't exist. Please double check it."

# ask for the user's word
word = input("Enter word: ")

# get corresponding data from dictionary
output = translate(word)

# print the output cleanly
if type(output) == list:
    for item in output:
        print(item)
else:
    print(output)
