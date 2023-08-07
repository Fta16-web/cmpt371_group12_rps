# cmpt371_group12_rps 
Rock-Paper-Scissors is a straightforward two-player hand game but in the form of an
online platform, where each participant chooses one of three distinct hand shapes.
These shapes are the familiar motions we commonly employ in face-to-face interactions
with friends: the gestures are classified as "rock," "paper," and "scissors."
The outcome is determined based on the rules: rock beats scissors, scissors beats
paper, and paper beats rock. The game is structured around a series of three rounds,
and whoever first scores three is victorious.
###################
How To Play The Game
##################
Setting up the Server:
One player (let's call them Player 1) acts as the server, and the other player (Player 2)
acts as the client.
Player 1 runs the server code on their computer. The server listens for incoming
connections from the client (Player 2).
Server Setup:
Player 1's computer will have a public IP address (or domain name) assigned by their
internet service provider (ISP). This IP address is used by Player 2 to connect to the
server remotely.
Player 1's computer opens a specific port (e.g., 12346) on the router to accept incoming
connections. This process is called port forwarding. It allows the server to be reachable
from outside the local network.
Connecting as Player 2:
Player 2 runs the client code on their computer. The client code prompts them to enter
the IP address (or domain name) of Player 1's computer and the port number (e.g.,
12346). Player 2's client code establishes a connection to the server running on Player
1's computer using the provided IP address and port number.for wifi connection make
sure that routers are set up to handle public IP reversing. If server uses dynamic IP, the
client needs to update IP accordingly.
