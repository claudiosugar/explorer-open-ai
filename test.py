import gym
import gym_findexit
import numpy as np

# inicializar q table
q_table = {}
for x1 in range(-9, 10):
    for y1 in range(-9, 10):
                q_table[(x1, y1)] = [np.random.uniform(0, 4) for i in range(4)]
print(q_table)



# inicializar entorno
env = gym.make('findexit-v0')
env.reset()
print(env.action_space)


for i in range(1):
    reward, ob = env.step(np.random.randint(0, 4))
    print("ob = " + str(ob))
    if reward == 1:
        print("Exit reached in step " + str(i))
        break

'''

    max_future_q = np.max(q_table[ob])
    
    current_q = q_table[obs][action]
    
    new q = (1 - LEARNING_RATE) * current_q + LEARNING_RATE * (reward + DISCOUNT * max_future_q)
    
    q_table[obs][action] = new_q

'''

