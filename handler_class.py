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
        if command == "doof":
            this.UI.console_addline("> ne du")
            print(args)
        
        if command == "autohome":
            this.UI.console_addline("> autohoming")
            this.UI.setxyz(0, 0, 0)
            auto_home()
        
        if command == "moveto":
            this.UI.console_addline("> moving to coords")
            this.UI.setxyz(int(args[0]), int(args[1]), int(args[2]))
            moveto(int(args[0]), int(args[1]), int(args[2]))

    def arrows(this, x, y):
        print("hey")
        