import gym
from gym import error, spaces, utils
from gym.utils import seeding
import numpy as np
import element
from PIL import Image
import cv2


class findexitEnv(gym.Env):

    explorer = element.Element(0, 0)
    map_exit = element.Element(9, 9)

    game_map = np.array([
        [1, 1, 1, 1, 1, 1, 1, 1, 0, 0],
        [0, 0, 0, 1, 0, 0, 1, 0, 0, 1],
        [0, 1, 1, 1, 0, 0, 1, 0, 1, 1],
        [0, 1, 0, 0, 0, 0, 0, 0, 1, 0],
        [0, 1, 1, 1, 1, 1, 1, 1, 1, 0],
        [0, 1, 0, 1, 0, 0, 0, 1, 0, 0],
        [0, 1, 0, 0, 0, 0, 1, 1, 0, 0],
        [1, 1, 0, 1, 0, 1, 1, 0, 1, 1],
        [0, 1, 0, 1, 0, 1, 0, 1, 1, 1],
        [0, 1, 0, 1, 1, 1, 1, 1, 0, 1]
    ])

    def __init__(self):
        self.action_space = 4
        '''
        TODO: añadir inicializacion de posicion inicial del explorador aleatoria en contstructor del entorno
        '''

    def step(self, action):
        """

        ejecuta la acción escogida

        reward retorna 1 si ha llegado al final, o 0 si aún no ha llegado al final

        """
        #print("explorer position = " + str(self.explorer.get_position()))
        #print("value at coordinates = " + str(self.game_map[self.explorer.x, self.explorer.y]))
        if action == 0:
            if self.explorer.x - 1 >= 0 and self.game_map[self.explorer.x - 1, self.explorer.y] > 0:
                #print("MOVE UP")
                self.explorer.move(-1, 0)
            else:
                #print("WALL UP")
                pass
        elif action == 1:
            if self.explorer.y + 1 < len(self.game_map[0]):
                if self.game_map[self.explorer.x, self.explorer.y + 1] > 0:
                    #print("MOVE RIGHT")
                    self.explorer.move(0, 1)
            else:
                #print("WALL RIGHT")
                pass
        elif action == 2:
            if self.explorer.x + 1 < len(self.game_map):
                if self.game_map[self.explorer.x + 1, self.explorer.y] > 0:
                    #print("MOVE DOWN")
                    self.explorer.move(1, 0)
            else:
                #print("WALL DOWN")
                pass
        elif action == 3:
            if self.explorer.y - 1 >= 0 and self.game_map[self.explorer.x, self.explorer.y - 1] > 0:
                #print("MOVE LEFT")
                self.explorer.move(0, -1)
            else:
                #print("WALL LEFT")
                pass

        # la observación del entorno es la distancia entre el explorador y la salida, (x, y)
        ob = self.get_observation(self.map_exit)

        # la recompensa es 1 si ha llegado a la salida, 0 si no es así
        reward = self.get_reward()
        return reward, ob


    def reset(self):
        self.explorer.set_position(0, 0)
        self.map_exit.set_position(9, 9)
        return self.get_observation(self.map_exit)

    def render(self, mode='human', close=False):
        map_image = np.zeros((10, 10, 3), dtype=np.uint8) #sera tamaño
        for line in self.game_map:
            for pixel in range(len(line)):
                #map_image[line][pixel] = 0, 255, 0
                print(map_image[0])

        img = Image.fromarray(map_image, "RGB")
        img = img.resize((400, 400), resample=Image.NEAREST)
        cv2.imshow("", np.array(img))
        cv2.waitKey(20)



    def get_reward(self):
        if self.explorer.x == self.map_exit.x and self.explorer.y == self.map_exit.y:
            return 1
        else:
            return 0

    def get_observation(self, other):
        return self.explorer.distance(other)
