from init import initiation
import numpy as np
from functions import Functions
from my_queue import PriorityQueue


class method(initiation):
	def __init__(self):
		  self.assign()
	def assign_operation(self,job,t):

		time= initiation.Job[job][3]
		for y in range(initiation.drone_counter):
			if(Functions.check_availability(y,t,t+Functions.g(job,y)+Functions.r(job,y)+time.astype(int))==1):
				initiation.result[job][y]=1
				initiation.Job[job][4]=t+Functions.g(job,y)
				#print(y ,job ,t,Functions.g(job,y),Functions.r(job,y),time.astype(int))
				for x in range( time.astype(int)+Functions.g(job,y)+Functions.r(job,y)):
					initiation.Drone[y][x+t]=1
				return 1;
		return 0;

	def assign(self):

		#print('2D Numpy Array')
		#print(initiation.Job)

		sortedArr=np.array(sorted(sorted(initiation.Job,key=lambda e:e[3]),key=lambda e:e[5]))
		#print('Sorted 2D Numpy Array')
		sortedArr=sortedArr.astype(int)
		queue = PriorityQueue()

		#print(sortedArr)
		temp = np.zeros(initiation.job_counter)
		for t in range(6*initiation.max_time.astype(int)):
			count=0
			for x in range(initiation.job_counter):
				if(initiation.Job[sortedArr[x][0]][4]==-1):
					if(sortedArr[x][5]<=t):
						queue.insert(sortedArr[x][0])
						count+=1
			while not queue.isEmpty():
				method.assign_operation(self,queue.delete(),t)
		total_waiting=0
		for i in range(initiation.job_counter):
			total_waiting+=initiation.Job[i][4]-initiation.Job[i][5]
		print("Result for Shortest Time First",total_waiting/initiation.job_counter)
		#print(initiation.Job)

		for i in range(initiation.job_counter):
			initiation.Job[i][4] = -1
		initiation.Drone =np.zeros((initiation.drone_counter,20*initiation.max_time.astype(int)))
		initiation.result = np.zeros((initiation.job_counter,initiation.drone_counter))
		#print(initiation.result)

		return 0
