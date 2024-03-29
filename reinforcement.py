from init import initiation
from functions import Functions
from my_queue import PriorityQueue
import numpy as np
import DQN
import random
import first_come
import shortest_time
import newmethod
import matplotlib.pyplot as plt

EPISODES = 20

class method(initiation):

	def __init__(self):

			self.assign()



	def max(self,a,b):
		if (a>b):
			return a
		return b

	def assign_operation(self,job,drone,t):

		time= initiation.Job[job][3]
		initiation.result[job][drone]=1
		initiation.Job[job][4]=t+Functions.g(job,drone)
		for x in range( time.astype(int)+Functions.g(job,drone)+Functions.r(job,drone)):  # assign drone for work in time(going to job+making job+returning to base)
			initiation.Drone[drone][x+t]=1  #1 means drone is in job otherwise 0
		return 1;


	def assign(self):
		number_feature = 1
		batch_size = initiation.job_counter * initiation.drone_counter*200
		agent = DQN.DQNAgent(initiation.job_counter, number_feature)
		reward=0
		best = 1000

		for m in range (EPISODES):
			max_time=0
			for i in range(initiation.job_counter):
				max_time+=initiation.Job[i][3]

			initiation.Drone = np.zeros((initiation.drone_counter,20*max_time.astype(int)))

			for i in range(initiation.job_counter):
				initiation.Job[i][4] = -1
			initiation.Drone =np.zeros((initiation.drone_counter,20*max_time.astype(int)))
			initiation.result = np.zeros((initiation.job_counter,initiation.drone_counter))

			done=False
			total_time =0
			arr=[0]
			state = np.array(arr*initiation.job_counter)
			state = [np.reshape(state[i], (1, 1,)) for i in range(initiation.job_counter)]  ## state for jobs 0(wait) or 1(assigned)
			action_list = []        ## list to predict job
			total_time = 0          ## total time of waiting time of job and going + returning time of drone
			avarage_wtime=0
			assigned_job=0
			for i in range(1000):  # because of the random assign, there should be more iterations  # REVIEW: should find better way
				action = agent.act(state)       # act function decides to the action
				if(initiation.Job[action][4].astype(int)==-1):  # if the selected job is not assigned before
					time= initiation.Job[action][3]
					work_time = Functions.g(action,i%initiation.drone_counter)+Functions.r(action,i%initiation.drone_counter)+time.astype(int)
					state[[action][0]]=1    ## assigned the "action" th cell of state as 1
					state = [np.reshape(state[k], (1, 1,)) for k in range(initiation.job_counter)]  # reshape state suitable for act function array of arrays
					for j in range(initiation.Job[action][5].astype(int),10*initiation.max_time.astype(int)):
						if(Functions.check_availability(i%initiation.drone_counter,j,j+work_time)==1):      ##check_availability of the drone to "action"th job at first possible time
							initiation.Job[action][4] =j
							break
					method.assign_operation(self,action,i%initiation.drone_counter,initiation.Job[action][4].astype(int)) ## assign

					#print(i%initiation.drone_counter ,action ,initiation.Job[action][4].astype(int)-Functions.g(action,i%initiation.drone_counter),initiation.Job[action][4].astype(int)+work_time-Functions.g(action,i%initiation.drone_counter))
					total_time = initiation.Job[action][4]-initiation.Job[action][5]
					assigned_job = assigned_job+1
					avarage_wtime = (avarage_wtime + total_time)/ assigned_job
					reward = reward + (avarage_wtime -total_time  )*500           ##  reward if given according to total time;  if the current total time is smaller than the previous reward is bigger
					agent.remember(state, action, reward, state,done)  ## save the state to agent
					action_list.append(action)      #append action to list
					done=True


				else:
					reward = reward - 100  # punishment to select already selected job
					agent.remember(state, action, reward, state,done)  ## save the state to agent
					done=True

				if len(agent.memory) > batch_size:
					agent.replay(batch_size)

			total_waiting=0
			for i in range(initiation.job_counter):
				if(initiation.Job[i][4]==-1):
					total_waiting=1000
					break
				total_waiting+=initiation.Job[i][4]-initiation.Job[i][5]        ## calculate the waiting time / i tried to minimize that


			#print(initiation.Job)
			#print(initiation.result)
			for n in range(initiation.job_counter):
				initiation.Job[n][4] = -1
			initiation.Drone =np.zeros((initiation.drone_counter,20*initiation.max_time.astype(int)))
			initiation.result = np.zeros((initiation.job_counter,initiation.drone_counter))
			flag =0
			test = total_waiting/initiation.job_counter
			if (best>test):
				best=test
			print(test)
		print(best)
		return 0
