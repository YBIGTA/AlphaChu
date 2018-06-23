from gym.envs.registration import register

register(
    id='alphachu-v0',
    entry_point='gym_alphachu.env:VolleyBall'
)
