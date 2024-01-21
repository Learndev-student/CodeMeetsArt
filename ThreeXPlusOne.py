#3x+1
import matplotlib.pyplot as plt
import math
colors = ["red","blue","green","violet","cyan"]
plt.axes().set_facecolor("black")
def f(a):
    if a%2==0:
        return a/2
    else:
        return 3*a+1

for i in range(2,500):
        a = i
        x = []
        y = []
        k = 1
        while a!=1:
            k = k+1
            a = f(a)
            x.append(a*math.cos(k/10))
            y.append((a+100)*math.sin(k/10))
        plt.plot(x,y,color=colors[i%5],linewidth=0.01)
plt.savefig("new.png",dpi=2000)
plt.show()
