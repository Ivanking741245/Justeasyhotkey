import os
PATH = os.path.dirname(os.path.abspath(__file__))
def pynput_keyboard_checkrule():
    seen = []
    modifierkey = ["ctrl", "alt", "shift", "cmd", "space", "enter", "tab", "esc", "up", "down", "left", "right", "delete", "page up", "page down", "home", "end"]
    #"win" : "cmd"
    with open(os.path.join(PATH, "hotkeylist.txt"), "r+", encoding="utf-8") as f:
        lines = f.readlines()
        f.seek(0)
        for line in lines:
            key = line.strip().split("+")
            true_keys = []
            """
            for i in range(len(a)):
                try:
                    num = modifierkey.index(a[i])
                    if num >= 0:
                        a[i] = f"<{a[i]}>"
                except: 
                    pass
            """
            for k in key:
                if k in modifierkey:
                    true_keys.append(f"<{k}>")
                else:
                    true_keys.append(k)
            frline = line.strip()
            endline = "+".join(true_keys)
            if endline != frline:
                f.write(endline + "\n")
            else:
                f.write(frline + "\n")
            #check same keys in a line
            for i in range(len(true_keys)):
                for j in range(i):
                    if true_keys[i] == true_keys[j]:
                        raise ValueError("keys have same in one line.")
            #check double hotkeys
            key_set = set(true_keys)
            for l, line_set in enumerate(seen):
                duplicates = key_set & line_set
                if len(duplicates) > 1:
                    raise ValueError("Hotkey has two or more duplicates.")
            seen.append(key_set)
    with open(os.path.join(PATH, "activity.txt")) as f:
        seen2 = []
        lines = f.readlines()
        allsamekey = 0
        for line in lines:
            key = line.strip().split("+")[0]
            keys = []
            if key == "CMCM":
                pass
            else:
                allsamekey += 1
                keys.append(key)
                for i in range(len(keys)):
                    for j in range(i):
                        if keys[i] == keys[j]:
                            raise ValueError("keys have same in one line.")
                if allsamekey > 1:
                    keyset = set(keys)
                    for l, line_set in enumerate(seen2):
                        duplicates = keyset & line_set
                        if len(duplicates) > 1:
                            raise ValueError("Hotkey has two or more duplicates.")
                    seen2.append(keyset)
if __name__ == "__main__":
    pynput_keyboard_checkrule()
