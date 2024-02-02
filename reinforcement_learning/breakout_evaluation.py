from stable_baselines3 import A2C
from stable_baselines3.common.env_util import make_atari_env
from stable_baselines3.common.evaluation import evaluate_policy
from stable_baselines3.common.vec_env import VecFrameStack

from reinforcement_learning import a2c_path

env = make_atari_env('Breakout-v4', n_envs=1, seed=0, env_kwargs={'render_mode':'human'})
env = VecFrameStack(env, n_stack=6)

#A2C - 100k (7.0, 2.792848008753788)
model_100k = A2C.load(a2c_path + '-100k', env)
#A2C - 300k (10.8, 3.1240998703626617)
model_300k = A2C.load(a2c_path + '-300k', env)
#A2C - 600k (14.5, 3.7483329627982624)
model_600k = A2C.load(a2c_path + '-600k', env)
#A2C - 900k (17.3, 8.1)
model_900k = A2C.load(a2c_path + '-900k', env)

result = evaluate_policy(model_900k, env, n_eval_episodes=10, render=True)

print(result)

env.close()