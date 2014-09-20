import numpy as np
import matplotlib.pyplot as plt
import cubehelix 
# set up some simple data to plot
x = np.random.randn(10000)
y = np.random.randn(10000)
cx1 = cubehelix.cmap(startHue=240,endHue=-300,minSat=1,maxSat=2.5,minLight=.3,maxLight=.8,gamma=.9)
plt.hexbin(x,y,gridsize=50,cmap=cx1)
plt.colorbar()
#plt.savefig('rainbow.png')
