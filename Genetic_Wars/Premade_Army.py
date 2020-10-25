import time
import random
import statistics
#Warning: I comment on all of this and have bad spelling sorry. 

#Contstant Varibles
GOAL = 1000
NUM_PEOPLE = 20
MIN_STR = 100
MAX_STR = 500
MODE_STR = 300
MUTATE_ODDS = 0.1
MUTATE_MIN = 0.5
MUTATE_MAX = 1.2
OFFSPRING_AMOUNT = 10
PEOPLE_PER_Y = 10
GENERATION_LIMIT = 500

#This checks if the number of people can be dived by 2 and if not then it adds one to it.
if NUM_PEOPLE % 2 != 0:
    NUM_PEOPLE += 1

def populate(num_people, min_str, max_str, mode_str):
    """Set up the function that will start to populate the tribes"""
    #More in depth this function takes does a random triangular which returns a floating number that was in the
    # middle of the two paramters and the mode gets it closer. Again I could be wrong use the google for more and better info.
    # Then a good old for loop. 
    return [int(random.triangular(min_str,max_str,mode_str))\
            for i in range(num_people)]

def training(population, goal):
    """Check if the population is doing good and nearing the goal"""
    avt = statistics.mean(population)
    return avt / goal

def select(population, to_retain):
    """Go through all of the warroirs and check which ones are best fit to breed and move on."""
    #This starts off by sorting the population then gets all of the population dived by 2 using floor divison I think
    #that just makes sure it doesn't output as a pesky decimal. Then it takes one half of memebers which shall be females.
    # which tend to be not as strong as males(Not being sexist just science thats how we are built.) So the front half will be 
    #The lower digits because we sorted it then the upper half will be males. Then it finishes off by getting the strongest males and
    #females and returns them.
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
    #This one is pretty self explanitory.
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
    #Mutates the childern which for the most part has bad mutations but those good ones are well really good.
    #Note: When running the program they are really powerful so you don't half to but for good results keep them in 
    #the decimal places.
    for index, person in enumerate(children):
        if mutate_odds >= random.random():
            children[index] = round(person * random.uniform(mutate_min,
                                                        mutate_max))
    return children

def main():
    """Initialize everything and display the results"""
    #Also for the most part self explaitory.
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
    print("average strenght per generation = {}".format(avt_str))
    print("\nnumber of generations = {}".format(generations))
    print("number of years = {}".format(int(generations / PEOPLE_PER_Y)))
    start_time = time.time()
    end_time = time.time()
    duration = end_time - start_time


