import gym
import numpy as np
import element
from PIL import Image
import cv2


class explorer_random_exit0Env(gym.Env):

    game_map = np.array([
        [1, 1, 1, 1, 1, 1, 1, 1, 0, 0, 1, 1, 0, 0, 1, 1, 0, 1, 1, 1],
        [0, 1, 0, 1, 0, 0, 1, 0, 0, 1, 1, 0, 0, 1, 1, 1, 0, 1, 0, 1],
        [0, 1, 1, 1, 0, 0, 1, 0, 1, 1, 1, 1, 1, 1, 1, 1, 0, 1, 0, 1],
        [0, 1, 0, 0, 0, 0, 0, 0, 1, 0, 1, 0, 0, 1, 1, 1, 0, 1, 0, 1],
        [0, 1, 1, 1, 1, 1, 1, 1, 1, 0, 1, 0, 0, 1, 0, 0, 0, 1, 0, 1],
        [0, 1, 0, 1, 0, 0, 0, 1, 0, 0, 1, 1, 0, 1, 1, 1, 1, 1, 0, 1],
        [0, 1, 0, 0, 0, 0, 1, 1, 0, 0, 1, 1, 1, 1, 0, 0, 0, 0, 0, 1],
        [1, 1, 0, 1, 0, 1, 1, 0, 1, 1, 0, 0, 1, 1, 0, 1, 1, 1, 0, 1],
        [0, 1, 0, 1, 0, 1, 0, 1, 1, 1, 1, 0, 1, 1, 1, 1, 1, 1, 0, 1],
        [0, 1, 0, 1, 1, 1, 1, 1, 0, 1, 1, 0, 0, 1, 0, 1, 1, 1, 0, 1],
        [1, 1, 1, 1, 1, 1, 1, 1, 0, 0, 1, 1, 0, 1, 0, 1, 1, 1, 0, 1],
        [0, 1, 0, 1, 0, 0, 1, 0, 0, 1, 1, 1, 0, 1, 0, 1, 1, 1, 0, 1],
        [0, 1, 1, 1, 0, 0, 1, 0, 1, 1, 1, 1, 0, 1, 0, 1, 1, 1, 0, 1],
        [0, 1, 0, 0, 0, 0, 0, 0, 1, 0, 1, 1, 0, 1, 1, 0, 1, 1, 0, 1],
        [0, 1, 1, 1, 1, 1, 1, 1, 1, 0, 1, 1, 0, 1, 1, 1, 0, 1, 0, 1],
        [0, 1, 0, 1, 0, 0, 0, 1, 0, 0, 1, 1, 1, 1, 1, 1, 1, 1, 0, 1],
        [0, 1, 0, 0, 0, 0, 1, 1, 0, 0, 1, 1, 1, 1, 1, 1, 1, 1, 0, 1],
        [1, 1, 0, 1, 0, 1, 1, 0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0, 1],
        [0, 1, 0, 1, 0, 1, 0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0, 1, 0, 1],
        [0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0, 1, 1, 1]
    ])
    '''
    game_map = np.array([
        [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
        [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
        [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
        [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
        [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
        [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
        [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
        [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
        [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
        [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
        [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
        [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
        [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
        [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
        [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
        [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
        [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
        [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
        [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
        [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1]
    ])
    '''

    # posición aleatoria válida del explorador
    explorer = element.Element(np.random.randint(0, len(game_map)), np.random.randint(0, len(game_map)))
    while game_map[explorer.initial_x][explorer.initial_y] == 0:
        explorer = element.Element(np.random.randint(0, len(game_map)), np.random.randint(0, len(game_map)))

    # posicion aleatoria valida de la salida
    map_exit = element.Element(np.random.randint(0, len(game_map)), np.random.randint(0, len(game_map)))
    while game_map[map_exit.initial_x][map_exit.initial_y] == 0:
        map_exit = element.Element(np.random.randint(0, len(game_map)), np.random.randint(0, len(game_map)))


    def __init__(self):
        self.action_space = 4
        self.observation_space = len(self.game_map)


    def step(self, action):
        """

        ejecuta la acción escogida

        reward retorna 1 si ha llegado al final, o -1 si aún no ha llegado al final

        """
        #print("explorer position = " + str(self.explorer.get_position()))
        #print("value at coordinates = " + str(self.game_map[self.explorer.x, self.explorer.y]))
        if action == 0:
            if self.explorer.x - 1 >= 0 and self.game_map[self.explorer.x - 1, self.explorer.y] > 0:
                self.explorer.move(-1, 0)
            else:
                pass
        elif action == 1:
            if self.explorer.y + 1 < len(self.game_map[0]):
                if self.game_map[self.explorer.x, self.explorer.y + 1] > 0:
                    self.explorer.move(0, 1)
            else:
                pass
        elif action == 2:
            if self.explorer.x + 1 < len(self.game_map):
                if self.game_map[self.explorer.x + 1, self.explorer.y] > 0:
                    self.explorer.move(1, 0)
            else:
                pass
        elif action == 3:
            if self.explorer.y - 1 >= 0 and self.game_map[self.explorer.x, self.explorer.y - 1] > 0:
                self.explorer.move(0, -1)
            else:
                pass

        # la observación del entorno es la distancia entre el explorador y la salida, (x, y)
        ob = self.get_observation(self.map_exit)

        # la recompensa es 1 si ha llegado a la salida, -1 si no es así
        reward = self.get_reward()
        return reward, ob


    # reset coloca al explorador y la salida en una nueva posición inicial
    def reset(self):
        self.explorer.set_position(np.random.randint(0, len(self.game_map)), np.random.randint(0, len(self.game_map)))
        while self.game_map[self.explorer.initial_x][self.explorer.y] == 0:
            self.explorer.set_position(np.random.randint(0, len(self.game_map)), np.random.randint(0, len(self.game_map)))

        self.map_exit.set_position(np.random.randint(0, len(self.game_map)), np.random.randint(0, len(self.game_map)))
        while self.game_map[self.map_exit.initial_x][self.map_exit.y] == 0:
            self.map_exit.set_position(np.random.randint(0, len(self.game_map)),
                                       np.random.randint(0, len(self.game_map)))


        return self.get_observation(self.map_exit)




    # TODO: inicializar map_image en constructor para no realizar este proceso cada render?
    def render(self, mode='human', close=False):
        map_image = np.zeros((self.observation_space, self.observation_space, 3), dtype=np.uint8) #sera tamaño
        line_index = 0
        for line in self.game_map:
            for pixel in range(len(line)):
                if self.game_map[line_index][pixel] == 1:
                    map_image[line_index][pixel] = 250, 250, 250
            line_index += 1

        map_image[self.explorer.x][self.explorer.y] = 255, 100, 100
        map_image[self.map_exit.x][self.map_exit.y] = 0, 0, 255
        img = Image.fromarray(map_image, "RGB")
        img = img.resize((400, 400), resample=Image.NEAREST)
        cv2.imshow("", np.array(img))
        cv2.waitKey(40)

    def get_reward(self):
        if self.explorer.distance(self.map_exit) == (0, 0):
            return 1
        else:
            return -1

    def get_observation(self, other):
        return self.explorer.distance(other)

