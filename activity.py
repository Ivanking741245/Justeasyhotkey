import keyboard
import time
import sys
import os
import pyautogui
import pyperclip
class activity():
    def __init__(self):
        pass
    def check_id(self, id):
        global act
        act = activity()
        def check_command(command, line , ms=None, debg=None):
            commandlist = ["cmd", "mouse", "print"]
            if commandlist.index(command) == 0:
                act.activity_cmd(line=line)
            elif commandlist.index(command) == 1:
                act.activity_mouse(command=line, info=ms, debg=debg)
            elif commandlist.index(command) == 2:
                act.activity_print(line=line)
        with open("activity.txt", "r", encoding="utf-8") as f:
            a = f.readlines()[id].strip().split("+")
            print(a)
            if "CMCM" in a[0]:
                try:
                    check_command(command=a[1], line=a[2], ms=a[3], debg=a)
                except:
                    check_command(command=a[1], line=a[2], ms=None, debg=a)
            else:
                act.activity_keyboard(line=id)
    def activity_keyboard(self, line):
        keyboard.release("ctrl")
        keyboard.release("alt")
        keyboard.release("shift")
        keyboard.release("win")
        with open("activity.txt", "r", encoding="utf-8") as f:
            allkey = f.readlines()[line].strip().split("+")
        print(f"call:{allkey}")
        for i in range(len(allkey)):
            keyboard.press(allkey[i])
            time.sleep(0.05)
        for i in range(len(allkey)):
            keyboard.release(allkey[i])
            time.sleep(0.05)
        time.sleep(0)
    def activity_cmd(self, line):
        os.system(line)
    def activity_mouse(self, command, info, debg):
        mouse_command = ["cl", "cl_sp","mv"]
        if mouse_command.index(command) == 0:
            for i in range(int(info)):
                pyautogui.click()
        if mouse_command.index(command) == 1:
            start = time.time()
            while True:
                pyautogui.click()
                stop = time.time()
                if stop-start >= int(info):
                    break
        elif mouse_command.index(command) == 2:
            #print(f"debg:{debg}")
            x , y = str(info).strip().split(",")
            x, y = int(x), int(y)
            pyautogui.moveTo(x , y)
    def activity_print(self, line):
        pyperclip.copy(line)
        time.sleep(0.1)
        keyboard.press("ctrl")
        keyboard.press("v")
        keyboard.release("ctrl")
        keyboard.release("v")