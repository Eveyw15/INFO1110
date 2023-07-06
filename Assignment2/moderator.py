"""
Author: Elaine
SID: 520154106
Unikey: yliu8540
"""
import sys
import my_functions

sys.argv = ["moderator.py", "-task", "evaluate_forum", "-log", "example.log", "-forum", "example.forum", "-words", "example.words", "-people", "example.people"]


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
                elif add0 == 0 and add1 == 0:
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
            if not my_functions.task(op_task):
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

    my_functions.read(op_forum)
    my_functions.read(op_words)
    my_functions.read(op_people)
    print("Moderator program starting...")


    if op_task == "rank_people":
        my_functions.rank_people(op_people, op_log)

    if op_task == "validate_forum":
        my_functions.validate_forum(op_forum, op_log)

    if op_task == "censor_forum":
        my_functions.validate_forum(op_forum, op_log)
        user = my_functions.get_user_list(op_people)
        my_functions.censor_forum(op_forum, op_words, op_log, user)

    if op_task == "evaluate_forum":
        my_functions.rank_people(op_people, op_log)
        my_functions.validate_forum(op_forum, op_log)
        user = my_functions.get_user_list(op_people)
        my_functions.censor_forum(op_forum, op_words, op_log, user)
        my_functions.evaluate_forum(op_people, op_log, user)
