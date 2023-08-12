import numpy as np
import matplotlib.pyplot as plt


# defining triangle vertices v1, v2 and v3

v1=[0,0]
v2=[20,0]
v3=[10,20]


current_point=[13,12]  # Random initial point choosen that lies inside the triangle 


# arrays to store values of p as x and y co-ordinates to plot 
resultx=[]
resulty=[]


# finding the midpoint of point p[x,y] and q[x,y]
def midpoint(p,q):
    return(0.5*(p[0]+q[0]),0.5*(p[1]+q[1]))


# iterating 100000 times for midpoint and appending each midpoint's x and y co-ordinates to resultx and resulty
for i in range(1,100000):
    n=int(1+3*np.random.uniform())

    if(n==1):
        current_point=midpoint(current_point,v1)
    if(n==2):
        current_point=midpoint(current_point,v2)
    if(n==3):
        current_point=midpoint(current_point,v3)
        
        
    resultx.append(current_point[0])
    resulty.append(current_point[1])

    

# plotting the points obtained in a scatter plot 

plt.scatter(resultx,resulty,s=1,marker='o',color="red")
plt.show()
