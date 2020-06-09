from gym.envs.registration import register

register(
    id='explorer-v0',
    entry_point='gym_explorer.envs:explorer0Env',
)

register(
    id='explorer-random-exit-v0',
    entry_point='gym_explorer.envs:explorer_random_exit0Env',
)

