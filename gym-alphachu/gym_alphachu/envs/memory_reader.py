import win32api
import win32process

class MemoryReader:
    PROCESS_ALL_ACCESS = 0x1F0FFF
    
    def __init__(self, handler, base_address):
        self.handler = handler
        self.pid = self.get_pid()
        self.base_address = base_address
        self.read_process_memory = ctypes.windll.kernel32.ReadProcessMemory
        
    def get_pid(self):
        _, pid = win32process.GetWindowThreadProcessId(self.handler)
        return pid
    
    def get_score(self):
        buffer = ctypes.c_char_p(b"0")
        
        # read com score
        self.read_process_memory(process_handle, base_addr + 0x448f1d0, buffer, len(buffer.value), ctypes.byref(ctypes.c_ulong(0)))
        com_score = int.from_bytes(buffer.value, byteorder='little')
        
        # read my score
        self.read_process_memory(process_handle, base_addr + 0x448f1d4, buffer, len(buffer.value), ctypes.byref(ctypes.c_ulong(0)))
        my_score = int.from_bytes(buffer.value, byteorder='little')
        
        return com_score, my_score