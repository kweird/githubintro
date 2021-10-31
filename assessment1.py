import random
import operator
import tkinter
import matplotlib
matplotlib.use('TkAgg')
import matplotlib.pyplot
import matplotlib.animation 
import agentframework
import csv
import requests
import bs4
import time

start_time = time.time()

# We set the random seed so we can see repeatable patterns
random.seed(0)

#Function distance_between that uses Pythagoras' theorem to calculate distance between agents
#def distance_between(agents_row_a, agents_row_b):
#    return (((agents_row_a.x - agents_row_b.x)**2) +
#    ((agents_row_a.y - agents_row_b.y)**2))**0.5

#Setting up initial variables
num_of_agents = 10
num_of_iterations = 1000 #Number of times the agents move
agents = []
environment = [] 
neighbourhood = 20



r = requests.get('http://www.geog.leeds.ac.uk/courses/computing/practicals/python/agent-framework/part9/data.html')
content = r.text
soup = bs4.BeautifulSoup(content, 'html.parser')
td_ys = soup.find_all(attrs={"class" : "y"})
td_xs = soup.find_all(attrs={"class" : "x"})
print(td_ys)
print(td_xs)





#Code to store the environment for ABM as a list of lists
#Read the in.text file
with open('in.txt', newline='') as f:
    reader = csv.reader(f, quoting=csv.QUOTE_NONNUMERIC)
    for row in reader:
        rowList = []
        for value in row:
            rowList.append(value)
        environment.append(rowList)
        
#Calculate size of environment, so that it can be used to pass to agents etc
rows = len(environment)
cols = len(environment[0])




# Make the agents. This is calling the Agent class in agentframework
# We are passing various variables so they need to be created first
for i in range(num_of_agents):
    
    # We set the y and x values from the data scraped from the webpage, if 
    # we choose not to do this 
    y = int(td_ys[i].text)
    x = int(td_xs[i].text)
    agents.append(agentframework.Agent(i, agents, environment, rows, cols, y, x))
    
    # This is the code to not pass y and x variables, so the agents will be 
    # created in a random place
    
    #agents.append(agentframework.Agent(i, agents, environment, rows, cols))
    

#Create variables for max and min distance between each agent
max_distance = 0
min_distance = 0

'''
max_distance = distance_between(agents[0], agents[1])
min_distance = max_distance

#for i in range(num_of_agents):
for i in range(0, num_of_agents, 1):
    #for j in range(num_of_agents):
    for j in range(0, num_of_agents, 1):    
        #if i != j:
        #if i < j:
            answer = distance_between(agents[i], agents[j])
            max_distance = max(max_distance, answer)
            min_distance = min(min_distance, answer)
        
print("Maximum distance between agents =", max_distance)
print("Minimum distance between agents =", min_distance)
'''


def run():
    animation = matplotlib.animation.FuncAnimation(fig, update, frames=gen_function, repeat=False)
    canvas.draw()    
    

fig = matplotlib.pyplot.figure(figsize=(7, 7))
ax = fig.add_axes([0, 0, 1, 1])

# This builds the main window ("root"); sets its title, then creates and lays
# out a matplotlib canvas embedded within our window and associated with fig,
# our matplotlib figure.
root = tkinter.Tk()
root.wm_title("Model")
canvas = matplotlib.backends.backend_tkagg.FigureCanvasTkAgg(fig, master=root)
canvas._tkcanvas.pack(side=tkinter.TOP, fill=tkinter.BOTH, expand=1)


menu = tkinter.Menu(root)
root.config(menu=menu)
model_menu = tkinter.Menu(menu)
menu.add_cascade(label="Model", menu=model_menu)
model_menu.add_command(label="Run model", command=run)




carry_on = True	
	
def update(frame_number):
    #print("update")
    fig.clear()   
    
    #Show the environment raster image
    matplotlib.pyplot.imshow(environment)

    #Limit the graph size on the x and y axis to the max size of our environment
    matplotlib.pyplot.xlim(0, cols)
    matplotlib.pyplot.ylim(0, rows)
    
    global carry_on

    print("Iteration: ", frame_number)
    random.shuffle(agents)
    for i in range(num_of_agents):
        #Make each agent move
        agents[i].move()
        #After moving, make each agent eat
        agents[i].eat()
        #After eating make each agent share, if they are in range
        agents[i].share_with_neighbours(neighbourhood)
        #Then Print out each agent's status after moving, eating and sharing
        print("Agent", i, agents[i])
        
    if random.random() < 0.01:
        carry_on = False
        print("Probability stopping condition met")
    
    for i in range(num_of_agents):
        #print("Scatter plotting")
        matplotlib.pyplot.scatter(agents[i].x,agents[i].y)
        #print(agents[i][0],agents[i][1])

		
def gen_function(b = [0]):
    a = 0
    global carry_on #Not actually needed as we're not assigning, but clearer
    global agents # Used to access the agents list within this function
    while (a < num_of_iterations) & (carry_on) :
        yield a			# Returns control and waits next call.
        a = a + 1
        #print("Iteration number", a)
    else:
        print("Max iterations: ", num_of_iterations)
        print("Stopping condition encountered:\n" + "Completed " + str(a) + " iterations")
        
    #Print final agent states
    print("Final agents")
    #Use the sorted function to reorder the agents list, sorted on the attribute i
    #This is to make the readout easier to read for humans, as the agents are 
    #always in the same order, so we can easily compare how any changes have
    #affected the outcome
    agents = sorted(agents, key=lambda Agent: Agent.i)
    for i in range(num_of_agents):
        print(agents[i])

    #Write sorted agent final states to output.txt
    #Using with means the file is closed when the with statement is finished
    with open("output.txt", "w") as f:
        f.write("Final agent states\n")
        for i in range(num_of_agents):
            f.write(str(agents[i]))
            f.write("\n")


    end_time = time.time()
    
    print ("Time taken =", (end_time - start_time))


#animation = matplotlib.animation.FuncAnimation(fig, update, interval=1, repeat=False, frames=10)
#animation = matplotlib.animation.FuncAnimation(fig, update, frames=gen_function, repeat=False)

#def run():
#    animation = matplotlib.animation.FuncAnimation(fig, update, frames=gen_function, repeat=False)
#    canvas.draw()

#matplotlib.pyplot.show()






tkinter.mainloop()













