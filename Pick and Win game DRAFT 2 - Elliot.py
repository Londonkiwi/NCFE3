
""" Pick & Win v1.0 © Elliot Smith 12.06.2021.

The purpose of this interactive multiple-choice quiz
is to choose the correct answer from the options
"a", "b" or "c". Any other inputs will return a
pleasant reminder that these options are the only
ones permitted, and the player will be prompted
to try again until they choose one of them.


At start-up, the player will be presented with
game instructions, the rules, and they will be
prompted to accept the latter before gameplay
commences """

# Ask for player name:

name=(input("What’s your name please?: "))

# Assignment of variable to game name:

game=("Pick & Win")

print("\r\n")

# Welcome message and rules:

print("Welcome to the world of",(game),",",(name),"!!","\r\n")

print("Your mission, should you decide to accept it, is to answer multiple-choice questions.","\r")

print("Each question only has one correct answer, and you can only choose from the options \"a\",\"b\" or \"c\" - free-text entries will not be accepted.","\r\n")

print("Googling is not permitted please!","\r\n")

resp=(str(input("Are you happy to play the game with these rules?: ")))

print("\r\n")

# Request for confirmation of willingness to play by the rules, and error capture therefore:

while resp != "y" and resp != "Y" and resp != "N" and resp != "n" and resp != "Yes" and resp != "No" and resp !="YES" and resp !="NO":

    resp=(input("Please answer Yes or No: "));
    
    print("\r\n")
    
    continue

if resp == "N" and resp == "n" and resp == "No" and resp =="NO":
        
    print("Sad to see you go",(name),".", "We hope to see you next time!!","\r\n")
    
if resp == "Y" and resp == "y" and resp == "Yes" and resp =="YES":
    
    print("Let's play then!","\r\n")
    
round_selection=(int(input("You can enjoy a three-round or five-round game today - what'll it be?: ")))

print("\r\n")

# Below - unsure how to get this round_selection variable to compare to an integer for conditional statement - keep getting the message "syntax error"

while True :
    
# Ask user if they are happy to follow the rules

    number = input("How many rounds would you like to play? [3 or 5]")

    if number == "3" or number == "5" :
            
        return number
        
    elif (type(number) == int or float):
            
        print("Please enter a value of 3 or 5 rounds")
        
    else:
        
        # Invalid Response, Retry
        
        print("Please enter a numeric response")

        return ("Off we go then! ", "\r\n")


# Definition of function, and creation of sets of questions and answers in Lists:

def main():

    import random

    questions=["What is the capital of Mongolia?","What is the biggest city in France?", "What is the largest country by land area?","Which is the tallest mountain in the UK?", "Where are piranhas found?", "What causes frost?", "What are the two official languages of Canada?", "What are the two official languages of New Zealand?", "Who is the Prime Minister of the UK, as of 12 June 2021?", "Which is the southernmost continent?"]

    random.shuffle(questions)

    answer_choices=["a)Beijing\nb)Ulaan Bator\nc)Delhi\n:",":",
                      
                          "a)Marseille\nb)Edinburgh\nc)Paris\n:",":",
                          
                          "a)Canada\nb)Russia\nc)China\n:",":"
                          
                          "a)Mt Snowdon\nb)Ben Nevis\nc)Primrose Hill\n:",":"
                          
                          "a)River Thames\nb)Rhine River\nc)Amazon River\n:",":"
                          
                          "a)Rain\nb)Snow\nc)Condensation of water vapour\n:",":"
                          
                          "a)Swahili and German\nb)Polish and German\nc)English and French\n:",":"
                          
                          "a)Portuguese and Welsh\nb)English and Maori\nc)Turkish and Armenian\n:",":"
                          
                          "a)Bozo the Clown\nb)Theresa May\nc)Boris Johnson\n:",":"
                          
                          "a)Snowdonia\nb)Westeros\nc)Antarctica\n:",":"]

    correct_choices=[{"a", "Ulaan Bator"},
                       {"c", "Paris"},
                           {"b", "Russia"},
                           {"b", "Ben Nevis"},
                           {"c", "Amazon River"},
                           {"c", "Condensation of water vapour"},
                           {"c", "English and French"},
                           {"b", "English and Maori"},
                           {"c", "Boris Johnson"},
                           {"c", "Antarctica"}]
                           
    answers=["The capital of Mongolia is Ulaan Bator",
                   "The biggest city in France is Paris",
                   "The largest country by land area is Russia",
                   "The tallest mountain in the UK is Ben Nevis",
                   "Piranhas are found in the Amazon River",
                   "Frost is caused by condensation of water vapour",
                   "The two official languages of Canada are English and French"
                   "The two official languages of New Zealand are English and Maori",
                   "The Prime Minister of the UK as of 12 June 2021 is Boris Johnson",
                   "The southermost continent is Antarctica"]

        # Definition of function for the quiz
             
def quiz():
    score = 0
            
    for questions, answer_choices, correct_choices, answers in zip(questions, answer_choices, correct_choices, answers):
        print(questions)
        user_answer = input(answer_choices).lower()
        
# Score augmentation if input matches correct answer:

    if user_answer in correct_choices:
        print("Congrats",(name),"!","You got 10 points!!")
    score += 10
    
    if user_answer not in correct_choices:
        print(("Aww, what a shame. That wasn't the correct answer", "You got 0 points",(name),"!"))
    score += 0
        
# Announcement of winning score:

    if score == 40:
    
        print("Bravo bravo",(name),"!", "You've won the round!")
    
    if score < 40:
        
        print("Oh dear. So close and yet so far. Good luck next time (name)!", "\r\n")
 
 # Query as to whether player would like to play again:

replay_ques=(input("\033[1m" + "Would you like to play again?: "))

        # Error handling for incorrect input:

while replay_ques != "y" and replay_ques != "Y" and replay_ques != "N" and replay_ques != "n" and replay_ques != "Yes" and replay_ques != "No" and replay_ques !="YES" and replay_ques !="NO":

    replay_ques=(input("Please answer Yes or No: "))
            
    print("\r\n")
            
    continue

# Ending game upon request of player

if replay_ques == "N" and replay_ques == "n" and replay_ques == "No" and replay_ques == "NO":
                
    print("Thank you for playing",(game),".", "See you next time!!","\r\n")
            
    quit()
            
            # Starting game again with previous round selection:
            
if replay_ques == "Y" and replay_ques == "y" and replay_ques == "Yes" and replay_ques == "YES":
            
    main()