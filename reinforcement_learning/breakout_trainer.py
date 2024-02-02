from stable_baselines3 import A2C
from stable_baselines3.common.env_util import make_atari_env
from stable_baselines3.common.vec_env import VecFrameStack

from reinforcement_learning import a2c_path, log_path

"""
    Specify the environment and its wrapper (VecFrameStack)
    Run n_envs simultaneous environments for performance gains
"""
env = make_atari_env('Breakout-v4', n_envs=6, seed=0)
env = VecFrameStack(env, n_stack=6)

"""Load model & save the logs under ./training/logs/"""
model = A2C('CnnPolicy', env, verbose=1, tensorboard_log=log_path)

"""Train the model"""
model.learn(total_timesteps=900000)

"""Save the model under a2c_path"""
model.save(a2c_path)
