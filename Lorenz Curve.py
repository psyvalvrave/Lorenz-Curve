# -*- coding: utf-8 -*-
"""
Created on Tue Mar 26 14:34:26 2019

@author: zhech
"""

import numpy as np
import matplotlib.pyplot as plt

npdata=np.cumsum(np.sort(np.load('pop2010.npy')))
data=npdata*1.0/(npdata[-1])
print(data)
xvalue=np.arange(0,1,1/npdata.size)
plt.plot(xvalue,data, label='Lorenz Curve')#plot the real contribution
plt.plot(xvalue,xvalue, label='Real Contribution')#set the linear line
plt.title("Contribution to the Common Population")
plt.legend(loc = "best")
plt.savefig('population-lorenz.png',dpi=200)