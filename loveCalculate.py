import tkinter as tk
from tkinter import messagebox
import random
import pygame
import threading

# Initialize music player
def play_music():
    pygame.mixer.init()
    pygame.mixer.music.load("background.mp3")  # 🔊 Replace with your music file
    pygame.mixer.music.set_volume(0.3)
    pygame.mixer.music.play(-1)  # Loop forever

# Main app
class LoveCalculatorApp:
    def __init__(self, root):
        self.root = root
        self.root.title("❤️ Love Calculator - Ritesh & Soniya Special Edition")
        self.root.geometry("400x500")
        self.root.configure(bg="#ffe6f0")

        self.title_label = tk.Label(root, text="💖 LOVE CALCULATOR 💖", font=("Helvetica", 18, "bold"), bg="#ffe6f0", fg="darkred")
        self.title_label.pack(pady=20)

        # Name 1
        self.name1_label = tk.Label(root, text="Enter First Name:", font=("Arial", 12), bg="#ffe6f0")
        self.name1_label.pack()
        self.name1_entry = tk.Entry(root, font=("Arial", 12))
        self.name1_entry.pack(pady=5)

        # Name 2
        self.name2_label = tk.Label(root, text="Enter Second Name:", font=("Arial", 12), bg="#ffe6f0")
        self.name2_label.pack()
        self.name2_entry = tk.Entry(root, font=("Arial", 12))
        self.name2_entry.pack(pady=5)

        # Calculate button
        self.calc_btn = tk.Button(root, text="💘 Calculate Love 💘", font=("Arial", 12, "bold"), bg="#ff4d88", fg="white", command=self.calculate_love)
        self.calc_btn.pack(pady=20)

        # Result
        self.result_label = tk.Label(root, text="", font=("Arial", 14, "bold"), bg="#ffe6f0", fg="purple")
        self.result_label.pack(pady=20)

        # Play music in separate thread
        threading.Thread(target=play_music, daemon=True).start()

    def calculate_love(self):
        name1 = self.name1_entry.get().strip().lower()
        name2 = self.name2_entry.get().strip().lower()

        if not name1 or not name2:
            messagebox.showwarning("Input Error", "Please enter both names.")
            return

        # Special love pairs
        special_pairs = [("ritesh", "soniya"), ("shiv", "parvati"), ("romeo", "juliet")]
        if (name1, name2) in special_pairs or (name2, name1) in special_pairs:
            score = 100
        else:
            base = sum(ord(c) for c in name1 + name2)
            score = (base % 101) + random.randint(-10, 10)
            score = min(100, max(0, score))

        message = self.get_love_message(score)
        self.result_label.config(text=f"💌 Love Score: {score}%\n{message}")

    def get_love_message(self, score):
        if score == 100:
            return "💍 True Love! Meant for each other forever!"
        elif score >= 80:
            return "💞 A strong bond! Keep loving."
        elif score >= 50:
            return "💕 A nice match. There's potential!"
        elif score >= 30:
            return "💔 Some sparks, but needs work."
        else:
            return "😢 Better as friends... maybe?"

# Launch app
if __name__ == "__main__":
    root = tk.Tk()
    app = LoveCalculatorApp(root)
    root.mainloop()
