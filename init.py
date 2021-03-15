import numpy as np
import random

class initiation:
	Map = [[0 for x in range(50)] for y in range(50)]
	#job vector definition

	job_counter=5
	drone_counter=4#random.randrange(1,5)
	coor_job =np.array([(0,0)]*job_counter)
	coor_target =np.array([(0,0)]*job_counter)
	coor_drone =np.array([(0,0)]*drone_counter)
	for i in range(job_counter):
		coor_job[i] = (random.randrange(20),random.randrange(20))
		coor_target[i] = (random.randrange(20),random.randrange(20))

	for j in range(drone_counter):
		coor_drone[j] = (random.randrange(20),random.randrange(20))

	Job = np.zeros((job_counter,6))
	V =np.array([0]*drone_counter)

	for i in range(job_counter):
		Job[i][0] = i
		Job[i][3] = random.randrange(1,10)
		Job[i][4] = -1
		Job[i][5] = random.randrange(0,30)

	result = np.zeros((job_counter,drone_counter))

	max_time=0
	for i in range(job_counter):
		max_time+=Job[i][3]

	Drone =np.zeros((drone_counter,20*max_time.astype(int)))
