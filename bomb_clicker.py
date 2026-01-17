import tkinter as tk
from tkinter import messagebox
class BombClicker:
    def __init__(self, root):
        self.root = root
        self.root.title("Bomb Clicker")
        self.root.geometry("400x300")
        self.score = 0
        self.timer = 10
        self.running = False
        self.label = tk.Label(root, text="Score: 0", font=("Arial", 16))
        self.label.pack(pady=10)
        self.time_label = tk.Label(root, text="Time: 10", font=("Arial", 14))
        self.time_label.pack()
        self.button = tk.Button(root, text="CLICK", font=("Arial", 18), command=self.click)
        self.button.pack(pady=20)
        self.start_btn = tk.Button(root, text="Start", command=self.start_game)
        self.start_btn.pack()
    def start_game(self):
        if not self.running:
            self.running = True
            self.score = 0
            self.timer = 10
            self.update_labels()
            self.countdown()
    def click(self):
        if self.running:
            self.score += 1
            self.update_labels()
    def countdown(self):
        if self.timer > 0:
            self.timer -= 1
            self.update_labels()
            self.root.after(1000, self.countdown)
        else:
            self.running = False
            messagebox.showinfo("Game Over", f"Your score: {self.score}")
    def update_labels(self):
        self.label.config(text=f"Score: {self.score}")
        self.time_label.config(text=f"Time: {self.timer}")
if __name__ == "__main__":
    root = tk.Tk()
    app = BombClicker(root)
    root.mainloop()
