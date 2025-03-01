from matplotlib import pyplot as plt
#-->
#Linea reca: y=mx+b
#tabular para x.....
lim_inferior=-10
lim_superior=10
x=[]
for i in range(lim_inferior, lim_superior+1, 1):
    x.append(i)
print("x: ",x)
#Y=?
m=2
b=4
y=[]
for i in range(len(x)):
    y.append(m*x[i]+b)
print("Y: ", y)

plt.plot(x,y)
plt.show()
