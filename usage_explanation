This application is just a base class for future projects which rely on socket connection. Connection protocol could be implemented in different 
ways depending on why the connection is requried, and this is one way of doing it.   

If you run the two scripts as they are from the command line/terminal, a connection will be established and terminated, and nothing interesting will happen. 
If you want to have fun without modifying the code, do the following on Windows:

open two command lines in the python files directory
type the following in order:
_____________________________________
python                (command line 1)
from server import *  (command line 1)
server = Server()     (command line 1)
server.start()        (command line 1)

python                (command line 2)
from client import *  (command line 2)
client = Client()     (command line 2)
client.receive()      (command line 2)
_____________________________________

Now, you can talk to the client command line from the server command line. If you want to send one message only, type:
________________________________________
server.send("Hello!")   (command line 1)
client.receive()        (command line 2)
________________________________________
Repeat as many times as you want.

If you want to open a stream of communication with the client, then type:
________________________________________________________________
server.send("Keep listening!", stream=True)   (command line 1)
client.receive()                              (command line 2)

server.send("msg1", stream=True)    (command line 1)
server.send("msg2", stream=True)    (command line 1)
server.send("msg3", stream=True)    (command line 1)
server.send("msg4", stream=False)   (command line 1)
________________________________________________________________

Now the client will keep receiveing data automatically without the receive() method, as long as the variable "stream" is set to True in the server send() method.
When the server is done sending data, it can release the client by setting the stream variable to False (default value) in the last send call.

If you want to close the connection, type <server.close()> or simply close the command lines.

Enjoy!
