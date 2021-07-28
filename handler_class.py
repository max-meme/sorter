from controller import *

class Handler:
    def __init__(this, UI):

        this.UI = UI
        

    def commander(this, text):
        text_list = text.split()
        command = text_list[0]
        text_list.pop(0)
        args = text_list
        if command == "":
            return
        if command == "blöd":
            this.UI.console_addline("> ne du")
            print(args)
        
        if command == "autohome":
            this.UI.console_addline("> autohoming")
            auto_home()
        
        if command == "moveto":
            this.UI.console_addline("> moving to coords")
            moveto(int(args[0]), int(args[1]), int(args[2]))
        