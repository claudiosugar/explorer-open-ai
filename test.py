import gym
import gym_findexit
import numpy as np
import sys
import random

# inicializar q table (valores random de 0 a 4 por ahora. considerar inicializar a 0)
q_table = {}
for x in range(-9, 10):
    for y in range(-9, 10):
        q_table[(x, y)] = [np.random.uniform(0, 4) for i in range(4)]
        #q_table[x, y] = [0 for i in range(4)]
np.set_printoptions(threshold=sys.maxsize)
print(q_table)

LEARNING_RATE = 0.5
DISCOUNT_RATE = 0.95
EPISODE_STEPS = 200
EPISODES = 1000000
EXPLORATION = 0.99

# inicializar entorno
env = gym.make('findexit-v0')
env.reset()
print(env.action_space)

# posicion inicial (tengo que cambiar esto)
current_ob = (5, 0)
previous_ob = (5, 0)

for episode in range(EPISODES):
    # hay que resetear posicion inicial en funcion reset
    env.reset()
    current_ob = (5, 0)
    previous_ob = (5, 0)
    print("episode: " + str(episode))
    for step in range(EPISODE_STEPS):
        # exploración o explotación
        if EXPLORATION > np.random.uniform(0, 1):
            # explotacion
            action = np.argmax(q_table[current_ob])
        else:
            # exploracion
            action = np.random.randint(0, 1)


        # ejecutamos el step utilizando este valor como acción
        reward, current_ob = env.step(action)
        if reward == 1:
            print("Exit reached in step " + str(step))
            break

        # actualizamos valor de la posición en la q_table

        q_table[previous_ob][int(action)] = q_table[current_ob][int(action)] * (1 - LEARNING_RATE) + LEARNING_RATE * (reward + DISCOUNT_RATE * np.max(q_table[current_ob][int(action)]))
        previous_ob = current_ob

'''

    
    TODO: - posicion inicial aleatoria (pero valida)
          - entender mejor la back-propagation
          - probar si la q_table se esta actualizando correctamente
    
'''

