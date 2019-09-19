import tkinter as tk


class MainAppView(tk.Frame):
    """Encapsulates of all the GUI logic.
    Attributes:
        master: where to open the Frame, by deafult root window
        title: Main Label

        one: Button
        two: Button
        three: Button
    """

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

        my_msg = tk.StringVar()  # For the messages to be sent.
        my_msg.set("Type your messages here.")
        entry_field = tk.Entry(self, textvariable=my_msg)
        #entry_field.bind("<Return>", send)
        entry_field.pack()
        send_button = tk.Button(top, text="Send", command=send)
        send_button.pack()

        #  Create the three buttons
        self.one = tk.Button(self)
        self.one["text"] = "Task 1"
        self.one.grid(row=2, column=0)

        self.two = tk.Button(self)
        self.two["text"] = "Task 2"
        self.two.grid(row=2, column=1)

        self.three = tk.Button(self)
        self.three["text"] = "Task 3"
        self.three.grid(row=2, column=2)

        self.four = tk.Button(self)
        self.four["text"] = "Task 4"
        self.four.grid(row=2, column=3)



    def __init__(self, master=None):
        tk.Frame.__init__(self, master)
        self.grid()
        # option is needed to put the main label in the window
        self.create_widgets()
