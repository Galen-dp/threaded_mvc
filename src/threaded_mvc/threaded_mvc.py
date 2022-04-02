import abc
import threading

__version__ = '0.0.3'

class Model(threading.Thread, abc.ABC):
    """_summary_

    Args:
        threading (_type_): _description_
    """
    def __init__(self, to_controller_queue, to_model_queue):
        """_summary_

        Args:
            controller_queue (_type_): _description_
            model_queue (_type_): _description_
        """
        # Call Thread class's init() function
        threading.Thread.__init__(self)

        # These are our message queues to and from the from controller
        self.to_controller_queue = to_controller_queue
        self.to_model_queue = to_model_queue

    @abc.abstractmethod
    def run(self):
        """Method representing the thread's activity.

        You must override this method in a subclass.
        """
        pass


class View(abc.ABC):
    """
    View Class
    """
    @abc.abstractmethod
    def __init__(this):
        pass


class Controller(abc.ABC):
    """
    Controller Class
    """
    @abc.abstractmethod
    def __init__(this):
        pass