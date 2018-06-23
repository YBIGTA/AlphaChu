import win32con
import win32api
import time
import win32com.client as client

class Action:
    def __init__(self, config):
        self.shell = client.Dispatch('WScript.Shell')
        self.window_name = config.window_name
        self.interval_time = config.interval_time
        self.key_map = {0: 0x0D, # enter
                        1: 0x26, # up arrow
                        2: 0x28, # down arrow
                        3: 0x25, # left arrow
                        4: 0x27, # right arrow
                       }

    def send_key(self, key_num):
        """
        :param key_num: 입력 키의 조합
            0: SPIKE
            1: UP
            2: DOWN
            3: LEFT
            4: RIGHT
            5: LEFT & SPIKE
            6: UP & SPIKE
            7: RIGHT & SPIKE
            8: DOWN & SPIKE
            9: UP & LEFT & SPIKE
            10: UP & RIGHT & SPIKE
        """
        # Activate pika window
        self.shell.AppActivate(self.window_name)

        # 하나의 키일 때
        if key_num < 5:
            win32api.keybd_event(self.key_map[key_num], 0, 0, 0)
            return

        # key_num 5 : Left & Spike
        elif key_num == 5:
            win32api.keybd_event(self.key_map[3], 0, 0, 0)
            time.sleep(self.interval_time)
            win32api.keybd_event(self.key_map[0], 0, 0, 0)
            time.sleep(self.interval_time)
            win32api.keybd_event(self.key_map[3], 0, win32con.KEYEVENTF_KEYUP, 0)
            time.sleep(self.interval_time)
            win32api.keybd_event(self.key_map[0], 0, win32con.KEYEVENTF_KEYUP, 0)
            time.sleep(self.interval_time)
            return

        # key_num 7 : Right & Spike
        elif key_num == 7:
            win32api.keybd_event(self.key_map[4], 0, 0, 0)
            time.sleep(self.interval_time)
            win32api.keybd_event(self.key_map[0], 0, 0, 0)
            time.sleep(self.interval_time)
            win32api.keybd_event(self.key_map[4], 0, win32con.KEYEVENTF_KEYUP, 0)
            time.sleep(self.interval_time)
            win32api.keybd_event(self.key_map[0], 0, win32con.KEYEVENTF_KEYUP, 0)
            time.sleep(self.interval_time)
            return

        # key_num 8 : Down & Spike
        elif key_num == 8:
            win32api.keybd_event(self.key_map[2], 0, 0, 0)
            time.sleep(self.interval_time)
            win32api.keybd_event(self.key_map[0], 0, 0, 0)
            time.sleep(self.interval_time)
            win32api.keybd_event(self.key_map[2], 0, win32con.KEYEVENTF_KEYUP, 0)
            time.sleep(self.interval_time)
            win32api.keybd_event(self.key_map[0], 0, win32con.KEYEVENTF_KEYUP, 0)
            time.sleep(self.interval_time)
            return

        # key_num 9 : Up & Left & Spike
        elif key_num == 9:
            win32api.keybd_event(self.key_map[1], 0, 0, 0)
            time.sleep(self.interval_time)
            win32api.keybd_event(self.key_map[3], 0, 0, 0)
            time.sleep(self.interval_time)
            win32api.keybd_event(self.key_map[0], 0, 0, 0)
            time.sleep(self.interval_time)
            win32api.keybd_event(self.key_map[1], 0, win32con.KEYEVENTF_KEYUP, 0)
            time.sleep(self.interval_time)
            win32api.keybd_event(self.key_map[3], 0, win32con.KEYEVENTF_KEYUP, 0)
            time.sleep(self.interval_time)
            win32api.keybd_event(self.key_map[0], 0, win32con.KEYEVENTF_KEYUP, 0)
            time.sleep(self.interval_time)
            return

        # key_num 10 : Up & Right & Spike
        elif key_num == 9:
            win32api.keybd_event(self.key_map[1], 0, 0, 0)
            time.sleep(self.interval_time)
            win32api.keybd_event(self.key_map[4], 0, 0, 0)
            time.sleep(self.interval_time)
            win32api.keybd_event(self.key_map[0], 0, 0, 0)
            time.sleep(self.interval_time)
            win32api.keybd_event(self.key_map[1], 0, win32con.KEYEVENTF_KEYUP, 0)
            time.sleep(self.interval_time)
            win32api.keybd_event(self.key_map[4], 0, win32con.KEYEVENTF_KEYUP, 0)
            time.sleep(self.interval_time)
            win32api.keybd_event(self.key_map[0], 0, win32con.KEYEVENTF_KEYUP, 0)
            time.sleep(self.interval_time)
            return

    def start_game(self):
        # Activate pika window
        self.shell.AppActivate(self.window_name)
        for _ in range(3):
            win32api.keybd_event(self.key_map[0], 0, 0, 0) # enter down
            time.sleep(0.1)
            win32api.keybd_event(self.key_map[0], 0, win32con.KEYEVENTF_KEYUP, 0) # enter down
            time.sleep(0.1)
        time.sleep(2)

    def reset_game(self):
        # Activate pika window
        self.shell.AppActivate(self.window_name)
        win32api.keybd_event(0x12, 0, 0, 0) # alt
        time.sleep(self.interval_time)
        win32api.keybd_event(0x47, 0, 0, 0) # g
        time.sleep(self.interval_time)
        win32api.keybd_event(0x52, 0, 0, 0) # r
        time.sleep(self.interval_time)
        win32api.keybd_event(0x12, 0, win32con.KEYEVENTF_KEYUP, 0) # alt
        time.sleep(self.interval_time)
        win32api.keybd_event(0x47, 0, win32con.KEYEVENTF_KEYUP, 0) # g
        time.sleep(self.interval_time)
        win32api.keybd_event(0x52, 0, win32con.KEYEVENTF_KEYUP, 0) # r
        time.sleep(self.interval_time)
        self.start_game()

    def set_speed(self):
        # alt + c + s + h
        self.shell.AppActivate(self.window_name)
        win32api.keybd_event(0x12, 0, 0, 0) # alt
        time.sleep(self.interval_time)
        win32api.keybd_event(0x43, 0, 0, 0) # c
        time.sleep(self.interval_time)
        win32api.keybd_event(0x53, 0, 0, 0) # s
        time.sleep(self.interval_time)
        win32api.keybd_event(0x48, 0, 0, 0) # h
        time.sleep(self.interval_time)
        win32api.keybd_event(0x12, 0, win32con.KEYEVENTF_KEYUP, 0) # alt
        time.sleep(self.interval_time)
        win32api.keybd_event(0x43, 0, win32con.KEYEVENTF_KEYUP, 0) # c
        time.sleep(self.interval_time)
        win32api.keybd_event(0x53, 0, win32con.KEYEVENTF_KEYUP, 0) # s
        time.sleep(self.interval_time)
        win32api.keybd_event(0x48, 0, win32con.KEYEVENTF_KEYUP, 0) # h
        time.sleep(self.interval_time)
