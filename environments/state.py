import win32gui
import win32ui
from ctypes import windll
from PIL import Image, ImageGrab
import numpy as np

from .memory_reader import MemoryReader

class State:
    def __init__(self, handler, base_address, image_size):
        """
        :param handler: 피카츄배구의 윈도우 핸들러 번호
        :param config.image_size: 미리 이미지의 사이즈를 정할 수 있음
        """
        
        self.handler = handler
        left, top, right, bottom = win32gui.GetWindowRect(self.handler)
        self.bbox = (left+40, top+130, right+150, bottom+110)
        # self.bbox = (left, top+, right, bottom)
        self.image_size = image_size
        self.memory_reader = MemoryReader(self.handler, base_address)
        
    def get_state(self, gray=True):
        """Get image array of state
        :param gray: if true, get grayscale image (default True)
        """
        img = ImageGrab.grab(self.bbox)
        img = img.resize(self.image_size, Image.ANTIALIAS)
        if gray:
            img = img.convert("L")
        img_array = np.array(img, dtype=np.uint8)
        return img_array
    
    def get_score(self):
        com_score, my_score = self.memory_reader.get_score()
        return com_score, my_score
    
    def get_image(self, resize=True, gray=False):
        img = ImageGrab.grab(self.bbox)
        if resize:
            img = img.resize(self.image_size, Image.ANTIALIAS)
        if gray:
            img = img.convert("L")
        return img
    
    def is_over(self):
        return self.memory_reader.is_over()
