# coding=utf-8
import tkinter as tk
from handler_class import Handler
from datetime import datetime

class UI:
    def __init__(this, window_name, controller):
        this.controller = controller
        this.handler = Handler(this, this.controller)
        this.window_name = window_name

        this.x_Label_text = tk.StringVar()
        this.y_Label_text = tk.StringVar()
        this.z_Label_text = tk.StringVar()

        this.create_UI()
    
    def console_addline(this, text):
        now = datetime.now()
        current_time = now.strftime("%H:%M:%S")
        this.Lb.insert(0, "[" + current_time + "]: " + text)

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
        s = 10 #configure amount of steps here
        command_inputs = [
            this.handler.arrows(-s, s), this.handler.arrows(0, s), this.handler.arrows(s, s),
            this.handler.arrows(-s, 0), this.controller.auto_home(this), this.handler.arrows(s, 0),
            this.handler.arrows(-s, -s), this.handler.arrows(0, -s), this.handler.arrows(s, -s)
        ]
        arrow_buttons = []
        posx = 0
        posy = 0
        i = 0
        for c in chars:
            temp_button = tk.Button(arrow_Frame, text = c, height = 2, width = 4, command=lambda: command_inputs[i])
            temp_button.grid(column = posx, row = posy, padx=2, pady=2)
            arrow_buttons.append(temp_button)
            posx = posx + 1
            if(posx == 3):
                posy = posy + 1
                posx = 0
            i = i + 1

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
        
        #x y z indicators
        indicator_Frame = tk.Frame(root, relief=tk.RIDGE, bd=3)
        indicator_Frame.place(relx=0.5, rely=1, anchor="sw")

        this.x_Label_text.set("x: 0")
        this.y_Label_text.set("y: 0")
        this.z_Label_text.set("z: 0")

        x_Label = tk.Label(indicator_Frame, textvariable = this.x_Label_text, background="#1cff20").pack(side=tk.TOP)
        y_Label = tk.Label(indicator_Frame, textvariable = this.y_Label_text, background="#ff3c2e").pack(side=tk.TOP)
        z_Label = tk.Label(indicator_Frame, textvariable = this.z_Label_text, background="#2ec7ff").pack(side=tk.TOP)
        

        root.mainloop()

    #setter for x y z
    def setxyz(this, x, y, z):
        this.x_Label_text.set("x: " + str(x))
        this.y_Label_text.set("y: " + str(y))
        this.z_Label_text.set("z: " + str(z))

