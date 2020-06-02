import gym
import gym_findexit
import numpy as np
import sys
import random



LEARNING_RATE = 0.5
DISCOUNT_RATE = 0.95
EPISODE_STEPS = 200
EPISODES = 1000000
EXPLORATION = 0.990
SHOW_EPISODE = 100

# inicializar entorno
env = gym.make('findexit-v0')

# inicializar q table (valores random de 0 a 4 por ahora. considerar inicializar a 0)
q_table = {}
for x in range(-env.observation_space + 1, env.observation_space):
    for y in range(-env.observation_space + 1, env.observation_space):
        #q_table[(x, y)] = [np.random.uniform(0, 4) for i in range(4)]
        q_table[x, y] = [0 for i in range(4)]
np.set_printoptions(threshold=sys.maxsize)
print(q_table)




env.reset()
print(env.action_space)

for episode in range(EPISODES):
    current_ob = env.reset()
    previous_ob = current_ob
    print("episode: " + str(episode))

    for step in range(EPISODE_STEPS):
        # exploración o explotación
        if EXPLORATION > np.random.uniform(0, 1):
            # explotacion
            action = np.argmax(q_table[current_ob])
        else:
            # exploracion
            action = np.random.randint(0, 4)


        # ejecutamos el step utilizando este valor como acción
        reward, current_ob = env.step(action)
        if reward == 1:
            print("Exit reached in step " + str(step))
            break

        # actualizamos valor de la posición en la q_table
        q_table[previous_ob][int(action)] = q_table[current_ob][int(action)] * (1 - LEARNING_RATE) + LEARNING_RATE * (reward + DISCOUNT_RATE * np.max(q_table[current_ob][int(action)]))
        previous_ob = current_ob

        # mostrar gráficamente si toca
        if episode % SHOW_EPISODE == 0:
            env.render()

'''

    
    TODO: - posicion inicial aleatoria (pero valida)
          - entender mejor la back-propagation
          - probar si la q_table se esta actualizando correctamente
          - pillow para mostrar graficamente
    
'''

