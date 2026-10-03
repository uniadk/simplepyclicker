import time
import win32api, win32con
import keyboard
import ctypes

def setTitle(title): # Sets the title of the console window with the argument
    ctypes.windll.kernel32.SetConsoleTitleW(f"{title}")

def click(x, y): # Click Function
    win32api.mouse_event(win32con.MOUSEEVENTF_LEFTDOWN, x, y, 0, 0)
    win32api.mouse_event(win32con.MOUSEEVENTF_LEFTUP, x, y, 0, 0)

def getMouse(): # Fetches the current mouse position
    pos = win32api.GetCursorPos()
    return pos

def isPressedQ(): # Checking whether q is held down
    if keyboard.is_pressed('q'):
        return True
    else:
        return False

def isPressedB(): #Checking whether B is held down
    if keyboard.is_pressed('b'):
        return True
    else:
        return False


def clicker(): # Clicker function
    while True:
        time.sleep(0.1)
        if isPressedQ():
            setTitle("Clicker is Active")
            while True:
                pos = getMouse()
                positionx = pos[0]
                positiony = pos[1]
                click(positionx, positiony)
                time.sleep(0.1) # 10cps = 0.1, 20cps = 0.05
                if isPressedB():
                    setTitle("Clicker is Inactive")
                    break
                else: continue

setTitle("Clicker is Inactive")
print("Clicker")
print("Hold to enable/disable")
print("Q = Enable")
print("B = Disable")
print("Read the title for the current toggle")
clicker()
