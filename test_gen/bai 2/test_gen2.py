import random
import os 
LEFT = 4
NUM_TEST = 6
TEST_NAME = "in/input"
if not os.path.isdir('in'):
	os.mkdir('in')
for loop_ in range(LEFT,NUM_TEST+1):
	file = open(TEST_NAME + str(loop_) + ".txt", "w")

	test = 10000 
	file.write(str(test) + '\n')
	for _ in range(test):
		x = random.randint(-10000000,10000000)
		y = random.randint(-10000000, -1)
		file.write(str(x) + ' ' + str(y) + '\n')
