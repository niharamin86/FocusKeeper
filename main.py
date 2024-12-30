import tkinter as tk
from tkinter import messagebox

class FocusTimerApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Focus Timer")
        self.root.geometry("300x200")

        self.time_left = 25 * 60  # Default to 25 minutes
        self.running = False

        # Create a frame for centering
        main_frame = tk.Frame(root)
        main_frame.pack(expand=True)

        # Timer display
        self.timer_label = tk.Label(main_frame, text=self.format_time(self.time_left), font=("Helvetica", 24))
        self.timer_label.pack(pady=20)

        # Buttons frame
        buttons_frame = tk.Frame(main_frame)
        buttons_frame.pack()

        self.start_button = tk.Button(buttons_frame, text="Start", command=self.start_timer)
        self.start_button.grid(row=0, column=0, padx=10)

        self.pause_button = tk.Button(buttons_frame, text="Pause", command=self.pause_timer)
        self.pause_button.grid(row=0, column=1, padx=10)

        self.reset_button = tk.Button(buttons_frame, text="Reset", command=self.reset_timer)
        self.reset_button.grid(row=0, column=2, padx=10)

    def format_time(self, seconds):
        minutes, seconds = divmod(seconds, 60)
        return f"{minutes:02}:{seconds:02}"

    def update_timer(self):
        if self.running and self.time_left > 0:
            self.time_left -= 1
            self.timer_label.config(text=self.format_time(self.time_left))
            self.root.after(1000, self.update_timer)
        elif self.time_left == 0:
            self.running = False
            messagebox.showinfo("Focus Timer", "Time's up! Take a break.")

    def start_timer(self):
        if not self.running:
            self.running = True
            self.update_timer()

    def pause_timer(self):
        self.running = False

    def reset_timer(self):
        self.running = False
        self.time_left = 25 * 60  # Reset to 25 minutes
        self.timer_label.config(text=self.format_time(self.time_left))

# Create the application
root = tk.Tk()
app = FocusTimerApp(root)
root.mainloop()
