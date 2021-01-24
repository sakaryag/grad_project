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
        for x in range( time.astype(int)+Functions.g(job,drone)+Functions.r(job,drone)):
            initiation.Drone[drone][x+t]=1
        return 1;


    def assign(self):
        for e in range(EPISODES):

            #print(initiation.Job)
            number_feature = 1
            agent = DQN.DQNAgent(initiation.job_counter, number_feature)
            agent.load("./save/my_method.h5")
            batch_size = 5#initiation.job_counter * initiation.drone_counter
            history = []
            successnumber = 0
            done=False
            total_time =0
            arr=[0]
            state = np.array(arr*initiation.job_counter)
            state = [np.reshape(state[i], (1, 1,)) for i in range(initiation.job_counter)]

            action_list = []
            oldtotal_time = 0
            total_time = 0

            for i in range(100*initiation.job_counter):
                action = agent.act(state)
                if(initiation.Job[action][4].astype(int)==-1):
                    time= initiation.Job[action][3]
                    work_time = Functions.g(action,i%initiation.drone_counter)+Functions.r(action,i%initiation.drone_counter)+time.astype(int)
                    state[[action][0]]=1
                    state = [np.reshape(state[k], (1, 1,)) for k in range(initiation.job_counter)]
                    next_state=state
                    for j in range(initiation.Job[i%initiation.drone_counter][5].astype(int),10*initiation.max_time.astype(int)):
                        if(Functions.check_availability(i%initiation.drone_counter,j,j+work_time)==1):
                            initiation.Job[action][4] =j
                            break
                    method.assign_operation(self,action,i%initiation.drone_counter,initiation.Job[action][4].astype(int))
                    #print(i%initiation.drone_counter ,action ,initiation.Job[action][4].astype(int),initiation.Job[action][4].astype(int)+work_time)
                    total_time = initiation.Job[action][4]-initiation.Job[action][5] + work_time
                    reward = oldtotal_time - total_time
                    oldtotal_time = total_time
                    agent.remember(state, action, reward, next_state)
                    state = next_state


                    # record the history
                    action_list.append(action)
                    agent.save("./save/my_method.h5")
                    done=False
                else:
                    done=True
                #if len(agent.memory) > batch_size:
                #    agent.replay(batch_size)

            total_waiting=0


            for i in range(initiation.job_counter):
                total_waiting+=initiation.Job[i][4]-initiation.Job[i][5]
            print(total_waiting/initiation.job_counter)
            #print(initiation.Job)

            #print(initiation.result)

            for i in range(initiation.job_counter):
                initiation.Job[i][4]=-1
            initiation.Drone.fill(0)
            #temp = input()
        return 0
