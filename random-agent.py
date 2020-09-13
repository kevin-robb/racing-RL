# requires OpenAI Gym CarRacing-v0 environment

# Easiest continuous control task to learn from pixels, 
# a top-down racing environment. Discrete control is reasonable 
# in this environment as well, on/off discretization is fine. 
# State consists of 96x96 pixels. Reward is -0.1 every frame and +1000/N 
# for every track tile visited, where N is the total number of tiles in track. 
# For example, if you have finished in 732 frames, your reward 
# is 1000 - 0.1*732 = 926.8 points. Episode finishes when all tiles are visited. 
# Some indicators shown at the bottom of the window and the state RGB buffer. 
# From left to right: true speed, four ABS sensors, steering wheel position, gyroscope.

# To play yourself, go to the gym repository and run:
# python3 gym/envs/box2d/car_racing.py
# Up arrow to accelerate, left/right arrow to turn front wheels

import gym
env = gym.make('CarRacing-v0')
env.reset()
#print(env.action_space.sample())

#TODO:  determine how to create actions to send rather than from sample().
#       send actions to have car go straight.
#       understand box object & what different entries mean for the commanded action.

for _ in range(1000):
    env.render()
    env.step(env.action_space.sample()) # take a random action
env.close()