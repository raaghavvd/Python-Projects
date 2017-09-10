import json
from difflib import get_close_matches
data= json.load(open("data.json"))
keys= data.keys()
def dict_fun(val):

    if val in data:

        return data[val]

    elif len(get_close_matches(val,keys))>0:

        wm = get_close_matches(val,keys)[0]
        print("The value entered by you isn't correct, the closest word match is..%s " % wm)
        confirm_input= input("Is this what you wanted to enter ? (Y/N)")
        if confirm_input.lower() == 'y':
            return data[wm]
        else:
            return " Re-enter the word"






    else:

        return "It doesn't exist. Try again"






val= input("Enter the word: ")

output= dict_fun(str.lower(val))
if type(output)== list:
    for i in output:
        print (i)
else:
    print(output)
