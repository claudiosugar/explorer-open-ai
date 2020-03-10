import gym
from gym import error, spaces, utils
from gym.utils import seeding
import numpy as np
import element


class findexitEnv(gym.Env):

    metadata = {'render.modes': ['human']}
    explorer = element.Element(0, 3)
    map_exit = element.Element(3, 5)

    game_map = np.array([
        [0, 0, 0, 1, 7, 0, 0],
        [0, 0, 0, 2, 0, 0, 0],
        [0, 0, 0, 3, 0, 0, 0],
        [0, 0, 0, 4, 0, 0, 0],
        [0, 0, 0, 5, 0, 0, 0],
        [0, 0, 0, 6, 0, 0, 0]
    ])



    def __init__(self):
        print(self.explorer.position)
        print(self.map_exit.position)
        print(self.game_map)

    def step(self, action):
        if action == 2:
            print(self.game_map[self.explorer.x - 1, self.explorer.y])
            if self.game_map[self.explorer.x - 1, self.explorer.y] > 0:
                print("DOWN")
            else:
                print("WALL DOWN")

        '''
        if action == 0:
            if self.explorer.x > 0 and self.game_map[self.explorer.y, self.explorer.x - 1] == 1:
                self.explorer.x -= 1
                print("UP")
            else:
                print("WALL UP")
        if action == 1:
            if self.explorer.y < 7 and self.game_map[self.explorer.y + 1, self.explorer.x] == 1:
                self.explorer.y += 1
                print("RIGHT")
            else:
                print("WALL RIGHT")
        if action == 2:
            if self.explorer.x < 6 and self.game_map[self.explorer.y, self.explorer.x + 1] == 1:
                self.explorer.x += 1
                print("DOWN")
            else:
                print("WALL DOWN")
        if action == 3:
            if self.explorer.x > 0 and self.game_map[self.explorer.y, self.explorer.x - 1] == 1:
                self.explorer.y -= 1
                print("LEFT")
            else:
                print("WALL LEFT")
        '''

    def reset(self):
        print("reset")
        pass

    def render(self, mode='human', close=False):
        pass



