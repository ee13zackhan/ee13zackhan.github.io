import random
import matplotlib.pyplot
import agentframework
import enviro

random.seed(2)


agents = []

def move(y, x):
    """
    Randomly moves the agent by one step or stays still
    
    Parameters
    ----------
    None
    """ 
    rand_y = random.random()
    if rand_y < 0.33:
        y = (y + 1) % 10
    elif 0.33 <= rand_y < 0.66:
        y = (y - 1) % 10
    else:
        pass

    rand_x = random.random()
    if rand_x < 0.33:
        x = (x + 1) % 10
    elif 0.33 <= rand_x < 0.66:
        x = (x + 1) % 10
    else:
        pass

    print(f"({y},{x})")
    
    
agent1 = [random.randint(0,9), random.randint(0,9)]
agent2 = [random.randint(0,9), random.randint(0,9)]


for i in range(10):
    move(agent1[0],agent1[1])
    move(agent2[0],agent2[1])












