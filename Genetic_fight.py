import time
import random
import statistics
import Premade_Army
import User_Army

def run():
    """Run both of the programs"""
    Premade_Army.start_time = time.time()
    Premade_Army.main()
    Premade_Army.end_time = time.time()
    User_Army.start_time = time.time()
    User_Army.main()
    User_Army.end_time = time.time()
    Premade_Army.duration = Premade_Army.start_time - Premade_Army.end_time
    User_Army.duration = User_Army.start_time - User_Army.end_time
    
    #Checks the programs to see who had won
    if Premade_Army.duration > User_Army.duration:
        print("The winning civilaztion is the Premade. With an overall time of {} to reach the overall goal.".format(Premade_Army.duration))
    if User_Army.duration > Premade_Army.duration:
        print("The winning civilaztion is the Users. With an overall time of {} to reach the overall goal.".format(User_Army.duration))


if __name__ == '__main__':
    run()