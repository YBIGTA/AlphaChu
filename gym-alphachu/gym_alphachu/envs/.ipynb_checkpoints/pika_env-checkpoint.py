import numpy as np
import os
import gym
from gym import error, spaces
from gym import utils
from gym.utils import seeding
from gym.envs.classic_control import rendering

import subprocess
import os
import win32gui

from .helper import open_game, get_window
from .state import State
from .action import Action

class PikaEnv(gym.Env):
    meta_data = {'render.modes': ['human']}
    
    def __init__(self, config):
        # define hparams
        self.frame_skip = (2,5)
        self.repeat_action_prob = 0.
        self.base_address = config.base_address
        
        # 게임 실행
        open_game()
        
        # 윈도우 이름과 handler 받아오기
        _, self.window_name, self.handler = get_window()
        
        # state, action, memory_reader 정의
        self.state = State(self.handler, config)
        self.com_score = 0
        self.my_score = 0
        self.action = Action(config)
        
        # rendering
        self.viewer = None
        
    def seed(self, seed=None):
        self.np_random, seed1 = seeding.np_random(seed)
        # Derive a random seed. This gets passed as a uint, but gets
        # checked as an int elsewhere, so we need to keep it below
        # 2**31.
        seed2 = seeding.hash_seed(seed1 + 1) % 2**31
        # Empirically, we need to seed before loading the ROM.
        self.ale.setInt(b'random_seed', seed2)
        self.ale.loadROM(self.game_path)
        return [seed1, seed2]
    
    def step(self, key_num):
        """
        :param key_num: 입력할 액션 값
        
        Return:
            observation : 이전 행동에 의한 state값
            reward : 이전 행동에 의한 보상 값
            done : 게임(or episode)가 종료되었는 지의 여부
            info : 부가적인 정보
        """
        reward = 0.0
        num_steps = np.random.randint(self.frameskip[0], self.frameskip[1])

        # do action and get reward
        for _ in range(num_steps):
            self.action.send_key(key_num)
            reward += self.get_reward()

        observation = self.state.get_state()
        return observation, reward, False, {"com_score": self.com_score, 
                                                           "my_score": self.my_score}
    
    def render(self, mode='human'):
        img = self._get_image()
        if mode == 'rgb_array':
            return img
        elif mode == 'human':
            if self.viewer is None:
                self.viewer = rendering.SimpleImageViewer()
            self.viewer.imshow(img)
            return self.viewer.isopen
        
    def close(self):
        if self.viewer is not None:
            self.viewer.close()
            self.viewer = None
            
    def get_reward(self):
        com_score, my_score = self.state.get_score()
        # computer wins
        if com_score-self.com_score == 1:
            reward = -1
            self.com_score = com_score
        # agent wins
        elif my_score-self.my_score == 1:
            reward = 1
            self.my_score = my_score
        # not finished
        else:
            reward = 0
        return reward
