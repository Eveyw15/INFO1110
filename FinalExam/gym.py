class Trainer:
    def __init__(self, name, rate, classes):
        self.name = name
        self.classes = classes
        self.rate = rate

class Classes:
    def __init__(self, ID, class_name):
        self.ID = ID
        self.class_name = class_name

def get_trainer_list():
    file_trainer = open("gym_trainer.txt")
    file_schedule = open("gym_schedule.txt")
    f_trainer = file_trainer.readlines()
    f_schedule = file_schedule.readlines()
    trainer = []
    i = 0
    while i < len(f_trainer):
        name = " ".join(f_trainer[i].split()[1:])
        rate = f_trainer[i].split()[0]
        classes = f_schedule[i].strip("\n")
        temp = Trainer(name, rate, classes)
        trainer.append(temp)
        i += 1
    return trainer

def get_class_list():
    file_classes = open("gym_classes.txt")
    f_classes = file_classes.readlines()
    classes = []
    i = 0
    while i < len(f_classes):
        class_name = " ".join(f_classes[i].split()[1:])
        ID = f_classes[i].split()[0]
        temp = Classes(ID, class_name)
        classes.append(temp)
        i += 1
    return classes

trainer = get_trainer_list()
classes = get_class_list()

choice = input('''___________________________________________________________ 
Menu.. 
___________________________________________________________ 
1. Display the gym class name by its class ID
2. Display class ID by class name
3. Display which gym trainer(s) is running a class with a given class ID
4. Display gym classes that a trainer is running
5. Display trainer(s) name who is running a given number of classes
6. Display the trainer's salary
7. Display all classes with IDs
8. Display the details of all gym schedules and gym trainers
9. Exit the program
enter your choice ---> ''')

while choice != "9":
    if choice == "1":
        id = input("Enter a class ID ---> ")
        i = 0
        while i < len(classes):
            a = classes[i].ID
            if id == classes[i].ID:
                print(classes[i].class_name)
                break
            if i == len(classes)-1 and id != classes[i].ID:
                print("Class ID does not exist")
            i += 1

    elif choice == "2":
        class_name = input("Enter a class name ---> ")
        i = 0
        while i < len(classes):
            if class_name == classes[i].class_name:
                print(classes[i].ID)
                break
            if i == len(classes) - 1 and class_name != classes[i].class_name:
                print("Class name does not exist")
            i += 1

    elif choice == "3":
        id = int(input("Enter Class ID ---> "))
        output = []
        i = 0
        while i < len(trainer):
            temp = trainer[i].classes
            if temp[id-1] == "1":
                output.append(trainer[i].name)
            i += 1
        if output == []:
            print("Class ID does not exist")
        print(",".join(output))

    elif choice == "4":
        name = input("Enter Trainer Name ---> ")
        output = []
        i = 0
        while i < len(trainer):
            if name == trainer[i].name:
                temp = trainer[i].classes
                j = 0
                while j < len(temp):
                    if temp[j] == "1":
                        output.append(classes[j].class_name)
                    j += 1
                break
            if i == len(trainer) and name != trainer[i].name:
                print("No trainer with this name exists")
                break
            i += 1
        if output == []:
            print("No class is assigned to this trainer")
        print(",".join(output))

    elif choice == "5":
        count = int(input("Enter count of classes ---> "))
        output = []
        i = 0
        while i < len(trainer):
            temp = trainer[i].classes
            new_count = 0
            j = 0
            while j < len(temp):
                if temp[j] == "1":
                    new_count += 1
                j += 1
            if new_count == count:
                output.append(trainer[i].name)
            i += 1
        if output == []:
            print("Data Not Available")
        print(",".join(output))

    elif choice == "6":
        name = input("Enter Trainer Name ---> ")
        output = 0
        i = 0
        while i < len(trainer):
            if name == trainer[i].name:
                temp = trainer[i].classes
                new_count = 0
                j = 0
                while j < len(temp):
                    if temp[j] == "1":
                        new_count += 1
                    j += 1
                output = new_count * int(trainer[i].rate)
            i += 1
            if i == len(trainer) and name != trainer[i].name:
                print("No trainer with this name exists")
        print(f"Salary for this trainer is ${output}")

    elif choice == "7":
        file_classes = open("gym_classes.txt")
        f_classes = file_classes.readlines()
        print(f_classes)
        f_classes.close()

    # elif choice == "8":

    else:
        print("Wrong choice, please enter again")

    choice = input('''___________________________________________________________ 
Menu.. 
___________________________________________________________ 
1. Display the gym class name by its class ID
2. Display class ID by class name
3. Display which gym trainer(s) is running a class with a given class ID
4. Display gym classes that a trainer is running
5. Display trainer(s) name who is running a given number of classes
6. Display the trainer's salary
7. Display all classes with IDs
8. Display the details of all gym schedules and gym trainers
9. Exit the program
enter your choice ---> ''')

print("Thank you for using our program. Bye!")
