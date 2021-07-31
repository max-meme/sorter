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
            auto_home(this.UI)
        
        if command == "moveto":
            # check if negative
            if int(args[0]) < 0 or int(args[1]) < 0 or int(args[2]) < 0:
                this.UI.console_addline("Error: cannot move to negative")
                return
            this.UI.console_addline("> moving to coords")
            this.UI.setxyz(int(args[0]), int(args[1]), int(args[2]))
            moveto(int(args[0]), int(args[1]), int(args[2]), this.UI)

    def arrows(this, x, y):
        moverel(x, y, 0)
        
        