# -*- coding: utf-8 -*-

import os
import numpy as np
import matplotlib.pyplot as plt

def f(x):
	return "{0:.2f}".format(1/3*np.sin(1.5*x)+4/3)

bars="\draw[line width=3pt] (0,0) -- (0,0"+str(f(0))+")\n"

path="\draw (0,"+str(f(0))+") to [curve through={"
for k in np.arange(0.4,5,0.4):
	path+='('+ str(k)+','+str(f(k))+') .. '
	bars+="                           ("+str(k)+",0) -- ("+str(k)+","+str(f(k))+")\n"

path+="(4.8,"+ str(f(4.8))+")}] (5,"+str(f(5))+");"

print(str(bars)+";")

print(path)