#import python components
import json
import string
import random
import nltk


def remove_punctuation(input_string):
    """Converts an input string into a string without punctuation 
    
    Parameters
    ----------
    input_string: String
        string to remove punctuation of 
        
    Returns
    -------
    out_string: string
        string without punctuations 
    """
    
    out_string = ""
    
    for char in input_string:
        if char not in string.punctuation:
            out_string += char
    
    return out_string



def prepare_text(input_string):
    """Converts a string into a string with all lowercase characters, no punctuation, and is splits terms into a list 
    
    Parameters
    ----------
    input_string: string
        string to convert 
        
    Returns
    -------
    out_list: list
        list without punctuations, lowercase, and split into a list 
    """
    
    temp_string = input_string.lower()
    temp_string = remove_punctuation(temp_string)
    out_list = temp_string.split()
    
    return out_list



def store_advice(advice):
    """Takes the user input beginning with "for later:", stores the phrase in the advice.json file, and provides an output
       statement for the user to see it's been stored.
    
    Parameters
    ----------
    input_string: user input string
        function checks for string starting with "for later:" and stores the phrase that follows in the json file. 
        
    Returns
    -------
    output: string
        string to verify to user that their phrase has been stored. 
    """
    
    output = None
    
    fixed_advice = advice.lower()
    
    #checks for starting with the term "for later:"
    if fixed_advice.startswith("for later:"):
        try:
            with open('advice.json', 'r') as file: #calls on json file
                data = json.load(file)
        #error reading, creates new array of advice
        except (FileNotFoundError, json.JSONDecodeError): 
            data = {'advice': []} 
        
        data['advice'].append(advice)
        
        #opens json file with parameter 'w' to write in it
        with open('advice.json', 'w') as file:
            json.dump(data, file, indent=2) 
        
        output = "awesome! i'll remember that for you later"
    
    return output



def output_advice(request, advice_file = 'advice.json'):
    """Takes the user input "share my wise words" and will output a randomly selected phrase from the strings stored in the 
       json file.
    
    Parameters
    ----------
    request: will look for the string "share my wise words".
        this input will set off the function to run
    advice_file: default set to advice.json as it is the main file to store the user advice inputs
    """
    
    try:
        #opens json file with perameter 'r' to read it
        with open(advice_file, 'r') as file: 
            data = json.load(file)
    #error reading, outputs string to notify user that nothing exists in their file yet
    except (FileNotFoundError, json.JSONDecodeError):
            return 'you have not shared any wise words yet. please input them first.'
        
    user_input = request.lower()
    
    if user_input.startswith('share my wise words'):
        random_advice = random.choice(data['advice'])
        random_advice = random_advice[random_advice.index(":") + 2:]
        return random_advice
        
    

def selector(input_list, check_list, return_list):
    """randomly selects a response for a given list of possible inputs
    
    Parameters
    ----------
    input_list: user input list
    check_list: the list of possible inputs to be checked
    return_list: the list of possible outputs to be returned
        
    Returns
    -------
    output: randomly selected string from the return_list   
    """
    
    output = None
    
    for element in input_list:
        if element in check_list:
            output = random.choice(return_list)
            break
    
    return output
    


def end_chat(input_string):
    """prompt to stop the chat with the bot, ending the infinite loop
    
    Parameters
    ----------
    input_string: user input the string "quit"
        
    Returns
    -------
    output: boolean
        sets the function to True
    """
    new_string = input_string.lower()
    
    if new_string == 'quit':
        output = True
    else:
        output = False
    
    return output
    
  