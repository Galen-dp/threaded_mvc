import tkinter as tk
from tkinter import RAISED, RIDGE, ttk
from threaded_mvc import Model, View, Controller


class Exmodel(Model):
    def __init__(self):
        pass

    def run(self):
        pass


class Excontroller(Controller):
    def __init__(self, model, view):
        self._model = model
        self._view = view


class Exview(tk.Tk, View):
    def __init__(self):
        """View initializer."""
        super().__init__()

        # Build the GUI
        self.title("Tkinter Example")
        self.columnconfigure(0, weight=1, minsize=75)
        self.rowconfigure(0, weight=1, minsize=75)
        self.frame = ttk.Frame(relief=RIDGE, borderwidth=5)
        self.frame.grid(row=0, column=0, padx=5, pady=5)
        self.button_up = ttk.Button(master=self.frame, text="^")
        self.button_up.pack(side=tk.LEFT)
        self.label_value = ttk.Label(master=self.frame, width=15, relief=RIDGE, borderwidth=5, text="Hello World!")
        self.label_value.configure(anchor="center")
        self.label_value.pack(side=tk.LEFT)
        self.button_down = ttk.Button(master=self.frame, text="v")
        self.button_down.pack(side=tk.LEFT)

#        self.frame.pack()



def main():
    # Create the calculator's GUI
    view = Exview()

    # Create the model
    model = Exmodel()

    # Create the controller and run it
    controller = Excontroller(model, view)

    # Execute calculator's main loop
    view.mainloop()


if __name__ == "__main__":
    main()
