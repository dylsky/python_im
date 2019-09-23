from src.views.MainAppView import MainAppView
from src.models.MainAppModels import MainAppModel
from socket import AF_INET, socket, SOCK_STREAM
from threading import Thread
import tkinter as tk
import select


class MainAppController(object):
    def init_view(self, root):
        """Initializes GUI view. In addition it bindes the Buttons with the callback methods."""
        self.view = MainAppView(master=root)
        self.model = MainAppModel()
        self.model.new_message.addCallback(self.message_received)

        self.HOST = "127.0.0.1"
        self.PORT = 33000
        self.BUFSIZ = 1024
        self.ADDR = (self.HOST, self.PORT)

        self.client_socket = socket(AF_INET, SOCK_STREAM)
        self.client_socket.connect(self.ADDR)

        receive_thread = Thread(target=self.message_listen)
        receive_thread.start()

        self.view.entry_field.bind("<Return>", self.send)
        self.view.entry_field.bind("<FocusIn>", self.clear_input_on_focus)
        self.view.send_button.config(command=self.send)

        root.protocol("WM_DELETE_WINDOW", self.on_closing)

        # Start the gui
        self.view.start_gui()

    def message_received(self, message):
        self.view.msg_list.insert(tk.END, message)

    def message_listen(self):
        """Handles receiving of messages."""
        while True:
            try:
                self.client_socket.setblocking(0)
                ready = select.select([self.client_socket], [], [], 1)
                if ready[0]:
                    msg = self.client_socket.recv(self.BUFSIZ).decode("utf8")
                    self.message_received(msg)
            except OSError:  # Possibly client has left the сhat.
                break

    def send(self, event=None):  # event is passed by binders.
        """Handles sending of messages."""
        msg = self.view.my_msg.get()
        self.view.my_msg.set("")  # Clears input field.
        self.client_socket.send(bytes(msg, "utf8"))
        if msg == "{quit}":
            self.client_socket.close()
            self.view.quit()

    def on_closing(self, event=None):
        """This function is to be called when the window is closed."""
        self.view.my_msg.set("{quit}")
        self.send()

    def clear_input_on_focus(self, event=None):
        self.view.my_msg.set("")

