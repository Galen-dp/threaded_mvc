import logging
import tkinter as tk
import example_model_controller as mc
from tkinter import RIDGE, ttk
from threaded_mvc import View


class Exview(tk.Tk, View):
    def __init__(self):
        """View GUI initialization."""
        super().__init__()

        # Build the GUI
        self.title("Tkinter Example")
        self.columnconfigure(0, weight=1, minsize=75)
        self.rowconfigure(0, weight=1, minsize=75)

        # Delay adjustment frame
        self.frame_timing = ttk.Frame(relief=RIDGE, borderwidth=5)
        self.frame_timing.grid(row=0, column=0, padx=5, pady=5)

        # Increase delay button
        self.button_up = ttk.Button(master=self.frame_timing, text="^")
        self.button_up.pack(side=tk.LEFT)

        # Delay display
        self.label_time_delay = ttk.Label(master=self.frame_timing, width=15, relief=RIDGE, borderwidth=5)
        self.label_time_delay.configure(anchor="center")
        self.label_time_delay.pack(side=tk.LEFT)

        # Decrease delay button
        self.button_down = ttk.Button(master=self.frame_timing, text="v")
        self.button_down.pack(side=tk.LEFT)

        # Random data frame
        self.frame_value = ttk.Frame(relief=RIDGE, borderwidth=5)
        self.frame_value.grid(row=1, column=0, padx=5, pady=5)
        self.label_value = ttk.Label(master=self.frame_value, width=15, relief=RIDGE, borderwidth=5, text="0")
        self.label_value.configure(anchor="center")
        self.label_value.pack(side=tk.LEFT)

    def update_time(self, seconds):
        if seconds == 1:
            self.label_time_delay.configure(text=str(seconds) + " second")
        else:
            self.label_time_delay.configure(text=str(seconds) + " seconds")

    def update_data(self, data):
        self.label_value.configure(text=str(data))

    def set_button_up_callback(self, callback):
        self.button_up.bind("<Button-1>", callback)

    def set_button_down_callback(self, callback):
        self.button_down.bind("<Button-1>",  callback)


def main():
    # Setup logging
    logging.basicConfig(filename='example.log',
                        level=logging.DEBUG,
                        #format='%(asctime)s %(message)s',
                        #datefmt='%m/%d/%Y %I:%M:%S %p')
    )
    logging.info('---Log Start---')
    # Create the controller and run it
    view = Exview()
    controller = mc.Excontroller(view)
    controller.start()
    logging.info('---Log End---')


if __name__ == "__main__":
    main()
