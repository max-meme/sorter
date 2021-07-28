from typing import Match


class Handler:
    def __init__(this, UI):

        this.UI = UI
        

    def commander(this, command):
        match command:
                case "":
                    return
                case "du bist blöd":
                    this.UI.console_addline("> ne du")
        