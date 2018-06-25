def open_game():
    process = subprocess.Popen("pika.exe")

def get_window():
    window_list = list()
    win32gui.EnumWindows(callback, window_list)
    for window in window_list:
        if '뫮먰귃' in window:
            print("Found window : {}".format(window))
            address = eval(window.split(":")[0])
            window_name = eval(window.split(":")[1])
            handler = win32gui.FindWindowEx(0, 0, None, window_name)
    return address, window_name, handler

def callback(handler, strings):
    if win32gui.IsWindowVisible(handler):
        window_title = win32gui.GetWindowText(handler)
        left, top, right, bottom = win32gui.GetWindowRect(handler)
        if window_title and right-left and bottom-top:
            string.append("0x{:08x}: '{}'".format(handler, window_title))
    return True