import socket
import time


class Client:
    # Socket client class
    def __init__(self, address=socket.gethostname()):
        # Each message should contain a header of size 10 characters
        # The header contains the number of characters in the message that follows
        self.header_size = 10

        self.sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.sock.connect((address, 1234))

    def receive(self):
        # Receive the header to know the message length
        # A "Zero-Header" (msg length of 0) is sent by the server to end the stream
        # First check for valid message format (valid header)
        # Second check if it's a zero-header, if so drop stream,
        # otherwise wait for the next header
        while True:
            header = self.sock.recv(self.header_size)
            try:
                # If an invalid header is received
                msg_size = int(header.decode("utf-8"))
            except ValueError:
                print("Invalid header!")
                continue

            if not msg_size:
                # Message ends when 0 is received as header size
                break

            msg = self.sock.recv(msg_size)
            print(msg)
        return


if __name__ == '__main__':
    client = Client()
    client.receive()
