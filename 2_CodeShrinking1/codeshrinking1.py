# Import the modules we use in our code
import random
import operator
import matplotlib.pyplot

# Set up the empty agents list
agents = []

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


# These are test values to check that the Pythagorean formula below is
# calculating the distance between agents correctly. Uncomment the line
# below and the answer should be 5, a well known solution that we can test.
# agents = [[0,0], [4,3]]


# Calculate the distance between two agents using Pythagoras' theorm
# answer = (((x0 - x1)**2) + ((x0 - y1)**2))**0.5
answer = (((agents[0][1] - agents[1][1])**2) \
          + ((agents[0][0] - agents[1][0])**2))**0.5

# Print the distance between the two agents
print("The distance between agent 0 and agent 1 is: ", answer)


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
matplotlib.pyplot.scatter(agents[0][1],agents[0][0])
matplotlib.pyplot.scatter(agents[1][1],agents[1][0])

# We re-plot our most easterly agent, but this time we set it red for
# identification. Because we plot this last it overwrites any previous colour
matplotlib.pyplot.scatter(most_easterly[1], most_easterly[0], color = 'red')


matplotlib.pyplot.show()