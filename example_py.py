from environments.pika_env import PikaEnv
from environments.helper import open_game, get_window
from tensorflow.python import pywrap_tensorflow
import time

class Config:
    def __init__(self):
        # environment
        self.base_address = 0x00000F40
        self.image_size = [80, 80]
        self.interval_time = 0.2
        
        # model
        self.hidden_layer_size = 200
        self.learning_rate = 0.0005
        self.batch_size_episodes = 10
        self.load_checkpoint = "store_true"
        self.discount_factor = 0.99
        self.render = "store_true"


config = Config()
env = PikaEnv(config)
env.reset_game()
time.sleep(5)
for _ in range(5):
    print("Dfgdfg")
    _,_,_,_ = env.step(1)
