from init import initiation
from functions import Functions
from my_queue import PriorityQueue
import first_come
import numpy as np
import shortest_time
import my_method
class method(initiation):

	def __init__(self):
			my_method.method()
			first_come.method()
			shortest_time.method()

			self.assign()
	def max(self,a,b):
		if (a>b):
			return a
		return b

	def assign_operation(self,job,drone,t):

		time= initiation.Job[job][3]
		initiation.result[job][drone]=1
		initiation.Job[job][4]=t+Functions.g(job,drone)
		for x in range( time.astype(int)+Functions.g(job,drone)+Functions.r(job,drone)):
			initiation.Drone[drone][x+t]=1
		return 1;


	def assign(self):
		#print(initiation.Job)


		for y in range(initiation.job_counter):
			as_time=PriorityQueue()

			for x in range(initiation.job_counter):
				time= initiation.Job[x][3]
				for t in range(10*initiation.max_time.astype(int)):
					if(initiation.Job[x][4]==-1):
						if(Functions.check_availability(y%initiation.drone_counter,t,t+Functions.g(x,y%initiation.drone_counter)+Functions.r(x,y%initiation.drone_counter)+time.astype(int))==1):
							temp=method.max(self,t,initiation.Job[x][5].astype(int))
							as_time.insert((x,temp,Functions.g(x,y%initiation.drone_counter)+Functions.r(x,y%initiation.drone_counter)+time.astype(int)))
							break;
		#    print(as_time)
			tem=as_time.delete_dif()
			#j,t=tem
			time= initiation.Job[tem[0]][3]
			method.assign_operation(self,tem[0],y%initiation.drone_counter,tem[1])
			#print(y%initiation.drone_counter ,tem[0] ,tem[1],tem[1]+Functions.g(tem[0],y%initiation.drone_counter)+Functions.r(tem[0],y%initiation.drone_counter)+time.astype(int))

		total_waiting=0
		for i in range(initiation.job_counter):
			total_waiting+=initiation.Job[i][4]-initiation.Job[i][5]
		print("Result For My New Method",total_waiting/initiation.job_counter)
		#print(initiation.Job)

		#print(initiation.result)
		for i in range(initiation.job_counter):
			initiation.Job[i][4] = -1
		initiation.Drone =np.zeros((initiation.drone_counter,20*initiation.max_time.astype(int)))
		initiation.result = np.zeros((initiation.job_counter,initiation.drone_counter))
		return 0
