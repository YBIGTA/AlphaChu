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
        self.bbox = (left+5, top+50, right-5, bottom-10)
        # self.bbox = (left+40, top+130, right+150, bottom+110)
        # self.bbox = (left, top, right, bottom)
        self.image_size = image_size
        self.memory_reader = MemoryReader(self.handler, base_address)
        
    def img_filtering(self, img):
        ball_index = np.logical_and(img[:,:,2]==0, np.logical_and(img[:,:,1]==0, img[:,:,0]==127))
        picka_index = np.logical_and(img[:,:,2]==0, np.logical_and(img[:,:,1]==255, img[:,:,0]==255))
        img_filterd = img
        img_filterd[np.logical_not(np.logical_or(ball_index, picka_index))] = 0
        img_filterd[np.logical_or(ball_index, picka_index)]=255
        return img_filterd
    
    def get_state(self, gray=True):
        """Get image array of state
        :param gray: if true, get grayscale image (default True)
        """
        img = ImageGrab.grab(self.bbox)
        img = self.img_filtering(np.array(img))
        img = Image.fromarray(img)
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
