import gym

import argparse
import os
import sys
sys.path.append(r'.\Reinforcement Learning')
import Env_agent_exploration_Sumo

if 'SUMO_HOME' in os.environ:
    tools = os.path.join(os.environ['SUMO_HOME'], 'tools')
    sys.path.append(tools)
else:
    sys.exit("Please declare the environment variable 'SUMO_HOME'")
import pandas as pd
from gym import spaces
import numpy as np
from Env_agent_exploration_Sumo.environment.env import SumoEnvironment
from Env_agent_exploration_Sumo.util.gen_route import write_route_file
import traci

from stable_baselines.common.policies import MlpPolicy
from stable_baselines.common.vec_env import SubprocVecEnv
from stable_baselines import A2C

#write_route_file('nets/2way-single-intersection/single-intersection-gen.rou.xml', 400000, 100000)

# multiprocess environment
if __name__ == '__main__':
    n_cpu = 1
    env = SubprocVecEnv([lambda: SumoEnvironment(net_file='./Net/simple.net.xml',
                                        route_file='./Net/trips.trips.xml',
                                        out_csv_name='./Reinforcement Learning/A2C/Outputs/a2c',
                                        single_agent=True,
                                        use_gui=True,
                                        num_seconds=5000,
                                        min_green=5,
                                        time_to_load_vehicles=120,
                                        max_depart_delay=0,
                                        phases=[
                                            traci.trafficlight.Phase(42, "GGGggrrrrrGGGggrrrrr"),  
                                            traci.trafficlight.Phase(20, "yyyyyrrrrryyyyyrrrrr"),
                                            traci.trafficlight.Phase(42, "rrrrrGGGggrrrrrGGGgg"),   
                                            traci.trafficlight.Phase(20, "rrrrryyyyyrrrrryyyyy")
                                            ]) for i in range(n_cpu)])
    
    model = A2C(MlpPolicy, env, verbose=1, learning_rate=0.0001, lr_schedule='constant')
    model.learn(total_timesteps=1000000)
