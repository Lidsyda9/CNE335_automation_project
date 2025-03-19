class Server:
    """ Server class for representing and manipulating servers. """

    def __init__(self, server_ip):
        # TODO -
        self.server_ip = server_ip

    def ping(self):
        # TODO - Use os module to ping the server
        return

from ipaddress import ip_address


class Server:
    """ Server class for representing and manipulating servers. """

    def __init__(self, server_ip):
        # TODO -
        self.server_ip = server_ip

    def ping(self):
        # TODO - Use os module to ping the server
        return

import os
import platform
from ipaddress import ip_address

class Server:
    """ Server class for representing and manipulating servers. """

    def __init__(self, server_ip):
        # Validate if the provided IP is valid
        try:
            self.server_ip = ip_address(server_ip)
        except ValueError:
            raise ValueError(f"Invalid IP address: {server_ip}")

    def ping(self):
        """Pings the server and returns whether it's reachable."""
        # Define the ping command based on the OS
        param = "-n" if platform.system().lower() == "windows" else "-c"
        command = ["ping", param, "4", str(self.server_ip)]

        # Execute the ping command
        response = os.system(" ".join(command))

        # Return the result based on the response
        if response == 0:
            return f"Server {self.server_ip} is reachable."
        else:
            return f"Server {self.server_ip} is not reachable."

# Example usage:
server = Server("8.8.8.8")  # Replace with your server IP
print(server.ping())
#Python Software Foundation. (n.d.). os — Miscellaneous operating system interfaces. In Python 3 documentation. Retrieved from https://docs.python.org/3/library/os.html
#Python Software Foundation. (n.d.). platform — Access to underlying platform’s identifying data. In Python 3 documentation. Retrieved from https://docs.python.org/3/library/platform.html
