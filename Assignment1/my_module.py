import math     # get math module

def training(nn, aa, ss, gg, dd):       # get final output by getting name, age, sex, goal and day
    i = 1           # variable 'day' in the loop
    dd = int(dd)    # change day from 'str' to 'int'
    aa = int(aa)    # change age from 'str' to 'int'
    gg = int(gg)    # change goal from 'str' to 'int'
    output_training = f'''
Hello {nn}! Here is your training:
-------------------------------------------------------------------------------------
'''                 # define the initial output
    while i <= dd:  # when i is less than the training days
        if i % 2 == 1:  # if odd numbered days
            output_training += f'Day {i}' + schedule_g(gg, aa)   # add the workout from the list of goals
        else:           # if even numbered days
            output_training += f'Day {i}' + schedule_s(aa, ss)   # add the workout from the list of age/sex
        i += 1          # move to the next day
    output_training += f'\nBye {nn}.'       # add 'Bye' at the end
    return output_training                  # return the training table

def schedule_g(goal, age):
    if goal == 1:  # get the set of exercises for "fat loss"
        wg = f'''
Gym workout for fat loss

Plate thrusters ({cal(15, age)} reps x 3 sets)
Mountain climbers ({cal(20, age)} reps x 3 sets)
Box jumps ({cal(10, age)} reps x 3 sets)
Lunges ({cal(10, age)} reps x 3 sets)
Renegade rows ({cal(10, age)} reps x 3 sets)
Press ups ({cal(15, age)} reps x 3 sets)
Treadmill ({cal(10, age)} mins x 3 sets)
Supermans ({cal(10, age)} reps x 3 sets)
Crunches ({cal(10, age)} reps x 3 sets)
-------------------------------------------------------------------------------------
'''                # call cal function to calculate how much reps/mins should be lowered based on the ages
    elif goal == 2:  # get the set of exercises for "stretch and relax"
        wg = f'''
Gym workout for stretch and relax

Quad stretchs ({cal(2, age)} mins x 3 sets)
Hamstring stretchs ({cal(2, age)} mins x 3 sets)
Chest and shoulder stretchs ({cal(2, age)} mins x 2 sets)
Upper back stretchs ({cal(3, age)} mins x 2 sets)
Biceps stretchs ({cal(2, age)} mins x 2 sets)
Triceps stretchs ({cal(2, age)} mins x 3 sets)
Hip flexors ({cal(2, age)} mins x 3 sets)
Calf stretchs ({cal(2, age)} mins x 3 sets)
Lower back stretchs ({cal(2, age)} mins x 3 sets)
-------------------------------------------------------------------------------------
'''
    elif goal == 3:  # get the set of exercises for "high-intensity exercises"
        wg = f'''
Gym workout for high-intensity exercises

Jumping jacks ({cal(20, age)} reps x 4 sets)
Sprints ({cal(20, age)} reps x 3 sets)
Mountain climbers ({cal(20, age)} reps x 4 sets)
Squat jumps ({cal(20, age)} reps x 4 sets)
Lunges ({cal(20, age)} reps x 3 sets)
Crunches ({cal(20, age)} reps x 3 sets)
Treadmill ({cal(15, age)} mins x 2 sets)
Side planks ({cal(15, age)} reps x 3 sets)
Burpees ({cal(15, age)} reps x 3 sets)
-------------------------------------------------------------------------------------
'''
    elif goal == 4:  # get the set of exercises for "strong legs"
        wg = f'''
Gym workout for strong legs

Back squats ({cal(10, age)} reps x 5 sets)
Hip thrusts ({cal(12, age)} reps x 3 sets)
Overhead presses ({cal(10, age)} reps x 5 sets)
Rack pulls ({cal(10, age)} reps x 5 sets)
Squats ({cal(10, age)} reps x 4 sets)
Dumbbell lunges ({cal(10, age)} reps x 3 sets)
Leg curls ({cal(15, age)} reps x 3 sets)
Standing calf raises ({cal(20, age)} reps x 2 sets)
-------------------------------------------------------------------------------------
'''
    elif goal == 5:  # get the set of exercises for "strong ABS"
        wg = f'''
Gym workout for strong ABS

Cross crunchs ({cal(12, age)} reps x 3 sets)
Knee ups ({cal(15, age)} reps x 5 sets)
Hip thrusts ({cal(15, age)} reps x 3 sets)
Mountain climbers ({cal(15, age)} reps x 3 sets)
Vertical hip thrusts ({cal(12, age)} reps x 3 sets)
Bicycles ({cal(15, age)} mins x 2 sets)
Front planks ({cal(15, age)} mins x 3 sets)
Dragon flags ({cal(12, age)} reps x 4 sets)
Reverse crunches ({cal(10, age)} reps x 3 sets)
-------------------------------------------------------------------------------------
'''
    elif goal == 6:  # get the set of exercises for "strong shoulder and arms"
        wg = f'''
Gym workout for strong shoulder and arms

Bench presses ({cal(10, age)} reps x 5 sets)
Triceps dips ({cal(10, age)} reps x 5 sets)
Incline dumbbell presses ({cal(12, age)} reps x 3 sets)
dumbbell flyes ({cal(15, age)} reps x 3 sets)
Triceps extensions ({cal(15, age)} reps x 3 sets)
Pull ups ({cal(10, age)} reps x 5 sets)
Treadmill ({cal(15, age)} mins x 2 sets)
Bent over rows ({cal(10, age)} reps x 5 sets)
Chin ups ({cal(10, age)} reps x 3 sets)
-------------------------------------------------------------------------------------
'''
    return wg

def schedule_s(age, sex):
    if sex == 'male':  # if the user's sex is male
        if age < 18:  # get the set of exercises for "a male younger than 18 years old"
            ws = '''
Gym workout for a male younger than 18 years old

High knees (20 reps x 3 sets)
Squats (10 reps x 3 sets)
Calf raises (10 reps x 3 sets)
Scissor jumps (12 reps x 3 sets)
Burpees (10 reps x 3 sets)
Treadmill (10 mins x 2 sets)
-------------------------------------------------------------------------------------
'''
        elif age >= 18:  # get the set of exercises for "a male at least 18 years old"
            ws = f'''
Gym workout for a male at least 18 years old

Standing biceps curls ({cal(20, age)} reps x 3 sets)
Seated incline curls ({cal(18, age)} reps x 3 sets)
Seated dumbbell presses ({cal(12, age)} reps x 3 sets)
Leg presses ({cal(15, age)} reps x 3 sets)
Bench presses ({cal(10, age)} reps x 4 sets)
Tricep kickbacks ({cal(15, age)} reps x 3 sets)
Hip thrusts ({cal(12, age)} reps x 3 sets)
Seated rows ({cal(10, age)} reps x 4 sets)
-------------------------------------------------------------------------------------
'''                     # call cal function to calculate how much reps/mins should be lowered based on the ages
    elif sex == 'female': # if the user's sex is male
        if age < 18:  # get the set of exercises for "a female younger than 18 years old"
            ws = '''
Gym workout for a female younger than 18 years old

Squats (10 reps x 3 sets)
Crunches (10 reps x 2 sets)
Jumping jacks (10 reps x 3 sets)
Push ups (10 reps x 2 sets)
Burpees (10 reps x 3 sets)
Treadmill (10 mins x 2 sets)
-------------------------------------------------------------------------------------
'''
        elif age >= 18:   # get the set of exercises for "a female at least 18 years old"
            ws = f'''
Gym workout for a female at least 18 years old

Lateral raises ({cal(15, age)} reps x 3 sets)
Reverse flyes ({cal(12, age)} reps x 3 sets)
Hip thrusts ({cal(12, age)} reps x 3 sets)
Incline dumbbell presses ({cal(15, age)} reps x 3 sets)
Squats ({cal(10, age)} reps x 4 sets)
Dumbbell lunges ({cal(10, age)} reps x 3 sets)
Leg presses ({cal(12, age)} reps x 3 sets)
Dumbbell presses ({cal(10, age)} reps x 4 sets)
-------------------------------------------------------------------------------------
'''
    return ws

def cal(x, a):
    if a <= 60:         # if user's age is less than 60 years old,
        ans = x         # the intensity of the workouts remains the same
    elif a <= 65:       # if user's age ∈ [60, 65]
        ans = math.ceil(x * (1 - (a - 60) / 100))
    elif a <= 75:       # if user's age ∈ [65, 75]
        ans = math.ceil(x * (1 - (5 + 2 * (a - 65)) / 100))
    elif a <= 80:       # if user's age ∈ [75, 80]
        ans = math.ceil(x * (1 - (25 + 3 * (a - 75)) / 100))
    elif a <= 90:       # if user's age ∈ [80, 90]
        ans = math.ceil(x * (1 - (40 + 4 * (a - 80)) / 100))
    else:               # the intensity of the exercise is reduced to the maximum(80%)
        ans = math.ceil(x * 0.2)
    return ans