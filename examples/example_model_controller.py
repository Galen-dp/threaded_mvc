"""
This is a an example of how to extend the Model and Controller classes
from threaded_mvc.


"""
import logging
import queue
import random
import time
from threaded_mvc import Model, Controller


DELAY_INCREASE = "DELAY_INCREASE"
DELAY_DECREASE = "DELAY_DECREASE"
DELAY_UPDATE = "DELAY_UPDATE"
DATA_RANDOM = "DATA_RANDOM"

logger = logging.getLogger(__name__)

class Exmodel(Model):
    """
    Brief summary of class purpose or behavior

    Any public methods
        Brief description

    Any class properties/attributes
        Brief description

    Anything to do with interfaces or subclassers

    Args:
        Model (_type_): _description_
    """
    def __init__(self, to_controller_queue, to_model_queue):
        """_summary_

        Args:
            to_controller_queue (_type_): _description_
            to_model_queue (_type_): _description_
        """
        super().__init__(to_controller_queue, to_model_queue)

        # Kill the thread if the main thread exits
        self.daemon = True

        # Time count.
        self.time_delay = 1

    def run(self):
        """_summary_
        """
        message = ["", ""]

        # Send a delay time update message to the controller
        self.to_controller_queue.put([DELAY_UPDATE, self.time_delay])

        while True:
            try:
                message = self.to_model_queue.get(block=False)
                logger.debug("Model: Received event: %s", message[0])
                if message[0] is None:
                    logger.debug("Model: exiting...")
                    return
                if message[0] == DELAY_INCREASE:
                    self.time_delay += message[1]
                    logger.debug("Model: Increasing time delay - Delay is now %s", self.time_delay)

                    # Send a delay time update message to the controller
                    self.to_controller_queue.put([DELAY_UPDATE, self.time_delay])

                elif message[0] == DELAY_DECREASE:
                    self.time_delay -= message[1]
                    if self.time_delay <= 0:
                        self.time_delay = 1
                    # Send a delay time update message to the controller
                    self.to_controller_queue.put([DELAY_UPDATE, self.time_delay])
                    logger.debug("Model: Decreasing time delay - Delay is now %s", self.time_delay)

                else:
                    print("Model: Unknown message", message[0])

            except queue.Empty:
                pass

            # Sleep to simulate a long blocking process.
            time.sleep(self.time_delay)

            # Generate random number to send to listener(s).
            x = random.randint(10000, 99999)
            logger.debug("Model: Random data is %s", x)

            # Send random number to the listener(s).
            self.to_controller_queue.put([DATA_RANDOM, x])


class Excontroller(Controller):
    def __init__(self, view):
        # Create the message queues.
        self.to_controller_queue = queue.Queue()
        self.to_model_queue = queue.Queue()

        # Call the super
        super().__init__(self.to_controller_queue, self.to_model_queue)

        # Save the program's GUI view
        self.view = view

    def start(self):
        # Tie callbacks to the view.
        self.view.set_button_up_callback(self.button_up_pressed)
        self.view.set_button_down_callback(self.button_down_pressed)

        # Create and start the model
        self.model = Exmodel(self.to_controller_queue, self.to_model_queue)
        self.model.start()

#        self.update_time = 1
#        self.view.update_time(self.update_time)

        # Execute main loop
        self.view.after(100, self.controller_loop)
        self.view.mainloop()

    def controller_loop(self):
        message = ["", ""]
        try:
            message = self.to_controller_queue.get(block=False)
            logger.debug("Controller: Received event: %s - %s", message[0], str(message[1]))
            if message[0] is None:
                logger.debug("Controller: exiting...")
                return

        except queue.Empty:
            pass

        if message[0] == DELAY_UPDATE:
            logger.debug("Controller: Updating time delay display")
            self.view.update_time(message[1])
        elif message[0] == DATA_RANDOM:
            logger.debug("Controller: Updating random data display")
            self.view.update_data(message[1])

        self.view.after(100, self.controller_loop)

    def button_up_pressed(self, event):
        logger.debug("Controller: Up button pressed")
        self.to_model_queue.put([DELAY_INCREASE, 1], block=False)

    def button_down_pressed(self, event):
        logger.debug("Controller: Down button pressed")
        self.to_model_queue.put([DELAY_DECREASE, 1], block=False)


if __name__ == "__main__":
    print("Run one of the example_xxx.py files instead.")
