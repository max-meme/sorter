import tkinter as tk
from handler_class import Handler

class UI:
    def __init__(this, window_name):

        this.handler = Handler(this)
        this.window_name = window_name
        this.create_UI()
    
    def console_addline(this, text):
        this.Lb.insert(0, text)

    def send(this):
        text = this.inp.get()
        this.inp.delete(0, tk.END)
        this.console_addline(text)
        this.handler.commander(text)
        
    def create_UI(this):
        root = tk.Tk()
        root.title(this.window_name)
        root.geometry("800x700")

        #arrow buttons
        arrow_Frame = tk.Frame(root, height = 200, width = 200)
        arrow_Frame.place(anchor="w", relx=0, rely=0.5)

        chars = ["↖", "↑", "↗", "←", "o", "→", "↙", "↓", "↘"]
        command_inputs = []
        arrow_buttons = []
        posx = 0
        posy = 0
        for c in chars:
            temp_button = tk.Button(arrow_Frame, text = c, height = 2, width = 4)
            temp_button.grid(column = posx, row = posy, padx=2, pady=2)
            arrow_buttons.append(temp_button)
            posx = posx + 1
            if(posx == 3):
                posy = posy + 1
                posx = 0

        #console
        console_Frame = tk.Frame(root, background="#14a9ff")
        console_Frame.place(anchor="sw", relx=0, rely=1, relwidth=0.5, relheight=0.4)

        send_button = tk.Button(console_Frame, text="Send", command=this.send)
        send_button.pack(side="bottom", fill="x")

        inp = tk.Entry(console_Frame, background="grey")
        inp.pack(side="bottom", fill="x")
        this.inp = inp

        #console text with scrollbar
        console_text_Frame = tk.Frame(console_Frame)
        scrolly = tk.Scrollbar(console_text_Frame, orient=tk.VERTICAL)
        scollx = tk.Scrollbar(console_text_Frame, orient=tk.HORIZONTAL)
        Lb = tk.Listbox(console_text_Frame, yscrollcommand=scrolly.set, xscrollcommand=scollx.set, selectmode=tk.EXTENDED)
        this.Lb = Lb

        scrolly.config(command=Lb.yview)
        scollx.config(command=Lb.xview)

        scrolly.pack(side=tk.RIGHT, fill="y")
        scollx.pack(side=tk.BOTTOM, fill="x")
        Lb.pack(expand=True, fill=tk.BOTH)
        console_text_Frame.pack(expand=True, fill=tk.BOTH)
        
        #test scroll
        testlist = ["1", "2", "3", "4", "5", "6"]
        for item in testlist:
            Lb.insert(0, item)
        

        root.mainloop()

