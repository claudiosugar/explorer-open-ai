import numpy as np

game_map = np.array([
    [0, 0, 0, 1, 0, 0, 0],
    [0, 0, 5, 1, 0, 0, 0],
    [0, 3, 0, 1, 0, 0, 0],
    [0, 0, 0, 1, 0, 0, 0],
    [0, 0, 0, 1, 0, 0, 0],
    [0, 0, 0, 1, 0, 0, 0]
])

position = 1, 2

print(game_map[position])