# 1059D Nature Reserve
import math 

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
        if mi > x[i] + dis: # min Right
            mi = x[i] + dis
        if mx < x[i] - dis: # max Left
            mx = x[i] - dis
    return mi >= mx

# doc 
n = int(input())
x = []
y = []
neg = False
pos = False

for _ in range(n):
    xy = input().split()
    x.append(int(xy[0]))
    y.append(int(xy[1]))
    if int(xy[1])<0:
        neg = True
    else:
        pos = True

# 2 phia cua truc hoanh
if neg and pos:
    print(-1)
    exit()

# chat nhi phan ket qua
l = 0.0
r = 100000000000000.0
for _ in range(300):
    mid = (l+r)/2
    if check(mid):
        r = mid
    else:
        l = mid
print(l)
