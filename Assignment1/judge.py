def is_name(n):     # judge whether 'n' is a name
    i = 0           # i stands the different digits of numbers
    judge = False   # Assume 'n' is not a name
    while i < len(n):       # if i is less than the length of the number
        if n[i].isalpha() or n[i] == ' ':   # if the i-th digit of n is a letter or space (start from 0)
            judge = True    # 'n' is a valid name
        else:
            judge = False   # 'n' is not a valid name
            break           # stop the loop (keep False)
        i += 1
    return judge    # return the judgment result

def is_age(a):      # judge whether 'a' is an age
    if a.isdigit(): # if 'a' is a number
        a = int(a)  # change 'a' from 'str' to 'int'
        if a >= 0 and a <= 110:         # if age ∈ [0, 110]
            return True     # 'a' is a valid age
        else:
            return False    # 'a' is not an age
    else:
        return False        # 'a' is not an age

def is_sex(s):      # judge whether 's' is a sex
    if s == 'female' or s == 'male':    # if sex is the same as 'female' or 'male'
        return True         # 's' is a valid sex
    else:
        return False        # 's' is not a sex

def is_goal(g):     # judge whether 'g' is a goal
    if g.isdigit(): # if 'g' is a number
        g = int(g)  # change 'g' from 'str' to 'int'
        if g >= 1 and g <= 6:           # if goal ∈ [1, 6]
            return True     # 'g' is a valid goal
        else:
            return False    # 'g' is not a goal
    else:
        return False        # 'g' is not a goal

def is_day(d):      # judge whether 'd' is a day
    if d.isdigit(): # if 'd' is a number
        d = int(d)  # change 'd' from 'str' to 'int'
        if d >= 1 and d <= 7:           # if day ∈ [1, 7]
            return True     # 'd' is a valid day
        else:
            return False    # 'd' is not a day
    else:
        return False        # 'd' is not a day