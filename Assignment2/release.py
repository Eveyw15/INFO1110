"""
Author: Elaine
SID: 520154106
Unikey: yliu8540
"""
import sys
from datetime import datetime

# Read files
def read(x):
    filename = x
    try:
        file = open(filename, 'r')
        file.close()
    except FileNotFoundError:
        print(f"{filename} cannot be read.")
        sys.exit()

# Get task argument
def task(x):
    ls_task = ["rank_people", "validate_forum", "censor_forum", "evaluate_forum"]
    i = 0
    temp = False
    while i < 4:
        if x == ls_task[i]:
            temp = True
            break
        i += 1
    return temp

# Get Class object
def get_user_list(f_people):
    file_people = open(f_people, 'r')
    people = file_people.readlines()
    user = []
    i = 2
    while i < len(people):
        name = people[i][:-1].split(",")[0]
        score = people[i][:-1].split(",")[1]
        temp = User(name)
        user.append(temp)
        user[i-2].initial_score = int(score)
        i += 1
    return user


# P3: Validating people's name
def is_name(name):
    i = 0
    name = name.strip()
    temp = False
    while i < len(name):
        if name[i].isalpha() or name[i] == ' ' or name[i] == '-':
            temp = True
        else:
            temp = False
            break
        i += 1
    return temp

# P3: Validating the personality score
def is_score(score):
    if score != "":
        if score[0] == "-":
            if score[1:].isdigit():
                score = int(score)
                if score >= -10 and score <= 10:
                    return True
                else:
                    return False
            else:
                return False
        else:
            if score.isdigit():
                score = int(score)
                if score >= -10 and score <= 10:
                    return True
                else:
                    return False
            else:
                return False

    else:
        return False

# P4: Validating the time format
def is_time(time):
    time = datetime.strptime(time, '%Y-%m-%dT%H:%M:%S')
    return time

# P4: Validating the chronological oder
def is_chronological(earlier_dt, later_dt):
    earlier_dt = datetime.strptime(earlier_dt, '%Y-%m-%dT%H:%M:%S')
    later_dt = datetime.strptime(later_dt, '%Y-%m-%dT%H:%M:%S')
    yy1 = earlier_dt.year
    mm1 = earlier_dt.month
    dd1 = earlier_dt.day
    hh1 = earlier_dt.hour
    nn1 = earlier_dt.minute
    ss1 = earlier_dt.second
    yy2 = later_dt.year
    mm2 = later_dt.month
    dd2 = later_dt.day
    hh2 = later_dt.hour
    nn2 = later_dt.minute
    ss2 = later_dt.second
    if yy1 < yy2:
        return True
    elif yy1 == yy2:
        if mm1 < mm2:
            return True
        elif mm1 == mm2:
            if dd1 < dd2:
                return True
            elif dd1 == dd2:
                if hh1 < hh2:
                    return True
                elif hh1 == hh2:
                    if nn1 < nn2:
                        return True
                    elif nn1 == nn2:
                        if ss1 < ss2:
                            return True
                        else:
                            return False
                    else:
                        return False
                else:
                    return False
            else:
                return False
        else:
            return False
    else:
        return False

# P5: Validating the banned words
def is_word(word):
    word = list(word)
    word = word[:-1]
    word = ''.join(word).strip()
    if len(word) != 0:
        return True
    else:
        return False

# P5: Replacing the banned words
def replace(line, word, start):
    line = list(line)
    word = list(word)
    n = len(word)
    line[start:start + n] = '*' * n
    return ''.join(line)


# P3 main function
def rank_people(f_people, f_log):
    file_people = open(f_people, 'r')
    lines = file_people.readlines()
    file_log = open(f_log, "w")
    if lines[0] == "\n":
        file_log.write("Error: people file read. The people file header is incorrectly formatted\n")
        file_log.close()
        sys.exit()
    if lines[1] == "\n":
        i = 0
        name = []
        score = []
        while i < len(lines)-2:
            lines[i+2] = lines[i + 2][:-1]
            try:
                name0 = lines[i + 2].split(',')[0]
                score0 = lines[i + 2].split(',')[1]
            except IndexError:
                file_log.write(f"Error: people file read. The personality score is invalid on line {i + 3}\n")
                file_log.close()
                sys.exit()
            if not is_name(name0):
                file_log.write(f"Error: people file read. The user's name is invalid on line {i+3}\n")
                file_log.close()
                sys.exit()
            if is_score(score0):
                score0 = int(score0)
            else:
                file_log.write(f"Error: people file read. The personality score is invalid on line {i+3}\n")
                file_log.close()
                sys.exit()
            name.append(name0)
            score.append(score0)
            i += 1
        file_people.close()
        m = 0
        while m < i - 1:
            highest = m
            n = m + 1
            while n < i:
                if score[n] >= score[highest]:
                    highest = n
                n += 1
            if m != highest:
                score[m], score[highest] = score[highest], score[m]
                name[m], name[highest] = name[highest], name[m]
            m += 1
        file_people = open(f_people, 'w')
        file_people.write(lines[0])
        file_people.write(lines[1])
        j = 0
        while j < i:
            file_people.write(f"{name[j]},{score[j]}\n")
            j += 1
        file_people.close()
    else:
        file_log.write("Error: people file read. The people file header is incorrectly formatted\n")
        file_log.close()
        file_people.close()
        sys.exit()

# P4 main function
def validate_forum(f_forum, f_log):
    file_forum = open(f_forum, 'r')
    lines = file_forum.readlines()
    file_log = open(f_log, "w")
    if lines[0] == "\n":
        file_log.write("Error: forum file read. The forum file header is incorrectly formatted\n")
        file_log.close()
        sys.exit()
    if lines[1] == "\n":
        i = 0
        while i < (len(lines) - 2)//3:
            if lines[3 * i + 2][0] == '\t': # reply
                if i == 0:  # the reply is placed before a post
                    file_log.write(f"Error: forum file read. The reply is placed before a post on line {3 * i + 3}\n")
                    file_log.close()
                    sys.exit()
                # invalid format
                if lines[3 * i + 3][0] == '\t':
                    if lines[3 * i + 4][0] != '\t':
                        file_log.write(f"Error: forum file read. The post has an invalid format on line {3 * i + 5}\n")
                        file_log.close()
                        sys.exit()
                else:
                    file_log.write(f"Error: forum file read. The post has an invalid format on line {3 * i + 4}\n")
                    file_log.close()
                    sys.exit()
                # invalid datetime
                try:
                    is_time(lines[3 * i + 2][1:-1])
                except Exception:
                    file_log.write(f"Error: forum file read. The datetime string is invalid on line {3 * i + 3}\n")
                    file_log.close()
                    sys.exit()
                # Validating the post before
                if lines[3 * i - 1][0] != '\t': # if the contents before is a post
                    if not is_chronological(lines[3 * i - 1][:-1], lines[3 * i + 2][1:-1]):  # reply before the post
                            file_log.write(f"Error: forum file read. The reply is out of chronological order on line {3 * i + 3}\n")
                            file_log.close()
                            sys.exit()
                else:   # if the contents before is a reply
                    if not is_chronological(lines[3 * i - 1][1:-1], lines[3 * i + 2][1:-1]):  # reply before the post
                            file_log.write(f"Error: forum file read. The reply is out of chronological order on line {3 * i + 3}\n")
                            file_log.close()
                            sys.exit()
            else:   # post
                # invalid format
                if lines[3 * i + 3][0] != '\t':
                    if lines[3 * i + 4][0] == '\t':
                        file_log.write(f"Error: forum file read. The post has an invalid format on line {3 * i + 5}\n")
                        file_log.close()
                        sys.exit()
                else:
                    file_log.write(f"Error: forum file read. The post has an invalid format on line {3 * i + 4}\n")
                    file_log.close()
                    sys.exit()
                try:
                    if i == 0:  # The first post of the forum
                        is_time(lines[3 * i + 2][:-1])
                except Exception:
                    file_log.write(f"Error: forum file read. The datetime string is invalid on line {3 * i + 3}\n")
                    file_log.close()
                    sys.exit()
                # invalid datetime
                try:
                    is_time(lines[3 * i + 2][:-1])
                except Exception:
                    file_log.write(f"Error: forum file read. The datetime string is invalid on line {3 * i + 3}\n")
                    file_log.close()
                    sys.exit()
                j = i - 1
                while j >= 0:
                    if lines[3 * j + 2][0] != '\t':
                        if not is_chronological(lines[3 * j + 2][:-1], lines[3 * i + 2][:-1]):
                            file_log.write(f"Error: forum file read. The post is out of chronological order on line {3 * i + 3}\n")
                            file_log.close()
                            sys.exit()
                    j -= 1
            if not is_name(lines[3 * i + 3][:-1]):
                file_log.write(f"Error: forum file read. The user's name is invalid on line {3 * i + 4}\n")
                file_log.close()
                sys.exit()
            i += 1
        file_forum.close()
    else:
        file_log.write("Error: forum file read. The forum file header is incorrectly formatted\n")
        file_log.close()
        file_forum.close()
        sys.exit()

# P5 main function
def censor_forum(f_forum, f_words, f_log, user):
    file_forum = open(f_forum, 'r')
    lines = file_forum.readlines()
    file_words = open(f_words, 'r')
    words = file_words.readlines()
    file_log = open(f_log, "w")
    file_forum.close()
    file_words.close()
    if words[0] == "\n":
        file_log.write("Error: words file read. The words file header is incorrectly formatted\n")
        file_log.close()
        sys.exit()
    if words[1] == "\n":
        words = words[2:]
        i = 0
        while i < len(words):
            if not is_word(words[i]):
                file_log.write(f"Error: words file read. The banned word is invalid on line {i + 3}\n")
                file_log.close()
                sys.exit()
            i += 1
        i = 0
        while i < (len(lines) - 2)//3:
            line = lines[3 * i + 4]
            p = 0
            while p < len(user):
                if lines[3 * i + 3][0] == "\t":
                    if user[p].name == lines[3 * i + 3][1:-1]:
                        User.process_message(user[p], line, words)
                else:
                    if user[p].name == lines[3 * i + 3][:-1]:
                        User.process_message(user[p], line, words)
                p += 1
            j = 0
            while j < len(line):
                k = 0
                while k < len(words):
                    n = len(words[k][:-1])
                    if str(line[j:j + n]).upper() == str(words[k][:-1]).upper():  # find the words in line that need to be replaced
                        if line[j - 1] == ',' or line[j - 1] == '.' or line[j - 1] == "'" or line[j - 1] != '"' or line[j - 1] == '!' or line[j - 1] == '?' or line[j - 1] == '(' or line[j - 1] == ')' or line[j - 1] == ' ' or line[j - 1] == '\n' or line[j - 1] == '\t':
                            if line[j + n] == ',' or line[j + n] == '.' or line[j + n] == "'" or line[j + n] == '"' or line[j + n] == '!' or line[j + n] == '?' or line[j + n] == '(' or line[j + n] == ')' or line[j + n] == ' ' or line[j + n] == '\n' or line[j + n] == '\t':
                                line = replace(line, words[k][:-1], j)
                                lines[3 * i + 4] = line
                    k += 1
                j += 1
            i += 1
        p = 0
        while p < len(user):
            User.calculate_personality_score(user[p])
            p += 1
        file_forum.close()
        file_forum = open(f_forum, 'w')
        file_forum.writelines(lines)
    else:
        file_log.write("Error: words file read. The words file header is incorrectly formatted\n")
        file_log.close()
        sys.exit()

# P6 main funtion
def evaluate_forum(f_people, f_log, user):
    file_people = open(f_people, 'r')
    f_p = file_people.readlines()
    file_people.close()

    file_people = open(f_people, 'w')
    file_people.write(f_p[0])
    file_people.write(f_p[1])
    j = 0
    while j < len(user):
        score = user[j].show_initial_score() + user[j].show_score()
        if score > 10:
            score = 10
        elif score < -10:
            score = -10
        file_people.write(f"{user[j].name},{score}\n")
        j += 1
    file_people.close()
    rank_people(f_people, f_log)


class User:
    def __init__(self, name):
        self.name = name
        self.engagement = 0
        self.expressiveness = 0
        self.offensiveness = 0
        self.initial_score = 0
        self.score = 0

    def show_score(self):
        return self.score

    def show_initial_score(self):
        return self.initial_score

    def calculate_personality_score(self):
        score = self.expressiveness - self.offensiveness
        if score > self.engagement:
            score = self.engagement
        if score > 10:
            score = 10
        elif score < -10:
            score = -10
        self.score = int(score)
        return self.score


    def process_message(self, message, banned_words):
        if type(message) == str:
            add0 = 0
            add1 = 0
            if message[0] == "\t":
                i = 0
                while i < len(message): # expressiveness
                    if message.find("!") != -1:
                        add0 = 1
                    if message.find("?") != -1:
                        add1 = 1
                    i += 1
                if add0 != 0 and add1 != 0:
                    self.expressiveness += 2.0
                elif add0 != 0 and add1 == 0:
                    self.expressiveness += 1.0
                elif add0 == 0 and add1 ==0:
                    self.expressiveness -= 1.0
                i = 0
                while i < len(banned_words):    # offensiveness
                    find_result = message.lower().find(banned_words[i][:-1])
                    if find_result != -1:
                        self.offensiveness += 1.0
                        break
                    i += 1
                self.engagement += 1.0
            else:
                i = 0
                while i < len(message):  # expressiveness
                    if message.find("!") != -1:
                        add0 = 1
                    if message.find("?") != -1:
                        add1 = 1
                    i += 1
                if add0 != 0 and add1 != 0:
                    self.expressiveness += 3.0
                elif add0 != 0 and add1 == 0:
                    self.expressiveness += 1.5
                elif add0 == 0 and add1 == 0:
                    self.expressiveness -= 1.5
                i = 0
                while i < len(banned_words):    # offensiveness
                    find_result = message.lower().find(banned_words[i][:-1])
                    if find_result != -1:
                        self.offensiveness += 1.5
                        break
                    i += 1
                self.engagement += 1.5
            return True
        else:
            return False




if __name__ == "__main__":
    ls_command = ["task", "log", "forum", "words", "people"]
    command = [0, 0, 0, 0, 0]
    i = 1
    while i < len(sys.argv):
        if sys.argv[i] == "-task":
            op_task = sys.argv[i + 1]
            if not task(op_task):
                print("Task argument is invalid.")
                exit()
            command[0] = 1
        if sys.argv[i] == "-log":
            op_log = sys.argv[i + 1]
            command[1] = 1
        if sys.argv[i] == "-forum":
            op_forum = sys.argv[i + 1]
            command[2] = 1
        if sys.argv[i] == "-words":
            op_words = sys.argv[i + 1]
            command[3] = 1
        if sys.argv[i] == "-people":
            op_people = sys.argv[i + 1]
            command[4] = 1
        i += 2

    i = 0
    while i < 5:
        if command[i] == 0:
            print(f"No {ls_command[i]} arguments provided.")
            exit()
        i += 1

    read(op_forum)
    read(op_words)
    read(op_people)
    print("Moderator program starting...")


    if op_task == "rank_people":
        rank_people(op_people, op_log)

    if op_task == "validate_forum":
        validate_forum(op_forum, op_log)

    if op_task == "censor_forum":
        validate_forum(op_forum, op_log)
        user = get_user_list(op_people)
        censor_forum(op_forum, op_words, op_log, user)

    if op_task == "evaluate_forum":
        rank_people(op_people, op_log)
        validate_forum(op_forum, op_log)
        user = get_user_list(op_people)
        censor_forum(op_forum, op_words, op_log, user)
        evaluate_forum(op_people, op_log, user)