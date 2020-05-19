import gym
import gym_findexit
import numpy as np
import element

# inicializar entorno
env = gym.make('findexit-v0')
env.reset()
print(env.action_space)


for i in range(1000):
    reward = env.step(np.random.randint(0, 4))
    if reward == 1:
        print("we did it in step " + str(i))
        break

