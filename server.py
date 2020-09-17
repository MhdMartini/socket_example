import socket
import time


class Server:
    def __init__(self, address=socket.gethostname(), port=1234, num_clients=1):
        # Header size is 10 characters (supports message lengths up to 100 Billion - 1 characters
        self.header_size = 10

        # Create socket object
        # Turn it into an actual socket
        # Have a default que of 1
        self.sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.sock.bind((address, port))
        self.sock.listen(num_clients)
        self.client, self.address = None, None

    def start(self):
        # Accept a client
        self.client, self.address = self.sock.accept()
        print(f"Connection from {self.address} has been established!")

    def send(self, msg, stream=False):
        # Send a message. If stream is True the client knows there is more to come
        # Message format: Header + message
        # Header is 10 characters long
        header = f"{len(msg):<{self.header_size}}"
        msg = bytes(header + msg, "utf-8")
        self.client.send(msg)
        if not stream:
            header = f"{0:<{self.header_size}}"
            self.client.send(bytes(header + "", "utf-8"))

    def close(self):
        self.client.close()

    def reset(self):
        self.__init__()


if __name__ == '__main__':
    server = Server()
    server.start()

    # Communicate here

    server.close()



