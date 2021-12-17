import os 

M=10**9+7
L=8**6
d=[1]*L
d[:10]=[1]*10
for i in range(10,L):
	d[i]=(d[i-9]+d[i-10])%M


TEST_NAME = "out/input"
if not os.path.isdir('out'):
	os.mkdir('out')

LEFT = 1
NUM_TEST = 10
for loop_ in range(LEFT,NUM_TEST+1):
	file_inp = open("in/input"+str(loop_)+".txt", "r")
	ff = file_inp.read().split()
	file = open("out/output" + str(loop_) + ".txt", "w")
	for i in range(int(ff[0])):
		n = ff[i*2+1]
		m = ff[i*2+2]
		o = int(m);
		file.write(str(sum(d[o+int(c)]for c in n)%M) + '\n')