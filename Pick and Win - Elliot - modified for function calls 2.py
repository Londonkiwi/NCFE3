""" Pick & Win v1.0 © Elliot Smith 05.07.2021. All rights reserved.

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

# Request for confirmation of willingness to play by the rules, and error capture thereof:


while resp != "y" and resp != "Y" and resp != "N" and resp != "n" and resp != "Yes" and resp != "No" and resp !="YES" and resp !="NO":

    resp=(input("Please answer Yes or No: "));
    
    print("\r\n")
    
    continue

if resp == "Y" and resp == "y" and resp == "Yes" and resp =="YES":
    
    print("Let's play then!","\r\n")
    
if resp == "N" and resp == "n" and resp == "No" and resp =="NO":
        
    print("Sad to see you go",(name),".", "We hope to see you next time!!","\r\n")

    quit()


# Definition of new function "quiz_main_3" and variable "newList_3" for three-round game:


def quiz_main_3():


    questions_3=["What is the capital of Mongolia?","What is the biggest city in France?", "What is the largest country by land area?","Which is the tallest mountain in the UK?", "Where are piranhas found?", "What causes frost?", "What are the two official languages of Canada?", "What are the two official languages of New Zealand?", "Who is the Prime Minister of the UK, as of 12 June 2021?", "Which is the southernmost continent?"];

     
    # Old (full) list of questions:

    # newList3=[questions[0]+answer_choices[0],questions[1]+answer_choices[1],questions[2]+answer_choices[2],questions[3]+answer_choices[3],questions[4]+answer_choices[4],questions[5]+answer_choices[5],questions[6]+answer_choices[6],questions[7]+answer_choices[7],questions[8]+answer_choices[8],questions[9]+answer_choices[9]]

    # Variables "answers_choices" and "correct_choices" renamed to reflect number of rounds being played:

    answer_choices_3=["\na)Beijing\nb)Ulaan Bator\nc)Delhi",
                    "a)\nMarseille\nb)Edinburgh\nc)Paris",
                    "a)\nCanada\nb)Russia\nc)China",
                    "a)\nMt Snowdon\nb)Ben Nevis\nc)Primrose Hill",
                    "a)\nRiver Thames\nb)Rhine River\nc)Amazon River",
                    "a)\nRain\nb)Snow\nc)Condensation of water vapour",
                    "a)\nSwahili and German\nb)Polish and German\nc)English and French",
                    "a)\nPortuguese and Welsh\nb)English and Maori\nc)Turkish and Armenian",
                    "a)\nBozo the Clown\nb)Theresa May\nc)Boris Johnson",
                    "a)\nSnowdonia\nb)Westeros\nc)Antarctica"];

    correct_choices_3=["a","c","b","b","c","c","c","b","c","c"];
 
    # To prevent NameErrors, moved definition of the new variable "newList_3" to the end of the (new) function "quiz_main_3" (for a three-round game):

    newList_3=[questions_3[0]+answer_choices_3[0],questions_3[1]+answer_choices_3[1],questions_3[2]+answer_choices_3[2]];
  

    # Commenting out of old variable "newList":

    # newList=[questions[0]+answer_choices[0],questions[1]+answer_choices[1],questions[2]+answer_choices[2],questions[3]+answer_choices[3],questions[4]+answer_choices[4],questions[5]+answer_choices[5],questions[6]+answer_choices[6],questions[7]+answer_choices[7],questions[8]+answer_choices[8],questions[9]+answer_choices[9]]

    # Definition of new function "quiz_main_5" and variable "newList_5" for five-round game:

def quiz_main_5():

    # Variable "questions" renamed to reflect number of rounds being played:

    questions_5=["What is the capital of Mongolia?","What is the biggest city in France?", "What is the largest country by land area?","Which is the tallest mountain in the UK?", "Where are piranhas found?", "What causes frost?", "What are the two official languages of Canada?", "What are the two official languages of New Zealand?", "Who is the Prime Minister of the UK, as of 12 June 2021?", "Which is the southernmost continent?"];
          
    # Old (full) list of questions: newList3=[questions[0]+answer_choices[0],questions[1]+answer_choices[1],questions[2]+answer_choices[2],questions[3]+answer_choices[3],questions[4]+answer_choices[4],questions[5]+answer_choices[5],questions[6]+answer_choices[6],questions[7]+answer_choices[7],questions[8]+answer_choices[8],questions[9]+answer_choices[9]]
        
    # Variable "answers_choices" and "correct_choices" renamed to reflect number of rounds being played:
    
    answer_choices_5=["\na)Beijing\nb)Ulaan Bator\nc)Delhi",
                    "a)\nMarseille\nb)Edinburgh\nc)Paris",
                    "a)\nCanada\nb)Russia\nc)China",
                    "a)\nMt Snowdon\nb)Ben Nevis\nc)Primrose Hill",
                    "a)\nRiver Thames\nb)Rhine River\nc)Amazon River",
                    "a)\nRain\nb)Snow\nc)Condensation of water vapour",
                    "a)\nSwahili and German\nb)Polish and German\nc)English and French",
                    "a)\nPortuguese and Welsh\nb)English and Maori\nc)Turkish and Armenian",
                    "a)\nBozo the Clown\nb)Theresa May\nc)Boris Johnson",
                    "a)\nSnowdonia\nb)Westeros\nc)Antarctica"];

    correct_choices_5=["a","c","b","b","c","c","c","b","c","c"];

    # To prevent NameErrors, moved definition of the new variable "newList_5" to the end of the (new) function "quiz_main_5" (for a three-round game):
    
    newList_5=[questions_5[3]+answer_choices_5[3],questions_5[4]+answer_choices_5[4],questions_5[5]+answer_choices_5[5],questions_5[6]+answer_choices_5[6],questions_5[7]+answer_choices_5[7]];


# Randomisation and shuffling of question and answer sets

import random

""" Definition of new variable "AI_question_3" for three round game, and definition of variable "AI_question_3" for randomisation for three-round game: """

def question_randomisation_3():

    AI_question_3=random.choice(newList_3);
    
    random.shuffle(AI_question_3)
    
    print(AI_question_3)

    pos_AI_ques=int(newList_3.index(AI_question_3));
    
# Answer input variable renamed from "answer_input" to "answer_input_3" to reflect number of rounds:

    answer_input_3=input("\nEnter your answer: ")
    
               
    # Definition of new variable "AI_question_5" for randomisation for a five round game:

def question_randomisation_5():
    
    AI_question_5=random.choice(newList_5);
    
    random.shuffle(AI_question_5)
    
    print(AI_question_5)
   
    # Answer input variable renamed from "answer_input" "answer_input_5" to reflect number of rounds:

    answer_input_5=input("\nEnter your answer: ");
    
    pos_AI_ques=int(newList_5.index(AI_question_5));

    answers=["The capital of Mongolia is Ulaan Bator",
         "The biggest city in France is Paris",
         "The largest country by land area is Russia",
         "The tallest mountain in the UK is Ben Nevis",
         "Piranhas are found in the Amazon River",
         "Frost is caused by condensation of water vapour",
         "The two official languages of Canada are English and French"
         "The two official languages of New Zealand are English and Maori",
         "The Prime Minister of the UK as of 12 June 2021 is Boris Johnson",
         "The southernmost continent is Antarctica"];

def round_selection(number_choice):


    number_choice=input(str("You can enjoy a three-round or five-round game today - what'll it be?: "));

    print("\r\n")

    # Call the appropriate function for the number of rounds desired:

    if number_choice == "3":
    
    # Calls function for three-round game:

        question_randomisation_3()

    if number_choice == "5":

    # Calls function for three-round game:

        question_randomisation_5()

    # Commenting out of redundant else statement:

    # else:
    #     
    #    return False

    while number_choice != "3" and number_choice != "5":

        number_choice=(int(input("Please enter a value of 3 or 5 rounds: ")))
                
        print("\r\n")
        

# Definition of functions for the three-round and five-round quizzes, and modification of variable names to match:
             
def quiz_score_3():
    score = 0
            
    for questions_3, answer_choices_3, correct_choices_3, answers_3 in zip(questions_3, answer_choices_3, correct_choices_3, answers_3):
        print(questions_3)
        answer_input_3=input(answer_choices_3).lower();
        
# Score accumulation if input matches correct answer:

    if answer_input_3 in correct_choices_3:
        print("Congrats",(name),"!","You got 10 points!!")
    score += 10
    
    if user_answer_3 not in correct_choices_3:
        print(("Aww, what a shame. That wasn't the correct answer", "You got 0 points",(name),"!"))
    score += 0
        
# Announcement of winning score:

    if score == 40:
    
        print("Bravo bravo",(name),"!", "You've won the round!")
    
    if score < 40:
        
        print("Oh dear. So close and yet so far. Good luck next time (name)!", "\r\n")
 
 # Query as to whether player would like to play again:
             
def quiz_score_5():
    score = 0
            
    for questions_5, answer_choices_5, correct_choices_5, answers_5 in zip(questions_5, answer_choices_5, correct_choices_5, answers_5):
        print(questions_5)
        answer_input_5=input(answer_choices_5).lower()
        
# Score accumulation if input matches correct answer:

    if answer_input_5 in correct_choices_5:
        print("Congrats",(name),"!","You got 10 points!!")
    score += 10
    
    if user_answer_5 not in correct_choices_5:
        print(("Aww, what a shame. That wasn't the correct answer", "You got 0 points",(name),"!"))
    score += 0
        
# Announcement of winning score:

    if score == 40:
    
        print("Bravo bravo",(name),"!", "You've won the round!")
    
    if score < 40:
        
        print("Oh dear. So close and yet so far. Good luck next time (name)!", "\r\n")
 
 # Query as to whether player would like to play again:
 
def play_again():

    replay_ques = (input("\033[1m" + "Would you like to play again?: (Yes or No): "));

    replay_ques = replay_ques.upper();


# Error handling for incorrect input:

    while replay_ques != "y" and replay_ques != "Y" and replay_ques != "N" and replay_ques != "n" and replay_ques != "Yes" and replay_ques != "No" and replay_ques !="YES" and replay_ques !="NO":

        replay_ques=(input("Please answer Yes or No: "));
                
        print("\r\n")
            
# Ending game upon request of player

    if replay_ques == "N" and replay_ques == "n" and replay_ques == "No" and replay_ques == "NO":
                
        print("Thank you for playing",(game),".", "See you next time!!","\r\n")
            
    quit()
            
# Starting game again with previous round selection:
            
    if replay_ques == "Y" and replay_ques == "y" and replay_ques == "Yes" and replay_ques == "YES":
            
        round_selection()
