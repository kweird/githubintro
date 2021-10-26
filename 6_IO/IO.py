# Import the modules we use in our code
import random
import operator
import matplotlib.pyplot
import time
import agentframework
import csv

# We set the random seed to a certain value so we have reproducable results
# for testing. This can be commented out when not testing.
random.seed(0)

# We create a variable called start_time that stores the current time in
# seconds. We do this with the intention of recording the end time when the
# entire code has finished and to calculate the running time.
start_time = time.time()


# Set up the empty agents list
agents = []

# Set up the empty environment list
environment = []

# Create variables that will determine how many agents there are, and how
# many iterations or steps they move
num_of_agents = 5
num_of_iterations = 11

# We create a function called distance_between to work out the distance
# between any pair of objects of the Agent class using their [y, x] coords 
# using Pythagoras' theorem.

def distance_between(agents_row_a, agents_row_b):
    """
    This function calculates and returns the distance between two sets of 
    points on the x, y plane.

    Parameters
    ----------
    agents_row_a : an object of the Agent class
        A object representing an agent, which includes x and y variables of
        the agent's position on a 2D plane.
    agents_row_b : an object of the Agent class
        A object representing an agent, which includes x and y variables of
        the agent's position on a 2D plane.

    Returns
    -------
    Float
        Returns the calculated Pythagorean distance between two agent objects
        using their coords on the x, y plane.

    """
    return (((agents_row_a.x - agents_row_b.x)**2) + \
            ((agents_row_a.y - agents_row_b.y)**2))**0.5
        
        
# Using the csv module we open a text file which contains raster data for an
# environment. We loop through all all the data and create an variable called
# environment, which is a list of lists corresponding to the rows and columns
# of data contained in the in.csv file

with open('in.txt', newline='') as f:
    reader = csv.reader(f, quoting=csv.QUOTE_NONNUMERIC)
    for row in reader:
        rowList = []
        for value in row:
            rowList.append(value)
        environment.append(rowList)
        
# Calculate size of our environment, so that it can be passed to the 
# Agent class in our agentframework module, so objects of the Agent class can
# interact with it
environment_rows = len(environment)
environment_cols = len(environment[0])


# We use a for loop to create the number of agents as specified in the
# num_of_agents variable, still with random [y, x] coords (due to the init
# function in the Agent class), and append to the initially empty agents list

for i in range(num_of_agents):
    agents.append(agentframework.Agent(environment))
    print("Agent", i, "initial coords:", agents[i].x, agents[i].y)
    

# Print each agent coords individually using another for loop
#for i in range(len(agents)):
    #print("Agent", i, "starting coords:", agents[i])
    
    
# For every iteration specified randomly move each agent in the agents list
# once on the y and x axis using the move function within the Agent class



for j in range(num_of_iterations):
    for i in range(num_of_agents): 
        agents[i].move()
        #print("Agent", i, "moved, new coords:", agents[i].x, agents[i].y)
        agents[i].eat()
        #print("Agent", i, "ate, new store value:", agents[i].store)
        print(agents[i])



# We create two variables to store the max / min distances between two agents
# We manually calculate the max distance between the first two agents using
# Pythagoras' theorem, and set the min distance to be the same, then we update
# these values in the for loop below if any distance is greater for max
# distance, or smaller for min distance

max_distance = distance_between(agents[0], agents[1])
min_distance = max_distance

# We create a for loop to calculate the distance between every agent and every
# other agent

for i in range(0, num_of_agents, 1):
    for j in range(i, num_of_agents, 1):
        if i != j:
            distance = distance_between(agents[i], agents[j])
            max_distance = max(max_distance, distance)
            min_distance = min (min_distance, distance)
            #print("Distance between Agent", i, "and Agent", j, "is:", distance)
            #print("Max distance:", max_distance)
            #print("Min distance:", min_distance)

        
print("Max distance:", max_distance)
print("Min distance:", min_distance)



total_store = 0

for i in range(num_of_agents): 
    total_store = total_store + agents[i].store
        
print("Total amount stored by agents:", total_store)

# Using matplotlib we set the y and x axes, we scatter plot the coordinates
# of our two agents onto the plot, then we show the plot
matplotlib.pyplot.ylim(0, environment_cols)
matplotlib.pyplot.xlim(0, environment_rows)

# Show the environment raster image
matplotlib.pyplot.imshow(environment)

# We are now using a for loop to scatter plot all the agents in the agents
# list, no matter how many agents there are
for i in range(num_of_agents):
    matplotlib.pyplot.scatter(agents[i].x,agents[i].y)

# We re-plot our most easterly agent, but this time we set it red for
# identification. Because we plot this last it overwrites any previous colour
# matplotlib.pyplot.scatter(most_easterly[1], most_easterly[0], color = 'red')


matplotlib.pyplot.show()

# We create a variable called end_time that stores the current time in
# seconds. We then subtract the end time from the starting time and print the
# total running time of the code.
end_time = time.time()
print("Total running time = " + str(end_time - start_time) + " seconds")