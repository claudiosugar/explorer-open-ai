import gym
import gym_findexit
import numpy as np

# inicializar q table (valores random de 0 a 4 por ahora. considerar inicializar a 0)
q_table = {}
for x in range(-9, 10):
    for y in range(-9, 10):
        q_table[(x, y)] = [np.random.uniform(0, 4) for i in range(4)]
        #q_table[(x, y)] = [0 for i in range(4)]
print(q_table)

LEARNING_RATE = 0.1
DISCOUNT_RATE = 0.95

# inicializar entorno
env = gym.make('findexit-v0')
env.reset()
print(env.action_space)

# posicion inicial (tengo que cambiar esto)
current_ob = (5, 0)
previous_ob = (5, 0)

for i in range(100000):
    # obtenemos la posición del valor mayor de las posibles acciones de la q table (posiblemente añadamos aleatoriedad con epsilon)
    action = np.argmax(q_table[current_ob])
    print("action = " + str(action) + ", values in q_table = " + str(q_table[current_ob]))

    # ejecutamos el step utilizando este valor como acción
    reward, current_ob = env.step(action)
    print("ob = " + str(current_ob))
    if reward == 1:
        print("Exit reached in step " + str(i))
        print(q_table)
        break

    # actualizamos valor de la posición en la q_table
    #next_q = np.max(q_table[ob])
    #print("next_q = " + str(next_q))

    #print("TEST: " + str(q_table[ob][int(action)]))

    q_table[previous_ob][int(action)] = q_table[current_ob][int(action)] * (1 - LEARNING_RATE) + LEARNING_RATE * (reward + DISCOUNT_RATE * np.max(q_table[current_ob][int(action)]))
    previous_ob = current_ob

'''
    
    y si consideramos tener las posiciones iniciales como aleatoria? asi tendria mas sentido los distintos valores q
    
    TODO: añadir episodios para ir refinando la Q table cada episodio
    
'''

