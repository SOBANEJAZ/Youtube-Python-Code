import random
import customtkinter as tk

# Global Variables
magic_number = random.randint(1, 100)
attempts = 0
feedback_label = None


# Function to Start the Game
def start(root):
    # GUI window
    root.geometry("500x200")
    root.title("Guess the Magic Number")

    # Global Variable
    global magic_number
    global attempts
    global feedback_label

    # Creating the GUI elements
    label = tk.CTkLabel(root, text="Guess a number between 1 to 100", font=tk.CTkFont(size=30))
    entry = tk.CTkEntry(root, font=tk.CTkFont(size = 30))
    feedback_label = tk.CTkLabel(root, text= "", font = tk.CTkFont(size = 30))

    #Layout the GUI elements
    label.pack(pady=10)
    entry.pack(pady=10)
    feedback_label.pack(pady=10)

    def check_guess_wrapper(*args):

        check_guess(root, entry.get())

    entry.bind("<Return>", check_guess_wrapper)


    root.mainloop()

#function to check player guess
def check_guess(root, player_guess):
    global attempts

    attempts += 1

    #checks the guess
    if int(player_guess) == magic_number:
        feedback_label.configure(text = "You Won - Number of Attempts: " + str(attempts))

    else:
        if int(player_guess) > magic_number:
            feedback_label.configure(text = "Too Big!!!")
        else:
            feedback_label.configure(text = "Too Small!!!")

#Starts the Game
start(tk.CTk())
