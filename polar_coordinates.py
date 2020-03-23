# -*- coding: utf-8 -*-

import numpy as np
import math

def o2p(x,y):
    return [(x**2+y**2)**0.5,np.arctan(y/x)]

#def o2p(ball):
    
d=[[-178.45,209.4],[0,209.4],[178.45,209.4],[-178.45,30.6],[0,30.6],[178.45,30.6]]

    
def choose(p):
    m = 0
    mini = 500
    for i in range(6):
        dis=((d[i][0]-p[0])**2+(d[i][1]-p[1])**2)**0.5
        if (dis < mini):
            mini = dis
            m = i
    return m, mini

