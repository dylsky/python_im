import tkinter as tk


class MainAppView(tk.Frame):
    def start_gui(self, ok=True):
        """Starts the GUI, if everything ok , to change"""
        if ok:
            self.mainloop()
        else:
            self.master.destroy()

    def create_widgets(self):
        """Create the set of initial widgets."""
        #  Create the label
        self.title = tk.Label(self, text="Just chatting")
        self.title.grid(row=0, column=0, columnspan=4, sticky=tk.E + tk.W)

        self.rooms_frame = tk.Frame(self)
        rooms_scrollbar = tk.Scrollbar(self.rooms_frame)  # To navigate through past messages.
        self.rooms_list = tk.Listbox(self.rooms_frame, height=30, width=32, yscrollcommand=rooms_scrollbar.set)
        rooms_scrollbar.pack(side=tk.RIGHT, fill=tk.Y)
        self.rooms_list.pack(side=tk.LEFT, fill=tk.BOTH)
        self.rooms_list.pack()
        self.rooms_frame.grid(row=1, column=0)

        self.messages_frame = tk.Frame(self)
        messages_scrollbar = tk.Scrollbar(self.messages_frame)  # To navigate through past messages.
        self.msg_list = tk.Listbox(self.messages_frame, height=30, width=128, yscrollcommand=messages_scrollbar.set)
        messages_scrollbar.pack(side=tk.RIGHT, fill=tk.Y)
        self.msg_list.pack(side=tk.LEFT, fill=tk.BOTH)
        self.msg_list.pack()
        self.messages_frame.grid(row=1, column=1, columnspan=3)

        self.my_msg = tk.StringVar()  # For the messages to be sent.
        self.my_msg.set("Type your messages here.")
        entry_field = tk.Entry(self, textvariable=self.my_msg, width=160)
        #entry_field.bind("<Return>", send)
        entry_field.grid(row=2, column=0, columnspan=3, padx=10, pady=15)
        self.send_button = tk.Button(self, text="Send")
        self.send_button.grid(row=2, column=3, sticky="nwse", padx=10, pady=15)

    def __init__(self, master=None):
        tk.Frame.__init__(self, master)
        self.grid()
        # option is needed to put the main label in the window
        self.create_widgets()

    def update_messages(self, new_message):
        self.msg_list.insert(tk.END, new_message)
