from pynput import keyboard
import time
from activity import activity
from functools import partial
from checkrule import pynput_keyboard_checkrule
import pyuac
def main():
    act = activity()
    def on_activate(key):
        time.sleep(0)
        act.check_id(id=key)
    def dohotkey():
        pynput_keyboard_checkrule()
        hotkeys = {}
        with open("hotkeylist.txt", "r", encoding="utf-8") as f:
            keys = [line.strip() for line in f.readlines() if line.strip()]
        print(keys)
        for key in keys:
            print(keys.index(key))
            hotkeys[key] = partial(on_activate, keys.index(key))
        with keyboard.GlobalHotKeys(hotkeys) as h:
            h.join()
    dohotkey()
    
def getuac():
    if not pyuac.isUserAdmin():
        print("get uac.")
        pyuac.runAsAdmin()
    else:        
        main()
getuac()