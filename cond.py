import time
import keyboard
import pyautogui
import win32api
import ctypes
from pynput import keyboard

def test_win32api():
    start_time = time.time()
    state = win32api.GetKeyState(0x14)
    end_time = time.time()
    print("win32api time: ", end_time - start_time)
    return state




def test_ctypes():
    start_time = time.time()
    state = ctypes.windll.user32.GetKeyState(0x14)
    end_time = time.time()
    print("ctypes time: ", end_time - start_time)
    return state


print("Win32api Caps Lock state: ", test_win32api())
print("ctypes Caps Lock state: ", test_ctypes())
