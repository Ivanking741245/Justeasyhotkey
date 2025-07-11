def pynput_keyboard_checkrule():
    modifierkey = ["ctrl", "alt", "shift", "cmd", "space", "enter", "tab", "esc", "up", "down", "left", "right", "delete", "page up", "page down", "home", "end"]
    #"win" : "cmd"
    with open("hotkeylist.txt", "r+", encoding="utf-8") as f:
        lines = f.readlines()
        f.seek(0)
        for line in lines:
            a = line.strip().split("+")
            for i in range(len(a)):
                try:
                    num = modifierkey.index(a[i])
                    if num >= 0:
                        a[i] = f"<{a[i]}>"
                except: 
                    pass
            frline = line.strip()
            endline = "+".join(a)
            if endline != frline:
                f.write(endline + "\n")
            else:
                f.write(frline + "\n")
if __name__ == "__main__":
    pynput_keyboard_checkrule()
