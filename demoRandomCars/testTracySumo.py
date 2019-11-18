# -*- coding: utf-8 -*-
"""
Created on Sun Nov 10 11:07:01 2019

@author: Gabriel
"""
import agentSUMOv2 as ag
import envSUMO as se
import matplotlib.pyplot as plt


env_train = se.SumoEnv(gui_f=False)
env_test = se.SumoEnv(gui_f=True)
print('already loaded enviroments')
print('env_train:{}'.format(env_train))
print('env_test:{}'.format(env_test))
agent = ag.Agent()

EPS = 20
arrayTimes=[]
for ieps in range(EPS):
    for i in range(20):
        state = env_train.reset()
        done = False
        while not done:
            action = agent.policy(state)
            wt,next_state, reward, done, rewards = env_train.step_d(action)
            arrayTimes.append(wt)
            agent.train(state, action, reward, 0.001, [1, 1, done, 1, 1])

            state = next_state
        env_train.close()

    state = env_test.reset()
    done = False
    while not done:
        action = agent.policy(state)
        next_state, reward, done, rewards = env_test.step_d(action)
        print(state)

        state = next_state
    env_test.close()
    
plt.plot(arrayTimes)
plt.ylabel('Waiting Time')
plt.show()