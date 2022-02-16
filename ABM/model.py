# -*- coding: utf-8 -*-
"""
Created on Tue Feb  1 11:10:18 2022

@author: ee13zk
"""
import random
import operator
import matplotlib.pyplot
import agentframework
import enviro

num_of_agents = 10
num_of_iterations = 10
neighbourhood = 20
#environment = []
agents = []

#Make the environment
'''f = open("in.txt", newline='')
reader = csv.reader(f,quoting=csv.QUOTE_NONNUMERIC)

for row in reader:
    environment.append(row)
    
f.close()

matplotlib.pyplot.xlim(0, 300)
matplotlib.pyplot.ylim(0, 300)
matplotlib.pyplot.imshow(environment)
matplotlib.pyplot.show()'''


random.seed(1)

# Make the agents.
for i in range(num_of_agents):
    agents.append(agentframework.Agent(enviro.environment, agents, i))
    
    print(f"Agent ID={agents[i].idnum}, y={agents[i].y}, x={agents[i].x}")


# Move the agents.
for j in range(num_of_iterations):
    random.shuffle(agents)
    for i in range(num_of_agents):
        print(str(j))
        agents[i].move()
        agents[i].eat()
        agents[i].share_with_neighbours(neighbourhood)
        # print(f"ID = {agents[i].idnum}")

# matplotlib.pyplot.xlim(0, 300)
# matplotlib.pyplot.ylim(0, 300)
# matplotlib.pyplot.imshow(enviro.environment)
# for i in range(num_of_agents):
#     matplotlib.pyplot.scatter(agents[i].x,agents[i].y)
# matplotlib.pyplot.show()


'''for agents_row_a in agents:
    for agents_row_b in agents:
        distance = agent.distance_between(agents_row_a, agents_row_b)
'''