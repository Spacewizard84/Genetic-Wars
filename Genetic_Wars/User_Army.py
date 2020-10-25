import time
import random
import statistics
import Premade_Army
Contstants = True

def check(msg):
    """Check if a letter is entered. If it is tell the user that doesn't work then prompt them again."""
    while True:
        try:
            msg = (int(input()))
        except ValueError:
            print("You Have to enter numbers and only numbers.")
            continue
        return msg
        
def check_decimal(msg):
    """Check if a decimal is entered and if it is allow it."""
    while True:
        try:
            msg = (float(input()))
        except ValueError:
            print("You Have to enter numbers and only numbers. This will only be used for the mutation and other decimal specifc things.")
            continue
        return msg

        
#Contstant Varibles
while Contstants:
    print("Welcome to the Genetics War Set up.")
    print("What do you want the goal to be(min should be 1000)?: ")
    GOAL = check("")
    print("How many people do you want to start with?: ")
    NUM_PEOPLE = check("")
    print("What do you want the minimum str to be?: ")
    MIN_STR = check("")
    print("What would you want the max str to be?: ")
    MAX_STR = check("")
    print("what would you like the mode str to be?: ")
    MODE_STR = check("")
    print("What would you like the mutate odds to be?: ")
    MUTATE_ODDS = check_decimal("")
    print("What would you like the mutate minimum to be?: ")
    MUTATE_MIN = check_decimal("")
    print("What would you like the mutate max to be?: ")
    MUTATE_MAX = check_decimal("")
    print("How much offspring do you want one pair to produce?: ")
    OFFSPRING_AMOUNT = check("")
    print("How many people per year would you like there to be?: ")
    PEOPLE_PER_Y = check("")
    print("What would you like the generation limit to be?: ")
    GENERATION_LIMIT = check("")
#Add skills which effect most of the contsants
    skill_loop = True
    while skill_loop:
        skill = input("Now time to add skills if you want(y/n): ")
        if skill == 'n':
            skill_loop = False
        elif skill == 'y':
            skills = ['War', 'Sci', 'Leadership', 'Farming']
            print(skills)
            print("Type '1' for War. \nType '2' for Sci. \nType '3' for Leadership. \nType '4' for Farming.")
            skills[0] = 1
            skills[1] = 2
            skills[2] = 3
            skills[3] = 4
            Pick_Skill = input("Please pick the skill you want by putting in the number of a skill: ")
            #Set if statments to check for a skill that was picked
            if Pick_Skill == '1':
                print("You have picked war as your main skill your min/max/mode str will all be increesed.")
                MIN_STR += 5
                MAX_STR += 5
                MODE_STR += 5
            if Pick_Skill == '2':
                print("You have picked science as you skill all of the mutate possiblitys will be increased.")
                MUTATE_ODDS += 2
                MUTATE_MIN += 1
                MUTATE_MAX += 2
            if Pick_Skill == '3':
                print("You have picked Leadership as your skill your population and people per year shall be increased")
                TRIBE_SIZE += 10
                PEOPLE_PER_Y += 5
            if  Pick_Skill == '4':
                print("you have picked Farming as your skill People per Year and Mutate ODDs shall be increased")
                PEOPLE_PER_Y += 5
                MUTATE_ODDS += 2
            skill_loop = False
    print("Now to decide if you want to attack.")
    attack = input("Do you want to attack the Premade army(y/n):  ")
    #This just defects the Premade_Army well not sure really hard to tell but from some of my tests 
    #it defects the premade army. 
    if attack == 'n':
       Contstants = False
    elif attack == 'y':
        print("Now to decide your method of attack.")
        attacks = ['Nuke', 'Bio', 'Pilliage', 'Orbital Laser']
        print(attacks)
        print(f"Type '1' for {attacks[0]}. \nType '2' for {attacks[1]}. \nType '3' for {attacks[2]}. \nType '4' for {attacks[3]}")
        attacks[0] = 1
        attacks[1] = 2
        attacks[2] = 3
        attacks[3] = 4
        attack_method = input("Put the number of desired attack: ")
        if attacks == '1':
            Premade_Army.NUM_PEOPLE -= 25 + random.randint(0, 500)
            Premade_Army.MUTATE_ODDS += 1
        if attacks == '2':
            Premade_Army.NUM_PEOPLE -= 20
            Premade_Army.PEOPLE_PER_Y -= 5
        if attacks == '3':
            Premade_Army.NUM_PEOPLE -= random.randint()
            NUM_PEOPLE += 2
            MIN_STR += 2
        if attacks == '4':
            Premade_Army.NUM_PEOPLE -= 20 + random.randint(0, 20)
            Premade_Army.MIN_STR -= 20
        Contstants = False

#This checks if the number of people can be dived by 2 and if not then it adds one to it.
if NUM_PEOPLE % 2 != 0:
    NUM_PEOPLE += 1

def attack(num_people, min_str, max_str, mode_str, mutate_odds, mutate_min, mutate_max):
    """Allows the user to attack the Premade army"""


def populate(num_people, min_str, max_str, mode_str):
    """Set up the function that will start to populate the tribes"""
    return [int(random.triangular(min_str,max_str,mode_str))\
            for i in range(num_people)]

def training(population, goal):
    """Check if the population is doing good and nearing the goal"""
    avt = statistics.mean(population)
    return avt / goal

def select(population, to_retain):
    """Go through all of the warroirs and check which ones are best fit to breed and move on."""
    sorted_pop = sorted(population)
    to_keep_by_sex = to_retain//2
    members = len(sorted_pop)//2
    females = sorted_pop[:members]
    males = sorted_pop[members:]
    strong_females = females[-to_keep_by_sex:]
    strong_males = males[-to_keep_by_sex:]
    return strong_males, strong_females

def breed(males, females, offspring_amount):
    """Breed the stonger males and females"""
    random.shuffle(males)
    random.shuffle(females)
    children = []
    for male, female in zip(males, females):
        for child in range(offspring_amount):
            child = random.randint(male, female)
            children.append(child)
    return children

def mutations(children, mutate_odds,mutate_min, mutate_max):
    """Check if the child will be mutated"""
    for index, person in enumerate(children):
        if mutate_odds >= random.random():
            children[index] = round(person * random.uniform(mutate_min,
                                                        mutate_max))
    return children

def main():
    """Initialize everything and display the results"""
    generations = 0
    parents = populate(NUM_PEOPLE,MIN_STR, MAX_STR, MODE_STR)
    print("The Inital population Strenght was = {}".format(parents))
    popl_training = training(parents,GOAL)
    print("The Inital population training was = {}".format(popl_training))
    print("Number to retain = {}".format(NUM_PEOPLE))

    avt_str = []

    while popl_training < 1 and generations < GENERATION_LIMIT:
        strong_males, strong_females = select(parents, NUM_PEOPLE)
        children = breed(strong_males, strong_males, OFFSPRING_AMOUNT)
        children = mutations(children, MUTATE_ODDS, MUTATE_MIN, MUTATE_MAX)
        parents = strong_males + strong_males + children
        popl_training = training(parents, GOAL)
        print("Generation {} training = {:4f}".format(generations, popl_training))

        avt_str.append(int(statistics.mean(parents)))
        generations += 1
    print("average str per generation = {}".format(avt_str))
    print("\nnumber of generations = {}".format(generations))
    print("number of years = {}".format(int(generations / PEOPLE_PER_Y)))
    start_time = time.time()
    end_time = time.time()
    duration = end_time - start_time