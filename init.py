import numpy as np

class initiation:
    Map = [[0 for x in range(50)] for y in range(50)]
    #job vector definition
    #job vector definition
    job_counter=6
    drone_counter=6
    #Job[][0]=ID
    #Job[][1]=vector
    #Job[][2]=type
    #Job[][3]=duration
    #Job[][4]=assign time
    #Job[][5]=arrival_time
    Job = np.zeros((job_counter,6))
    Drone =np.zeros((drone_counter,50))
    V =np.array([6]*drone_counter)
    Job[0][0]=0
    Job[0][3]=5
    Job[0][5]=0
    #
    Job[1][0]=1
    Job[1][3]=10
    Job[1][5]=0
    #
    Job[2][0]=2
    Job[2][3]=3
    Job[2][5]=0
    #
    Job[3][0]=3
    Job[3][3]=5
    Job[3][5]=4
    #
    Job[4][0]=4
    Job[4][3]=10
    Job[4][5]=4
    #
    Job[5][0]=5
    Job[5][3]=3
    Job[5][5]=4
    #W_ij
    result = np.zeros((job_counter,drone_counter))
