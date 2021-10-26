# Import the random module
import random

# Set up initial variables for Agent 0
# y0 = 50
# x0 = 50
y0 = random.randint(0, 99)
x0 = random.randint(0, 99)

print("Initial coords of Agent 0: y0 =", y0, ", x0 =", x0)

# Generate a new random number so the probabilities of each step are different
random_number = random.random()

# Randomly walk one step on the y axis
if random_number < 0.5:
    y0 += 1
else:
    y0 -= 1

# Generate a new random number so the probabilities of each step are different
random_number = random.random()

# Randomly walk one step on the x axis
if random_number < 0.5:
    x0 += 1
else:
    x0 -= 1


# Generate a new random number so the probabilities of each step are different
random_number = random.random()

# Randomly walk one step on the y axis
if random_number < 0.5:
    y0 += 1
else:
    y0 -= 1

# Generate a new random number so the probabilities of each step are different
random_number = random.random()

# Randomly walk one step on the x axis
if random_number < 0.5:
    x0 += 1
else:
    x0 -= 1


# Print the final coordinates of Agent 0
# print("y0 =", y0)
# print("x0 =", x0)
print("Final coords of Agent 0: y0 =", y0, ", x0 =", x0)











# Set up initial variables for Agent 1
# y1 = 50
# x1 = 50
y1 = random.randint(0, 99)
x1 = random.randint(0, 99)

print("Initial coords of Agent 1: y1 =", y1, ", x1 =", x1)


# Generate a new random number so the probabilities of each step are different
random_number = random.random()

# Randomly walk one step on the y axis
if random_number < 0.5:
    y1 += 1
else:
    y1 -= 1

# Generate a new random number so the probabilities of each step are different
random_number = random.random()

# Randomly walk one step on the x axis
if random_number < 0.5:
    x1 += 1
else:
    x1 -= 1


# Generate a new random number so the probabilities of each step are different
random_number = random.random()

# Randomly walk one step on the y axis
if random_number < 0.5:
    y1 += 1
else:
    y1 -= 1

# Generate a new random number so the probabilities of each step are different
random_number = random.random()

# Randomly walk one step on the x axis
if random_number < 0.5:
    x1 += 1
else:
    x1 -= 1


# Print the final coordinates of Agent 1
# print("y1 =", y1)
# print("x1 =", x1)
print("Final coords of Agent 1: y1 =", y1, ", x1 =", x1)


# These are test values to check that the Pythagorean formula below is
# calculating the distance between agents correctly. Uncomment the four lines
# below and the answer should be 5, a well known solution that we can test.
# y0 = 0
# x0 = 0
# y1 = 4
# x1 = 3


# Calculate the distance between two agents using Pythagoras' theorm
answer = (((x0 - x1)**2) + ((y0 - y1)**2))**0.5

# Print the distance between the two agents
print("The distance between agent 0 and agent 1 is: ", answer)