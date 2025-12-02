
from time import sleep

def print_text_list(text_list: list):
    for text, pause in text_list:
        print(text,end="",flush=True)
        sleep(pause)

def make_choice(question: str) -> str:
    answer = input(question).lower()
    return answer

def scene(question: str, text_list: list):

    valid_answers = ["y","yes","n","no"]

    while (answer := make_choice(question)) not in valid_answers:
        print("Please enter \"yes\" or \"no\"")
    else:
        
        if answer == valid_answers[0] or answer == valid_answers[1]:
            print_text_list(text_list)
            input("\nPress enter to continue... ")
            return "y"
            
        elif answer == valid_answers[2] or answer == valid_answers[3]:
            print("you wake up")
            input("\nPress enter to continue... ")
            return "n"

def main():
    #variables
    something = True

    #lists
    opening_text = [
        ("You wake up from a terrible dream where you're working 25 hour shifts at Arby's to afford food for yourself.",1.5),
        ("\n\"Wait",1.2),
        (".",1.2),
        (".",1.2),
        (".\"",1.5),
        ("\nYou realize that you're face-down at the table in the employee lounge.\n",1.5)
        ]
    bed_text = [
        ("You fall into an even deeper slumber...",1.5),
        ("\nDuring your peaceful rest you think you hear someone talking to your parents.",1.5),
        ("\nSomething about",1),
        (".",1),
        (".",1),
        (".",1.5),
        ("\nOverworking?",1.5),
        ("\nMalnutrition?",1.7),
        ("\nWhatever.",1.7),
        ("\nNone of those things matter to you anymore.",1.7),
        ("\nAt least you can finally get some quality sleep...",0)
        ]
    
    #code stuff
    print_text_list(opening_text)
    
    path = scene("\nWould you like to go back to sleep? (y/n)\n",bed_text)
    if path == "y":
        print("\nyour did it")
    else:
        print("\nyour didn't do it")
    
   
    
main()
