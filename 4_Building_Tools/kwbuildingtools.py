# Import the modules we use in our code
import random
import operator
import matplotlib.pyplot
import time

# We set the random seed to a certain value so we have reproducable results
# for testing. This can be commented out when not testing.
random.seed(0)

# We create a variable called start_time that stores the current time in
# seconds. We do this with the intention of recording the end time when the
# entire code has finished and to calculate the running time.
start_time = time.time()

# Set up the empty agents list
agents = []

# Create variables that will determine how many agents there are, and how
# many iterations or steps they move
num_of_agents = 500
num_of_iterations = 3


# We create a function called distance_between to work out the distance
# between any pair of [y, x] coords using Pythagoras' theorem.
# We drop a dimension when passing in the pair of coords because we are only
# going to pass in two separate [y, x] coords, not a list of lists containing
# two sets of [y, x] coords.
# e.g. we refer to agents_row_a[0] instead of agents_row_a[0][0]


def distance_between(agents_row_a, agents_row_b):
    """
    This function calculates and returns the distance between two sets of 
    points on the x, y plane.

    Parameters
    ----------
    agents_row_a : list with two elements that are numbers
        A list representing 2D coordinates.
    agents_row_b : list with two elements that are numbers
        A list representing 2D coordinates.

    Returns
    -------
    Float
        Returns the calculated Pythagorean distance between two sets of points
        (agents_row_a and agents_row_b) on the x, y plane.

    """
    return (((agents_row_a[0] - agents_row_b[0])**2) + \
            ((agents_row_a[1] - agents_row_b[1])**2))**0.5

# We use a for loop to create the number of agents as specified in the
# num_of_agents variable, still with random [y, x] coords, and append to the
# initially empty agents list
for i in range(num_of_agents):
    agents.append([random.randint(0,99),random.randint(0,99)])
    

# Print each agent coords individually using another for loop
#for i in range(len(agents)):
    #print("Agent", i, "starting coords:", agents[i])
    
    
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
    
# These are test values to check that the Pythagorean formula below is
# calculating the distance between agents correctly. Uncomment the lines
# below and the answer should be 5, a well known solution that we can test.
# distance = distance_between([0, 0], [4, 3])
# print(distance)



# We create two variables to store the max / min distances between two agents
# We manually calculate the max distance between the first two agents using
# Pythagoras' theorem, and set the min distance to be the same, then we update
# these values in the for loop below if any distance is greater for max
# distance, or smaller for min distance

# max_distance = (((agents[0][1] - agents[1][1])**2) \
#           + ((agents[0][0] - agents[1][0])**2))**0.5
max_distance = distance_between(agents[0], agents[1])
min_distance = max_distance

# We create a for loop to calculate the distance between every agent and every
# other agent

for i in agents:
    for j in agents:
        if i < j:
            distance = distance_between(i, j)
            max_distance = max(max_distance, distance)
            min_distance = min (min_distance, distance)
            #print("Distance between", i, "and", j, "is:", distance)
            #print("Max distance:", max_distance)
            #print("Min distance:", min_distance)

# This is an alternative way of calculating the distance between every agent

# for i in range(0, num_of_agents, 1):
#     for j in range(i, num_of_agents, 1):
#         distance = distance_between(agents[i], agents[j])
#         max_distance = max(max_distance, distance)
#         min_distance = min (min_distance, distance)
#         #print("Distance between", i, "and", j, "is:", distance)
#         #print("Max distance:", max_distance)
#         #print("Min distance:", min_distance)



# This line of code prints the [y, x] coords of the agent that is furthest
# east (has the largest x value). It does this by comparing the second
# element of each element within the agents list of lists.
# print(max(agents, key=operator.itemgetter(1)))

# We now create a variable with the [y, x] coords of the agent that is
# furthest east, so that we can easily reference the individual coords
# for use with matplotlib.pyplot.scatter
most_easterly = max(agents, key=operator.itemgetter(1))
print("The coords of the most easterly agent are:", most_easterly)

# most_westerly = min(agents, key=operator.itemgetter(1))
# print("The coords of the most westerly agent are:", most_westerly)
# most_northerly = max(agents, key=operator.itemgetter(0))
# print("The coords of the most northerly agent are:", most_northerly)
# most_southerly = min(agents, key=operator.itemgetter(0))
# print("The coords of the most southerly agent are:", most_southerly)


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

# We create a variable called end_time that stores the current time in
# seconds. We then subtract the end time from the starting time and print the
# total running time of the code.
end_time = time.time()
print("Total running time = " + str(end_time - start_time) + " seconds")