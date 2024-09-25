import os
import math
import matplotlib.pyplot as plt
import matplotlib.pylab as mp
import numpy as np
import matplotlib.cm as cm
import matplotlib.colors as mcolors


from mpl_toolkits.mplot3d import Axes3D


x=np.arange(100,400,10)#伤害
y=np.arange(5,35,1)#弹匣
z=np.arange(1.0,2.5,0.05)#后坐力


aaa=(x*0.5+y)/z


fig=plt.figure()

ax = fig.add_subplot(111, projection='3d')   

mp.title("AWP effort analysis",fontsize=20)

ax.set_xlabel('damage', fontsize=14)
ax.set_ylabel('clip', fontsize=14)
ax.set_zlabel('recoil', fontsize=14)

mp.tick_params(labelsize=10)

ax.plot(x,y,z,color='red')
mp.show()

#test
#print(z)
#print(z.size)
#zx=0.5*(x)
#print(zx)