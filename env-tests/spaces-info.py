import gym
env = gym.make('CarRacing-v0')
print(env.action_space)
#> Discrete(2)
print(env.observation_space)
#> Box(4,)
print(env.action_space.n)
