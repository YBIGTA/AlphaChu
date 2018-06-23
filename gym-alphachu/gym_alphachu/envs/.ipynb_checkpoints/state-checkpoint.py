import win32gui
import win32ui
from ctypes import windll
from PIL import Image, ImageGrab
import numpy as np

class State:
    def __init__(self, handler, config):
        """
        :param handler: 피카츄배구의 윈도우 핸들러 번호
        :param config.image_size: 미리 이미지의 사이즈를 정할 수 있음
        """
        self.handler = handler
        left, top, right, bottom = win32gui.GetWindowRect(self.handler)
        self.bbox = (left+10, top+50, right-5, bottom-20)
        self.image_size = config.image_size
        
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
    
    def get_image(self, resize=True, gray=False):
        img = ImageGrab.grab(self.bbox)
        if resize:
            img = img.resize(self.image_size, Image.ANTIALIAS)
        if gray:
            img = img.convert("L")
        return img
    
    def is_over(self):
        raise NotImplementedError