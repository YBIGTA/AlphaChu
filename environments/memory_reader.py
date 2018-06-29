import win32api
import win32process
import ctypes

class MemoryReader:
    PROCESS_ALL_ACCESS = 0xFFF
    read_process_memory = ctypes.windll.kernel32.ReadProcessMemory
    open_process = ctypes.windll.kernel32.OpenProcess
    close_handle = ctypes.windll.kernel32.CloseHandle
    
    handler = None
    pid = None
    process_handle = None
    
    buffer = ctypes.c_char_p(b"0")
    buffer_size = len(buffer.value)
    bytes_read = ctypes.c_ulong(0)
    
    score_address = 0x02360EAC
    
    def __init__(self, handler, base_address):
        self.handler = handler
        self.pid = self.get_pid()
        self.base_address = base_address
        self.process_handle = self.open_process(self.PROCESS_ALL_ACCESS, False, self.pid)
        
    def get_pid(self):
        _, pid = win32process.GetWindowThreadProcessId(self.handler)
        return pid
    
    def get_score(self):
        is_start = False
        
        # read com score
        self.read_process_memory(self.process_handle, self.score_address, self.buffer, self.buffer_size, ctypes.byref(self.bytes_read))
        com_score = int.from_bytes(self.buffer.value, byteorder='little')
        
        # read my score
        self.read_process_memory(self.process_handle, self.score_address+4, self.buffer, self.buffer_size, ctypes.byref(self.bytes_read))
        my_score = int.from_bytes(self.buffer.value, byteorder='little')
                
        return com_score, my_score
    
    def is_over(self):
        # read flag
        # 진행상태FLAG 0:(최초게임시작)공떨어지기전 1: 공떨어지기전 2:게임중 3:공이 땅에 닿임 4: 게임 종료 A: 메뉴
        self.read_process_memory(self.process_handle, self.score_address+4+8, self.buffer, self.buffer_size, ctypes.byref(self.bytes_read))
        flag = int.from_bytes(self.buffer.value, byteorder='little')
        return flag