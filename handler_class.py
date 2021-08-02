class Handler:
    def __init__(this, UI, controller, testing):
        this.testing = testing
        this.controller = controller
        this.UI = UI

    def commander(this, text):
        text_list = text.split()
        command = text_list[0]
        text_list.pop(0)
        args = text_list
        if command == "" or this.testing:
            return
        if command == "doof":
            this.UI.console_addline("> ne du")
            print(args)
        
        if command == "autohome":
            this.UI.console_addline("> autohoming")
            this.UI.setxyz(0, 0, 0)
            this.controller.auto_home(this.UI)
        
        if command == "moveto":
            # check if negative
            if int(args[0]) < 0 or int(args[1]) < 0 or int(args[2]) < 0:
                this.UI.console_addline("Error: cannot move to negative")
                return
            this.UI.console_addline("> moving to coords")
            this.UI.setxyz(int(args[0]), int(args[1]), int(args[2]))
            this.controller.moveto(int(args[0]), int(args[1]), int(args[2]), this.UI)

    def arrows(this, x, y):
        print("arrow triggered")
        this.controller.moverel(x, y, 0, this.UI)