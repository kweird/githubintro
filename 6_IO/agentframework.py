import random

class Agent():

    def __init__(self, environment):
        """
        Initialise an object of class Agent with two variables, x and y,
        which are randomly generated ints between 0 and 99

        Returns
        -------
        None.

        """
        self.environment = environment
        self.y = random.randint(0, 99)
        self.x = random.randint(0, 99)
        self.store = 0

    def __str__(self):
        #Standard string method, so that if you try to print an agent object
        #it will return something human readable, as defined by the code
        #below, so you can check on the status of the agent, rather than
        #just printing the agent's memory address.
        #This will print the x and y coords, and the store value of each agent
        return "Agent variables: x=" + str(self.x) + ", y=" + str(self.y) \
            + ", store=" + str(self.store)


    def move(self):
        """
        Randomly move an object of class Agent on the y and x axes by adding
        or subtracting from the y and x variables. The modulus 100 ensures
        that we treat our fixed environment like a torus

        Returns
        -------
        None.

        """
        if random.random() < 0.5:
            self.y = (self.y + 1) % 100
        else:
            self.y = (self.y - 1) % 100

        if random.random() < 0.5:
            self.x = (self.x + 1) % 100
        else:
            self.x = (self.x - 1) % 100

    def eat(self):
        #If the environment is higher than 10 units, eat 10 units and add to
        #agent's belly store
        if self.environment[self.y][self.x] > 10:
            self.environment[self.y][self.x] -= 10
            self.store += 10
        else:
        #Else if the environment is not greater than or equal to 10, eat
        #the environment down to zero height
            self.store += self.environment[self.y][self.x]
            self.environment[self.y][self.x] = 0
        #If belly is fuller than 100 units, chunder, and reset belly to zero
        if self.store >= 100:
            print("Agent has been sick")
            self.environment[self.y][self.x] += self.store
            self.store = 0