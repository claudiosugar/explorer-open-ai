from gym.envs.registration import register

register(
    id='findexit-v0',
    entry_point='gym_findexit.envs:findexitEnv',
)