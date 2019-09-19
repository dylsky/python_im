from src.views.MainAppView import MainAppView


class MainAppController(object):

    def nothing(self):
        pass

    def receive(self):
        """Handles receiving of messages."""
        while True:
            try:
                msg = client_socket.recv(BUFSIZ).decode("utf8")
                msg_list.insert(tkinter.END, msg)
            except OSError:  # Possibly client has left the chat.
                break

    def send(self, event=None):  # event is passed by binders.
        """Handles sending of messages."""
        msg = my_msg.get()
        my_msg.set("")  # Clears input field.
        client_socket.send(bytes(msg, "utf8"))
        if msg == "{quit}":
            client_socket.close()
            top.quit()

    def on_closing(self, event=None):
        """This function is to be called when the window is closed."""
        my_msg.set("{quit}")
        send()

    def init_view(self, root):
        """Initializes GUI view. In addition it bindes the Buttons with the callback methods."""
        self.view = MainAppView(master=root)

        # Bind buttons with callback methods
        self.view.one["command"] = self.nothing
        self.view.two["command"] = self.nothing
        self.view.three["command"] = self.nothing
        self.view.four["command"] = self.nothing

        # Start the gui
        self.view.start_gui()
