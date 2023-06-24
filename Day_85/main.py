import tkinter as tk
import time

class TypingSpeedTestApp:
    def __init__(self, master):
        self.master = master
        master.title("Typing Speed Test")

        self.text_to_type = "The quick brown fox jumps over the lazy dog."
        self.words_typed = 0
        self.start_time = None

        self.text_label = tk.Label(master, text=self.text_to_type)
        self.text_label.pack()

        self.input_text = tk.Text(master, height=10, width=30)
        self.input_text.pack()

        self.start_button = tk.Button(master, text="Start", command=self.start_typing)
        self.start_button.pack()

        self.result_label = tk.Label(master, text="")
        self.result_label.pack()

    def start_typing(self):
        self.words_typed = 0
        self.start_time = time.time()
        self.input_text.config(state=tk.NORMAL)
        self.input_text.delete("1.0", tk.END)
        self.input_text.focus_set()
        self.start_button.config(state=tk.DISABLED)
        self.master.bind("<Return>", self.check_typing)

    def check_typing(self, event):
        typed_text = self.input_text.get("1.0", tk.END).strip()
        typed_words = typed_text.split()
        self.words_typed = len(typed_words)

        elapsed_time = time.time() - self.start_time
        minutes = elapsed_time / 60
        wpm = self.words_typed / minutes if minutes > 0 else 0

        self.result_label.config(text="Words Per Minute: {:.2f}".format(wpm))
        self.input_text.config(state=tk.DISABLED)
        self.start_button.config(state=tk.NORMAL)
        self.master.unbind("<Return>")

# Create the main Tkinter window
root = tk.Tk()
typing_speed_test = TypingSpeedTestApp(root)
root.mainloop()
