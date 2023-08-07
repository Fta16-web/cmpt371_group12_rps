import tkinter as tk
from tkinter import messagebox
from PIL import Image, ImageTk
import socket

Player1_score = 0
Player2_score = 0

def outcome_handler(choice):
    global Player1_score, Player2_score

    client_socket.send(choice.encode())
    host_choice = client_socket.recv(1024).decode()

    client_choice_var.set("Player 2 choice: " + choice.capitalize())
    host_choice_var.set("Player 1 choice: " + host_choice.capitalize())

    if choice == host_choice:
        outcome_var.set("It's a tie!")
        outcome_label.config(fg="white")  # Change style for tie
    elif (choice == "rock" and host_choice == "scissors") or (choice == "paper" and host_choice == "rock") or (choice == "scissors" and host_choice == "paper"):
        outcome_var.set("You win!")
        outcome_label.config(fg="green")  # Change style for win
        Player1_score += 1
    else:
        outcome_var.set("Player 1 wins!")
        outcome_label.config(fg="red")  # Change style for lose
        Player2_score += 1

    update_scores()

    # Add a delay of 2 seconds before resetting the client's and host's choice labels
    master.after(2000, reset_choices)

def update_scores():
    label_client_score.config(text="Player 2 score: " + str(Player1_score))
    label_host_score.config(text="Player 1 score: " + str(Player2_score))

    if Player1_score >= 3 or Player2_score >= 3:
        winner = "Player 2" if Player1_score >= 3 else "Player 1"
        winner_label.config(text=f"The {winner} wins the game!", font=("calibri", 20, "bold"), fg="white")
        reset_scores()
        # Show the winner for 5 seconds and then clear the winner label
        master.after(5000, clear_winner)

def reset_scores():
    global Player1_score, Player2_score
    Player1_score = 0
    Player2_score = 0
    update_scores()

def reset_choices():
    client_choice_var.set("Player 2 choice: ")
    host_choice_var.set("Player 1 choice: ")
    outcome_var.set("")

def clear_winner():
    winner_label.config(text="")

master = tk.Tk()
master.title("RSP")
master.geometry("750x600")  # Sets a larger window size

# Make the window background black
master.configure(bg="black")

# Create StringVar variables for dynamic text
client_choice_var = tk.StringVar()
host_choice_var = tk.StringVar()
outcome_var = tk.StringVar()

# label
label = tk.Label(master, text="Welcome to Rock-Paper-Scissors!", font=("calibri", 24, "bold"), fg="white", bg="black")
label.grid(row=0, column=0, columnspan=3, pady=20)

label2 = tk.Label(master, text="Select your hand", font=("calibri", 20, "bold"), fg="white", bg="black")
label2.grid(row=3, column=0, columnspan=3, pady=20)

label_client_score = tk.Label(master, text="Player 2 score: 0", font=("calibri", 16), fg="white", bg="black")
label_client_score.grid(row=1, column=0, sticky="w", padx=20)

label_host_score = tk.Label(master, text="Player 1 score: 0", font=("calibri", 16), fg="white", bg="black")
label_host_score.grid(row=1, column=2, sticky="e", padx=20)

client_choice_label = tk.Label(master, textvariable=client_choice_var, font=("calibri", 18), width=20, fg="white", bg="black")  # Set a fixed width for the labels
client_choice_label.grid(row=2, column=0, sticky="w")

host_choice_label = tk.Label(master, textvariable=host_choice_var, font=("calibri", 18), width=20, fg="white", bg="black")  # Set a fixed width for the labels
host_choice_label.grid(row=2, column=2, sticky="e")

outcome_label = tk.Label(master, textvariable=outcome_var, font=("calibri", 20), bd=4, bg="black")
outcome_label.grid(row=2, column=1)

rock_img = Image.open("./png/rock.jpeg")
rock_img = rock_img.resize((200, 200), Image.LANCZOS)
rock_photo = ImageTk.PhotoImage(rock_img)
rock_label = tk.Label(master, image=rock_photo, bd=0, bg="black")
rock_label.grid(row=4, column=0, padx=20, pady=20)
rock_label.bind("<Button-1>", lambda event: outcome_handler("rock"))

paper_img = Image.open("./png/paper.png")
paper_img = paper_img.resize((200, 200), Image.LANCZOS)
paper_photo = ImageTk.PhotoImage(paper_img)
paper_label = tk.Label(master, image=paper_photo, bd=0, bg="black")
paper_label.grid(row=4, column=1, padx=20, pady=20)
paper_label.bind("<Button-1>", lambda event: outcome_handler("paper"))

scissors_img = Image.open("./png/scissors.jpeg")
scissors_img = scissors_img.resize((200, 200), Image.LANCZOS)
scissors_photo = ImageTk.PhotoImage(scissors_img)
scissors_label = tk.Label(master, image=scissors_photo, bd=0, bg="black")
scissors_label.grid(row=4, column=2, padx=20, pady=20)
scissors_label.bind("<Button-1>", lambda event: outcome_handler("scissors"))

winner_label = tk.Label(master, text="", font=("calibri", 20, "bold"), fg="white", bg="black")
winner_label.grid(row=5, column=0, columnspan=3, pady=20)

# Connect to the server
host = "localhost"# for remote change it to server external IP
port = 12346
client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client_socket.connect((host, port))

master.mainloop()
