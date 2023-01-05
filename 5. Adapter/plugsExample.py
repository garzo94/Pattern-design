from abc import ABC, abstractmethod

# Creating a Uk Plug interface
class IUkPlug(ABC):

    @staticmethod
    @abstractmethod
    def electricity_220v():
        """electricity supply, in VOLT"""

# Creating a Uk plug class that inherence from UkPlug interface
class UkPlug(IUkPlug):

    def electricity_220v(self):
        print("220 Volt")

# Creating a Us Socket Interface
class IUsSocket(ABC):

    @staticmethod
    @abstractmethod
    def electricity_110v():
        """electricity supply"""

# Creating a US socket that inherence from Us Socket Interface
class UsSocket(IUsSocket):

    def electricity_110v(self):
        print("110 Volt")

# Creating an adapter for our Uk plug that supports an Us Socket
class UktoUsAdapter(IUkPlug):

    def __init__(self):
        self.us_socket = UsSocket()

    def electricity_220v(self):
        # Changing electricity supply
        self.us_socket.electricity_110v()

my_plug = UkPlug()
my_plug.electricity_220v()
#220 Volt
my_plug = UktoUsAdapter()
my_plug.electricity_220v()
#110 Volt