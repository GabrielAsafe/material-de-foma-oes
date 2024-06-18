import pyautogui
import ctypes
import tkinter as tk
from tkinter.ttk import * 


def get_window_rect(hwnd):
    rect = ctypes.wintypes.RECT()
    ctypes.windll.user32.GetWindowRect(hwnd, ctypes.byref(rect))
    return rect.left, rect.top, rect.right - rect.left, rect.bottom - rect.top

def move_window(window):
    
     # Get the current mouse position
    mouse_x, mouse_y = pyautogui.position()

    # Move the window to the mouse position
    window.geometry(f"300x200+{mouse_x}+{mouse_y}")
    window.after(10, move_window)  # Update every 10 milliseconds

def createWindow():
    window = tk.Tk()
    window.title("janela")
    window.mainloop()

def main():
    createWindow()


if __name__ == "__main__":
    


    while(True):

     

        move_window(janela)
