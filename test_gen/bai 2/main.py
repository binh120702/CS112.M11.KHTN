import os 
import math 


TEST_NAME = "out/input"
if not os.path.isdir('out'):
	os.mkdir('out')

LEFT = 1
NUM_TEST = 10
for loop_ in range(LEFT,NUM_TEST+1):
	file_inp = open("in/input"+str(loop_)+".txt", "r")
	ff = file_inp.read().split()
	file = open("out/output" + str(loop_) + ".txt", "w")

 
	def check(r):
	    global n
	    global x
	    global y
	    mi = 100000000000000.0
	    mx = -100000000000000.0
	    for i in range(n):
	        if abs(y[i])>2*r:
	            return False
	        dis = math.sqrt(abs(2*r*abs(y[i]) - y[i]*y[i]))
	        if mi > x[i] + dis:
	            mi = x[i] + dis
	        if mx < x[i] - dis:
	            mx = x[i] - dis
	    return mi >= mx
	 
	 
	n = int(ff[0])
	x = []
	y = []
	neg = False
	pos = False
	 
	for ii in range(n):
	    x.append(int(ff[ii*2 + 1]))
	    y.append(int(ff[ii*2 + 2]))
	    if int(ff[ii*2 + 2]) < 0:
	        neg = True
	    else:
	        pos = True
	 
	if neg and pos:
		file.write("-1\n")
	else:
		l = 0.0
		r = 100000000000000.0
		for _ in range(300):
		    mid = (l+r)/2
		 
		    if check(mid):
		        r = mid
		    else:
		        l = mid
		file.write(str(l) + "\n")