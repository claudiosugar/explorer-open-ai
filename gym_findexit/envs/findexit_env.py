import gym
from gym import error, spaces, utils
from gym.utils import seeding
import numpy as np
import element


class findexitEnv(gym.Env):

    explorer = element.Element(0, 3)
    map_exit = element.Element(9, 4)

    game_map = np.array([
        [0, 0, 0, 1, 2, 3, 4, 0, 0, 0],
        [0, 0, 0, 5, 0, 0, 0, 0, 0, 0],
        [0, 8, 7, 6, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 9, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 10, 11, 12, 13, 0, 0, 0],
        [0, 0, 0, 14, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 15, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 15, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 15, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 15, 16, 0, 0, 0, 0, 0]
    ])

    def __init__(self):
        self.action_space = 4

    def step(self, action):
        """

        ejecuta la acción escogida

        reward retorna 1 si ha llegado al final, o 0 si aún no ha llegado al final

        """
        print("explorer position = " + str(self.explorer.position()))
        print("value at coordinates = " + str(self.game_map[self.explorer.x, self.explorer.y]))
        if action == 0:
            if self.explorer.x - 1 >= 0 and self.game_map[self.explorer.x - 1, self.explorer.y] > 0:
                print("MOVE UP")
                self.explorer.move(-1, 0)
            else:
                print("WALL UP")
                pass
        elif action == 1:
            if self.explorer.y + 1 < len(self.game_map[0]):
                if self.game_map[self.explorer.x, self.explorer.y + 1] > 0:
                    print("MOVE RIGHT")
                    self.explorer.move(0, 1)
            else:
                print("WALL RIGHT")
                pass
        elif action == 2:
            if self.explorer.x + 1 < len(self.game_map):
                if self.game_map[self.explorer.x + 1, self.explorer.y] > 0:
                    print("MOVE DOWN")
                    self.explorer.move(1, 0)
            else:
                print("WALL DOWN")
                pass
        elif action == 3:
            if self.explorer.y - 1 <= len(self.game_map) and self.game_map[self.explorer.x, self.explorer.y - 1] > 0:
                print("MOVE LEFT")
                self.explorer.move(0, -1)
            else:
                print("WALL LEFT")
                pass

        # la observación del entorno es la distancia entre el explorador y la salida, (x, y)
        ob = self.get_observation(self.map_exit)

        # la recompensa es 1 si ha llegado a la salida, 0 si no es así
        reward = self.get_reward()
        return reward, ob


    def reset(self):
        print("reset")
        pass

    def render(self, mode='human', close=False):
        pass

    def get_reward(self):
        if self.explorer.x == self.map_exit.x and self.explorer.y == self.map_exit.y:
            return 1
        else:
            return 0

    def get_observation(self, other):
        return self.explorer.distance(other)
