# -*- coding: utf-8 -*-
import random
from collections import deque
from init import initiation
import keras
import numpy as np
from keras.layers import Dense, Input
from keras.models import Model, Sequential
from keras.optimizers import Adam
from keras.utils import plot_model
import matplotlib.pyplot as plt



class DQNAgent:
    # class for deep q learning agent

    def __init__(self, number_job, number_feature):
        self.number_job = number_job
        self.number_feature = number_feature
        self.memory = deque(maxlen=2000)
        self.epsilon = 0.3  # exploration rate
        self.gamma = 0.95    # discount rate
        self.epsilon_min = 0.01
        self.epsilon_decay = 0.995
        self.learning_rate = 0.0005
        self.model = self._build_subproblem_model() # build the model
    def replay(self, batch_size):
            # replay the history and train the model

            minibatch = random.sample(self.memory, batch_size)

            for state, action, reward, next_state, done in minibatch:
                state = [np.reshape(state[k], (1, 1,)) for k in range(initiation.job_counter)]
                next_state = [np.reshape(next_state[k], (1, 1,)) for k in range(initiation.job_counter)]
                target = reward
                if not done:
                    target = (reward + self.gamma *
                              np.amax(self.model.predict(next_state)[0]))
                target_f = self.model.predict(state)
                target_f[0][action] = target

                history = self.model.fit(state, target_f, epochs=40, verbose=0)#self.model.fit(state, target_f, epochs=1, verbose=0)

            if self.epsilon > self.epsilon_min:
                self.epsilon *= self.epsilon_decay

    def _build_subproblem_model(self):
        # to build the whole model

        basic_model = self._submodel()

        output_list = []
        input_list = []
        for i in range(self.number_job):
            input_list.append(Input(shape=(self.number_feature,)))
            output_list.append(basic_model(input_list[i]))

        concatenated = keras.layers.concatenate(output_list)
        out = Dense(self.number_job, activation='linear')(concatenated)
        model = Model(input_list, out)
        model.compile(loss='mse',
                      optimizer=Adam(lr=self.learning_rate))

        plot_model(model, to_file="gorkem_model.png", show_shapes=True)

        return model

    def _submodel(self):
        # the sub model called by function  _build_subproblem_model

        model = Sequential(name='basic_model')
        model.add(Dense(24, input_dim=self.number_feature, activation='relu'))
        model.add(Dense(24, input_dim=self.number_feature, activation='relu'))
        model.add(Dense(24, input_dim=self.number_feature, activation='relu'))
        model.add(Dense(24, input_dim=self.number_feature, activation='relu'))
        model.add(Dense(24, input_dim=self.number_feature, activation='relu'))
        model.add(Dense(24, activation='relu'))
        model.add(Dense(1, activation='linear'))
        model.compile(loss='mse',
                      optimizer=Adam(lr=self.learning_rate))
        return model


    def remember(self, state, action, reward, next_state,done):
        # remember the information of this step

        self.memory.append((state, action, reward, next_state,done))

    def act(self, state):
        # let the agent make a decision
        # choose a job to process in current state

        if np.random.rand() <= self.epsilon:
            return random.randrange(self.number_job)
        act_values = self.model.predict(state)
        #print("Epsilon:",self.epsilon)

        return np.argmax(act_values[0])  # returns action





    def load(self, name):
        # load the model
        self.model.load_weights(name)

    def save(self, name):
        # save the model
        self.model.save_weights(name)
