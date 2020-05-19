import gym
from gym import error, spaces, utils
from gym.utils import seeding
import numpy as np
import element


class findexitEnv(gym.Env):

    metadata = {'render.modes': ['human']}
    explorer = element.Element(0, 3)
    map_exit = element.Element(4, 6)

    game_map = np.array([
        [0, 0, 0, 1, 7, 2, 2],
        [0, 0, 0, 2, 0, 0, 0],
        [0, 0, 0, 3, 0, 0, 0],
        [0, 0, 0, 4, 0, 0, 0],
        [0, 0, 0, 5, 3, 23, 99],
        [0, 0, 0, 6, 0, 0, 0],
        [0, 0, 0, 7, 0, 0, 0]
    ])


    def __init__(self):
        self.action_space = 4

    def step(self, action):
        print("value at coordinates = " + str(self.game_map[self.explorer.x, self.explorer.y]))
        if action == 0:
            if self.explorer.x - 1 >= 0 and self.game_map[self.explorer.x - 1, self.explorer.y] > 0:
                print("MOVE UP")
                self.explorer.x -= 1
            else:
                print("WALL UP")
        elif action == 1:
            if self.explorer.y + 1 < len(self.game_map[0]):
                if self.game_map[self.explorer.x, self.explorer.y + 1] > 0:
                    print("MOVE RIGHT")
                    self.explorer.y += 1
            else:
                print("WALL RIGHT")
        elif action == 2:
            if self.explorer.x + 1 < len(self.game_map):
                if self.game_map[self.explorer.x + 1, self.explorer.y] > 0:
                    print("MOVE DOWN")
                    self.explorer.x += 1
            else:
                print("WALL DOWN")
        elif action == 3:
            if self.explorer.y - 1 <= len(self.game_map) and self.game_map[self.explorer.x, self.explorer.y - 1] > 0:
                print("MOVE LEFT")
                self.explorer.y -= 1
            else:
                print("WALL LEFT")

        reward = self.getreward()
        return reward


    def reset(self):
        print("reset")
        pass

    def render(self, mode='human', close=False):
        pass

    def getreward(self):
        if self.explorer.x == self.map_exit.x and self.explorer.y == self.map_exit.y:
            return 1
        else:
            return 0

