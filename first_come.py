from init import initiation
from functions import Functions
import numpy as np
class method(initiation):

    def assign_operation(job):

        time= initiation.Job[job][3]
        #waiting queue for job>drone
        for y in range(initiation.drone_counter):
            if(Functions.check_availability(y,job)==1):
                initiation.result[job][y]=1
                for x in range(initiation.Job[job][3].astype(int)):
                    initiation.Drone[y][x]=1
                return 1;
        return 0;

    def assign( sth):


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
