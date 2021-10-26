# Import the modules we use in our code
import random
import operator
import matplotlib.pyplot

# Set up the empty agents list
agents = []

# Create variables that will determine how many agents there are, and how
# many iterations or steps they move
num_of_agents = 10
num_of_iterations = 3

# We use a for loop to create the number of agents as specified in the
# num_of_agents variable, still with random [y, x] coords, and append to the
# initially empty agents list
for i in range(num_of_agents):
    agents.append([random.randint(0,99),random.randint(0,99)])
    

# Print each agent coords individually using another for loop
for i in range(len(agents)):
    print("Agent", i, "starting coords:", agents[i])
    
    
# For every iteration specified randomly move each agent in the agents list
# once on the y and x axis
# We generate a new random_number inside both for loops so that the probabilty
# is individual for each agent during each iteration
# We use the modulus operator to effectively turn our 100 x 100 environment
# into a torus, where if an agent moves off either axis (either positively or
# negatively) it appears at the other extreme of the axis
for j in range(num_of_iterations):
    for i in range(num_of_agents): 
        random_number = random.random()
        if random_number < 0.5:
            agents[i][0] = (agents[i][0] + 1) % 100
        else:
            agents[i][0] = (agents[i][0] - 1) % 100
        random_number = random.random()
        if random_number < 0.5:
            agents[i][1] = (agents[i][1] + 1) % 100
        else:
            agents[i][1] = (agents[i][1] - 1) % 100
    
    
    
    
    
    
    

'''
This is old code from the previous practical, included for reference

# Set up intial variables for Agent 0
# y0 = random.randint(0, 99)
# x0 = random.randint(0, 99)

# agents.append([y0,x0])

# We are now using random.randint directly inside the append method to create
# random starting [y, x] coords without creating additional variables
agents.append([random.randint(0, 99),random.randint(0, 99)])

# print("Initial coords of Agent 0: y0 =", y0, ", x0 =", x0)
print("Initial coords of Agent 0: ", agents[0])

# Generate a new random number so the probabilities of each step are different
random_number = random.random()

# Randomly walk one step on the y axis
if random_number < 0.5:
    agents[0][0] += 1
else:
    agents[0][0] -= 1

# Generate a new random number so the probabilities of each step are different
random_number = random.random()

# Randomly walk one step on the x axis
if random_number < 0.5:
    agents[0][1] += 1
else:
    agents[0][1] -= 1


# Generate a new random number so the probabilities of each step are different
random_number = random.random()

# Randomly walk one step on the y axis
if random_number < 0.5:
    agents[0][0] += 1
else:
    agents[0][0] -= 1

# Generate a new random number so the probabilities of each step are different
random_number = random.random()

# Randomly walk one step on the x axis
if random_number < 0.5:
    agents[0][1] += 1
else:
    agents[0][1] -= 1


# Print the final coordinates of Agent 0
# print("Final coords of Agent 0: y0 =", y0, ", x0 =", x0)
print("Final coords of Agent 0:", agents[0])











# Set up intial variables for Agent 1
# y1 = random.randint(0, 99)
# x1 = random.randint(0, 99)

# We are now using random.randint directly inside the append method to create
# random starting [y, x] coords without creating additional variables
agents.append([random.randint(0, 99),random.randint(0, 99)])

# print("Initial coords of Agent 1: y1 =", y1, ", x1 =", x1)
print("Initial coords of Agent 0: ", agents[1])


# Generate a new random number so the probabilities of each step are different
random_number = random.random()

# Randomly walk one step on the y axis
if random_number < 0.5:
    agents[1][0] += 1
else:
    agents[1][0] -= 1

# Generate a new random number so the probabilities of each step are different
random_number = random.random()

# Randomly walk one step on the x axis
if random_number < 0.5:
    agents[1][1] += 1
else:
    agents[1][1] -= 1


# Generate a new random number so the probabilities of each step are different
random_number = random.random()

# Randomly walk one step on the y axis
if random_number < 0.5:
    agents[1][0] += 1
else:
    agents[1][0] -= 1

# Generate a new random number so the probabilities of each step are different
random_number = random.random()

# Randomly walk one step on the x axis
if random_number < 0.5:
    agents[1][1] += 1
else:
    agents[1][1] -= 1


# Print the final coordinates of Agent 1
# print("Final coords of Agent 1: y1 =", y1, ", x1 =", x1)
print("Final coords of Agent 1:", agents[1])
'''

'''
The code for working out distance between two agents has also been commented
out for this practical

# These are test values to check that the Pythagorean formula below is
# calculating the distance between agents correctly. Uncomment the line
# below and the answer should be 5, a well known solution that we can test.
# agents = [[0,0], [4,3]]


# Calculate the distance between two agents using Pythagoras' theorem
# answer = (((x0 - x1)**2) + ((x0 - y1)**2))**0.5
answer = (((agents[0][1] - agents[1][1])**2) \
          + ((agents[0][0] - agents[1][0])**2))**0.5

# Print the distance between the two agents
print("The distance between agent 0 and agent 1 is: ", answer)
'''

# This line of code prints the [y, x] coords of the agent that is furthest
# east (has the largest x value). It does this by comparing the second
# element of each element within the agents list of lists.
# print(max(agents, key=operator.itemgetter(1)))

# We now create a variable with the [y, x] coords of the agent that is
# furthest east, so that we can easily reference the individual coords
# for use with matplotlib.pyplot.scatter
most_easterly = max(agents, key=operator.itemgetter(1))
print("The coords of the most easterly agent are:", most_easterly)


# Using matplotlib we set the y and x axes, we scatter plot the coordinates
# of our two agents onto the plot, then we show the plot
matplotlib.pyplot.ylim(0, 99)
matplotlib.pyplot.xlim(0, 99)
# matplotlib.pyplot.scatter(agents[0][1],agents[0][0])
# matplotlib.pyplot.scatter(agents[1][1],agents[1][0])

# We are now using a for loop to scatter plot all the agents in the agents
# list, no matter how many agents there are
for i in range(num_of_agents):
    matplotlib.pyplot.scatter(agents[i][1],agents[i][0])

# We re-plot our most easterly agent, but this time we set it red for
# identification. Because we plot this last it overwrites any previous colour
matplotlib.pyplot.scatter(most_easterly[1], most_easterly[0], color = 'red')


matplotlib.pyplot.show()