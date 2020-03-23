# -*- coding: utf-8 -*-
"""
Created on Thu Mar 19 16:24:51 2020

@author: my13
"""

import math
import random
import sys
import sim as vrep
import numpy as np
import time
import movearm
import polar_coordinates


vrep.simxFinish(-1) # just in case, close all opened connections
clientID=vrep.simxStart('127.0.0.1',19997,True,True,5000,5)
print(clientID) # if 1, then we are connected.
if clientID!=-1:
    print("Connected to remote API server")
else:
    print("Not connected to remote API server")
    sys.exit("Could not connect")

vrep.simxStartSimulation(clientID, vrep.simx_opmode_oneshot)

time.sleep(0.5)

joint=[]
for i in range(4):
    err_code,S = vrep.simxGetObjectHandle(clientID,"J"+str(i), vrep.simx_opmode_blocking)
    
    joint.append(S)
d=[[-178.45,209.4],[0,209.4],[178.45,209.4],[-178.45,30.6],[0,30.6],[178.45,30.6]]

p = np.array([101,67])
k=polar_coordinates.choose(p)[0]

dis2 = d[k] - p
align = dis2/((dis2[0]**2 + dis2[1]**2)**0.5)
tar = p - 15*align
theta1=math.atan((p[0]-d[k][0])/(p[1]-d[k][1]))
theta2=math.atan(tar[0]/tar[1])

theta3 = math.atan(-tar[0]/tar[1])

theta=-theta1+theta2-np.pi
dis1 = (tar[0]**2+tar[1]**2)**0.5
print(tar)
print(dis1/100)
error = movearm.move(joint, [theta3,dis1/100,theta,0], clientID)

error = movearm.hit(joint[-1], clientID)
#vrep.simxSetJointTargetPosition(clientID, joint[0],np.pi/4, vrep.simx_opmode_oneshot)
#time.sleep(3)
#movearm.hit(joint[3],clientID)
#error, table = vrep.simxGetObjectHandle(clientID,"Table", vrep.simx_opmode_blocking)
#print(error)
#error, ball = vrep.simxGetObjectHandle(clientID,"Sphere", vrep.simx_opmode_blocking)
#print(error)
#error, pos = vrep.simxSetObjectPosition(clientID, ball, -1, [1,1,1],vrep.simx_opmode_streaming)

#print(error)
#error, pos = vrep.simxGetObjectPosition(clientID, ball, -1, vrep.simx_opmode_streaming)

#print(error)
#time.sleep(2)
#print(pos)

vrep.simxFinish(clientID)