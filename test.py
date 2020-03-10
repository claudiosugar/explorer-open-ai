import gym
import gym_findexit
import numpy as np
import element

# inicializar entorno
env = gym.make('findexit-v0')
env.reset()


for i in range(10):
    env.step(np.random.randint(0, 3))
