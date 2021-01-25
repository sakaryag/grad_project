from init import initiation
from functions import Functions
from my_queue import PriorityQueue
import numpy as np

import DQN

EPISODES = 10000

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
        for e in range(EPISODES):       # episodes for train    ####will be commented
            for i in range(initiation.job_counter):
                initiation.Job[i][4]=-1          # 4 th element of array corresponds assign time / at the beginning assign them all  ####will be commented
            initiation.Drone.fill(0)        # remove all jobs from drones
            #print(initiation.Job)
            number_feature = 1
            agent = DQN.DQNAgent(initiation.job_counter, number_feature)
            agent.load("./save/my_method.h5")       # load the saved data of agent
            batch_size = initiation.job_counter * initiation.drone_counter
            done=False
            total_time =0
            arr=[0]
            state = np.array(arr*initiation.job_counter)
            state = [np.reshape(state[i], (1, 1,)) for i in range(initiation.job_counter)]  ## state for jobs 0(wait) or 1(assigned)
            next_state=state
            action_list = []        ## list to predict job
            total_time = 0          ## total time of waiting time of job and going + returning time of drone
            oldtotal_time = 0       ## total time is used for giving reward

            for i in range(500):  # because of the random assign, there should be more iterations  # REVIEW: should find better way
                action = agent.act(state)       # act function decides to the action
                if(initiation.Job[action][4].astype(int)==-1):  # if the selected job is not assigned before
                    time= initiation.Job[action][3]
                    work_time = Functions.g(action,i%initiation.drone_counter)+Functions.r(action,i%initiation.drone_counter)+time.astype(int)
                    state[[action][0]]=1    ## assigned the "action" th cell of state as 1
                    state = [np.reshape(state[k], (1, 1,)) for k in range(initiation.job_counter)]  # reshape state suitable for act function array of arrays
                    for j in range(initiation.Job[i%initiation.drone_counter][5].astype(int),10*initiation.max_time.astype(int)):
                        if(Functions.check_availability(i%initiation.drone_counter,j,j+work_time)==1):      ##check_availability of the drone to "action"th job at first possible time
                            initiation.Job[action][4] =j
                            break
                    method.assign_operation(self,action,i%initiation.drone_counter,initiation.Job[action][4].astype(int)) ## assign
                    #print(i%initiation.drone_counter ,action ,initiation.Job[action][4].astype(int),initiation.Job[action][4].astype(int)+work_time)
                    total_time = initiation.Job[action][4]-initiation.Job[action][5] + work_time
                    reward = oldtotal_time - total_time             ##  reward if given according to total time;  if the current total time is smaller than the previous reward is bigger
                    oldtotal_time = total_time
                    agent.remember(state, action, reward, next_state,done)  ## save the state to agent
                    next_state = [np.reshape(state[k], (1, 1,)) for k in range(initiation.job_counter)]  # reshape state suitable for act function array of arrays
                    state = next_state
                    action_list.append(action)      #append action to list
                    done=True

                    if len(agent.memory) > batch_size:
                        agent.replay(batch_size)

                else:
                    done=True


            total_waiting=0
                # record the history
            if e % 10 == 0:             ## will be commented
                agent.save("./save/my_method.h5")   ## save agent

            for i in range(initiation.job_counter):
                total_waiting+=initiation.Job[i][4]-initiation.Job[i][5]        ## calculate the waiting time / i tried to minimize that
            print(total_waiting/initiation.job_counter)
            #print(initiation.Job)

            #print(initiation.result)


        return 0
