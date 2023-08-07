import socket

host = "localhost"  # for remote change it to server external IP
port = 12346

server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server_socket.bind((host, port))
server_socket.listen(2)

print("Waiting for players...")

player1_socket, player1_address = server_socket.accept()
print("Player 1 connected. Waiting for Player 2...")

player2_socket, player2_address = server_socket.accept()
print("Player 2 connected. Game starting!")

player1_socket.send("Player 2 connected. Game starting!".encode())

while True:
    player1_choice = player1_socket.recv(1024).decode()
    player2_choice = player2_socket.recv(1024).decode()

    print(f"Player 1 chose: {player1_choice}")
    print(f"Player 2 chose: {player2_choice}")

    player1_socket.send(player2_choice.encode())
    player2_socket.send(player1_choice.encode())

    print("Choices sent to players.")
