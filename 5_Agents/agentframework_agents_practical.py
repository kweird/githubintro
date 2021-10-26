import random

class Agent():

    def __init__(self):
        """
        Initialise an object of class Agent with two variables, x and y,
        which are randomly generated ints between 0 and 99

        Returns
        -------
        None.

        """
        self.y = random.randint(0, 99)
        self.x = random.randint(0, 99)

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

