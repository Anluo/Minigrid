#!/usr/bin/env python3

import time
import random
import gym
import gym_minigrid

import os

env_config = {
    "env_name" : "MiniGrid-Empty-16x16-v0",
    "agents_num" : 4, 
    "expert_num" : 3,
    "is_random_position" : 0,
    "size_dec_position": 1
}

env_config["agents"] = [
    {"num" : 5,  
     "position" : (3,1),
     "direction" : None,
     "color" : "red",
     "is_expert" : True,
     "carrying" : None,
     "algo" : "PPO"
   },

   {"num" : 1,  
     "position" : (1,1),
     "direction" : None,
     "color" : "red",
     "is_expert" : True,
     "carrying" : None,
     "algo" : "PPO"
   },

   {"num" : 2,  
     "position" : (2,1),
     "direction" : None,
     "color" : "red",
     "is_expert" : True,
     "carrying" : None,
     "algo" : "PPO"
   },

   {"num" : 3,  
     "position" : (4,1),
     "direction" : None,
     "color" : "blue",
     "is_expert" : False,
     "carrying" : None,
     "algo" : None
   },

]


# Load the gym environment
env = gym.make(env_config["env_name"])

obs_list = [None,None,None,None,None]
reward_list = []
done_list = []


obs_list = env.reset(**env_config)

i = 0
while True:
  print("step {}".format(i))

  action_list = []

  # Pick a random action
  for j in range(env_config["agents_num"]):
    action = random.randint(0, env.action_space.n - 1)
    action_list.append(action)

  obs_list, reward_list, done_list, info = env.step(action_list)
  env.render()

  time.sleep(0.05) #0.05

  i += 1
# Test the close method
env.close()


