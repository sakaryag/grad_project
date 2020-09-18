import numpy as np

class initiation:
    Map = [[0 for x in range(50)] for y in range(50)]
    #job vector definition

    #job vector definition
    job_counter=10
    drone_counter=4

    coor_job =np.array([(0,0)]*job_counter)
    coor_target =np.array([(0,0)]*job_counter)
    coor_drone =np.array([(0,0)]*drone_counter)

    coor_job[0]=(3,0)
    coor_job[1]=(3,2)
    coor_job[2]=(3,5)
    coor_job[3]=(7,5)
    coor_job[4]=(12,5)
    coor_job[5]=(17,4)
    coor_job[6]=(17,1)
    coor_job[7]=(11,1)
    coor_job[8]=(1,11)
    coor_job[9]=(7,3)
    #
    coor_target[0]=(0,0)
    coor_target[1]=(0,4)
    coor_target[2]=(0,0)
    coor_target[3]=(0,10)
    coor_target[4]=(0,3)
    coor_target[5]=(0,19)
    coor_target[6]=(17,0)
    coor_target[7]=(0,10)
    coor_target[8]=(0,0)
    coor_target[9]=(0,0)

    #
    coor_drone[0]=(5,6)
    coor_drone[1]=(14,1)
    coor_drone[2]=(8,2)
    coor_drone[3]=(5,5)


    #Job[][0]=ID
    #Job[][1]=vector
    #Job[][2]=type
    #Job[][3]=duration
    #Job[][4]=assign time
    #Job[][5]=arrival_time
    Job = np.zeros((job_counter,6))
    V =np.array([0]*drone_counter)

    Job[0][0]=0
    Job[0][3]=3
    Job[0][4]=-1
    Job[0][5]=0

    Job[1][0]=1
    Job[1][3]=4
    Job[1][4]=-1
    Job[1][5]=0
    #
    Job[2][0]=2
    Job[2][3]=5
    Job[2][4]=-1
    Job[2][5]=0
    #
    Job[3][0]=3
    Job[3][3]=3
    Job[3][4]=-1
    Job[3][5]=20
    #
    Job[4][0]=4
    Job[4][3]=3
    Job[4][4]=-1
    Job[4][5]=20
    #
    Job[5][0]=5
    Job[5][3]=4
    Job[5][4]=-1
    Job[5][5]=10
    #
    Job[6][0]=6
    Job[6][3]=6
    Job[6][4]=-1
    Job[6][5]=10
    #
    Job[7][0]=7
    Job[7][3]=4
    Job[7][4]=-1
    Job[7][5]=30
    #
    Job[8][0]=8
    Job[8][3]=5
    Job[8][4]=-1
    Job[8][5]=20
    #
    Job[9][0]=9
    Job[9][3]=3
    Job[9][4]=-1
    Job[9][5]=10

    #W_ij
    result = np.zeros((job_counter,drone_counter))

    max_time=0
    for i in range(job_counter):
        max_time+=Job[i][3]

    Drone =np.zeros((drone_counter,10*max_time.astype(int)))
