import numpy as np
import random

class initiation:
	Map = [[0 for x in range(50)] for y in range(50)]


	job_counter=50
	drone_counter=4#random.randrange(1,5)
	coor_job =np.array([(0,0)]*job_counter)
	coor_target =np.array([(0,0)]*job_counter)
	coor_drone =np.array([(0,0)]*drone_counter)
	grid =50
	for i in range(job_counter):
		coor_job[i] = (random.randrange(grid),random.randrange(grid))
		coor_target[i] = (random.randrange(grid),random.randrange(grid))

	for j in range(drone_counter):
		coor_drone[j] = (random.randrange(grid),random.randrange(grid))

	Job = np.zeros((job_counter,6))
	V =np.array([0]*drone_counter)
	mean = 90
	dev = 30
	np.random.seed(0)

	jobDur = np.random.normal(mean,dev, job_counter).astype(int)


	   # Arrival Times - Poisson arrivals => exponential dist.
	arrMean = 50
	jobArr = np.random.exponential(arrMean, job_counter).astype(int)

	jobArr = np.cumsum(jobArr)

	jobs = np.stack((jobArr, jobDur), axis=-1)

	for i in range(job_counter):
		Job[i][0] = i
		Job[i][3] = jobs[i][1]
		Job[i][4] = -1
		Job[i][5] = jobs[i][0]


	result = np.zeros((job_counter,drone_counter))

	max_time=0
	for i in range(job_counter):
		max_time+=Job[i][3]

	Drone =np.zeros((drone_counter,20*max_time.astype(int)))
