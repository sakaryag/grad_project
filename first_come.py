from init import initiation
from functions import Functions
import numpy as np
class method(initiation):

    def assign_operation(job):

        time= initiation.Job[job][3]
        for t in range(initiation.max_time.astype(int)):
            if(initiation.Job[job][5]<=t):
                for y in range(initiation.drone_counter):
                    if(Functions.check_availability(y,t,t+Functions.g(job,y)+Functions.r(job,y)+time.astype(int))==1):
                        initiation.result[job][y]=1
                        initiation.Job[job][4]=t+Functions.g(job,y)
                        print(y ,job ,t,t+Functions.g(job,y)+Functions.r(job,y)+time.astype(int))
                        for x in range( time.astype(int)+t+Functions.g(job,y)+Functions.r(job,y)):
                            initiation.Drone[y][x+t]=1
                        return 1;
        return 0;

    def assign(sth):

        print('2D Numpy Array')
        print(initiation.Job)
        columnIndex = 5
        sortedArr = initiation.Job[initiation.Job[:,columnIndex].argsort()]
        print('Sorted 2D Numpy Array')
        sortedArr=sortedArr.astype(int)
        print(sortedArr)

        for x in range(initiation.job_counter):
            method.assign_operation(sortedArr[x][0])

        print(initiation.result)

        return sth
