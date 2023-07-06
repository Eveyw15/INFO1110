'''
Author: Elaine Liu
SID: 520154106
Unikey: yliu8540
'''

import my_module    # call functions in my_module
import judge        # call functions in judge

i = 1   # jump to get the name
name = input("Please enter your name: ")    # get user's name at the first line
if judge.is_name(name):     # judge whether the input is a name
    i = 2   # jump to get the age
else:
    print("Error: Only accept alphabetical characters and spaces for name")

while i < 6:        # get input from user
    if i == 1:      # get name
        name = input("\nPlease enter your name: ")      # print a new line before asking the name again
        if judge.is_name(name):
            i += 1      # move to the next question
        else:
            print("Error: Only accept alphabetical characters and spaces for name")     # remain (i = 1)

    if i == 2:      # get age
        age = input("\nPlease enter your age: ")
        if judge.is_age(age):       # judge whether the input is an age
            i += 1      # move to the next question
        else:
            print("Error: The age is a number between 0 to 110")        # remain (i = 2)

    if i == 3:      # get the sex
        sex = input("\nPlease enter your biological sex (female/male): ")
        if judge.is_sex(sex):       # judge whether the input is male or female
            i += 1      # move to the next question
        else:
            print("Error: Please enter valid input")        # remain (i = 3)

    if i == 4:
        goal = input('''\nWhat do you want to get out of your training? 
    1. Your goal is losing weight
    2. Your goal is to staying calm and relax
    3. Your goal is increasing your heart rate
    4. Your goal is having stronger legs
    5. Your goal is having stronger ABS
    6. Your goal is having stronger shoulders and arms
Choose a number between 1 to 6: ''')
        if judge.is_goal(goal):     # judge whether the input is a goal
            i += 1      # move to the next question
        else:
            print("Error - It can only be a number between 1 to 6")     # remain (i = 4)

    if i == 5:
        day = input("\nHow many days per week you can train: ")
        if judge.is_day(day):       # judge whether the input is a valid day
            i += 1      # End of loop
            print(my_module.training(name, age, sex, goal, day))        # get the output and print it
        else:
            print("Error: It can only be a number between 1 to 7")      # remain (i = 5)