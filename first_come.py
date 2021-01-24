from init import initiation
from functions import Functions
import numpy as np
class method(initiation):

    def __init__(self):
            self.assign()
    def assign_operation(self,job):

        time= initiation.Job[job][3]
        for t in range(6*initiation.max_time.astype(int)):
            if(initiation.Job[job][5]<=t):
                for y in range(initiation.drone_counter):
                    if(Functions.check_availability(y,t,t+Functions.g(job,y)+Functions.r(job,y)+time.astype(int))==1):
                        initiation.result[job][y]=1
                        initiation.Job[job][4]=t+Functions.g(job,y)
                        print(y ,job ,t,t+Functions.g(job,y)+Functions.r(job,y)+time.astype(int))
                        for x in range( time.astype(int)+Functions.g(job,y)+Functions.r(job,y)):
                            initiation.Drone[y][x+t]=1
                        return 1;
        return 0;

    def assign(self):

        print('2D Numpy Array')
        print(initiation.Job)
        columnIndex = 5
        sortedArr = initiation.Job[initiation.Job[:,columnIndex].argsort()]
        print('Sorted 2D Numpy Array')
        sortedArr=sortedArr.astype(int)
        print(sortedArr)

        for x in range(initiation.job_counter):
            method.assign_operation(self,sortedArr[x][0])
        total_waiting=0
        for i in range(initiation.job_counter):
            total_waiting+=initiation.Job[i][4]-initiation.Job[i][5]
        print(total_waiting/initiation.job_counter)
        print(initiation.Job)

        print(initiation.result)

        return 0
