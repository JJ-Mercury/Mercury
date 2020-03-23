# -*- coding: utf-8 -*-
import sim as vrep
import time

def move(handle, theta, clientID):
    if len(handle)!=len(theta) or len(handle)!=4:
        return -1
    vrep.simxPauseCommunication(clientID,True)
    vrep.simxSetJointTargetPosition(clientID, handle[1], theta[1], vrep.simx_opmode_oneshot) 
    vrep.simxPauseCommunication(clientID,False)
    time.sleep(7)
    vrep.simxPauseCommunication(clientID,True)
    vrep.simxSetJointTargetPosition(clientID, handle[2], theta[2], vrep.simx_opmode_oneshot) 
    vrep.simxPauseCommunication(clientID,False)
    time.sleep(7)
    vrep.simxPauseCommunication(clientID,True)
    vrep.simxSetJointTargetPosition(clientID, handle[0], theta[0], vrep.simx_opmode_oneshot) 
    vrep.simxPauseCommunication(clientID,False)
    time.sleep(7)
    return 0
def hit(hammer, clientID):
    vrep.simxPauseCommunication(clientID,True)
    vrep.simxSetJointTargetPosition(clientID, hammer, -0.7,vrep.simx_opmode_oneshot) 
    vrep.simxPauseCommunication(clientID,False)
    time.sleep(10)
    vrep.simxPauseCommunication(clientID,True)
    vrep.simxSetJointTargetPosition(clientID, hammer,  0,vrep.simx_opmode_oneshot) 
    vrep.simxPauseCommunication(clientID,False)
    time.sleep(5)
    return 0


