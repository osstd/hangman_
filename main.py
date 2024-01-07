import tkinter as tk
from tkinter import messagebox
import random


class HangmanGame:
    def __init__(self, master):
        self.master = master
        self.master.title("Hangman Game")

        self.words = ["don't", "forget", "to", "input", "your", "words", "to", "be", "guessed"]
        self.word_to_guess = random.choice(self.words)
        self.guesses_left = 6
        self.guessed_letters = set()

        self.word_display = tk.Label(self.master, text=self.display_word())
        self.word_display.pack(pady=10)

        self.guess_label = tk.Label(self.master, text=f"Guesses left: {self.guesses_left}")
        self.guess_label.pack()

        self.entry = tk.Entry(self.master)
        self.entry.pack(pady=10)

        self.guess_button = tk.Button(self.master, text="Guess", command=self.make_guess)
        self.guess_button.pack()

    def display_word(self):
        return " ".join(letter if letter in self.guessed_letters else "_" for letter in self.word_to_guess)

    def make_guess(self):
        try:
            guess = self.entry.get().lower()

            if guess.isalpha() and len(guess) == 1:
                if guess in self.guessed_letters:
                    messagebox.showinfo("Duplicate Guess", "You already guessed that letter. Try again.")
                else:
                    self.guessed_letters.add(guess)

                    if guess not in self.word_to_guess:
                        self.guesses_left -= 1

                    self.update_display()

                    if self.guesses_left == 0:
                        self.game_over("Sorry, you ran out of guesses. The word was: " + self.word_to_guess)
                    elif set(self.word_to_guess) == self.guessed_letters:
                        self.game_over("Congratulations! You guessed the word: " + self.word_to_guess)

            else:
                messagebox.showerror("Invalid Guess", "Please enter a valid single letter.")

        except ValueError:
            messagebox.showerror("Error", "Please enter a valid letter.")

    def update_display(self):
        self.word_display.config(text=self.display_word())
        self.guess_label.config(text=f"Guesses left: {self.guesses_left}")

    def game_over(self, message):
        messagebox.showinfo("Game Over", message)
        self.master.destroy()


# Main function
def main():
    root = tk.Tk()
    game = HangmanGame(root)
    root.mainloop()


if __name__ == "__main__":
    main()
