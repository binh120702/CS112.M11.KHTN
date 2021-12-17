import random
import os 
LEFT = 1
NUM_TEST = 2
TEST_NAME = "in/input"
if not os.path.isdir('in'):
	os.mkdir('in')
for loop_ in range(LEFT,NUM_TEST+1):
	file = open(TEST_NAME + str(loop_) + ".txt", "w")
	#file_sample = open(TEST_NAME + ".inp", "w")

	test = 200 # random.randint(1,1000)
	file.write(str(test) + '\n')
	#file_sample.write(str(test) + '\n')
	for _ in range(test):
		n = random.randint(1, 1000)
		m = random.randint(1, 200)
		file.write(str(n) + ' ' + str(m) + '\n')
		#file_sample.write(str(n) + ' ' + str(m) + '\n')
