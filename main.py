# This is the template code for the CNE335 Final Project
# Lidsyda Nouanphachan
# CNE 335 Fall Winter
def print_program_info():
    # TODO - Change your name
    print("Server Automator v0.1 by Your Name")

# This is the entry point to our program
if __name__ == '__main__':
    print_program_info()
    # TODO - Create a Server object
    # TODO - Call Ping method and print the results

import subprocess
import platform

def ping_server(host):
    # Define the ping command based on the OS
    param = "-n" if platform.system().lower() == "windows" else "-c"
    command = ["ping", param, "4", host]

    try:
        output = subprocess.run(command, stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True)
        return output.stdout
    except Exception as e:
        return f"Error: {e}"

# Example usage
server = "google.com"
print(ping_server(server))

#Citation Format (APA style): Python Software Foundation. (n.d.). subprocess — Subprocess management. Python documentation. Retrieved March 18, 2025, from https://docs.python.org/3/library/subprocess.html
