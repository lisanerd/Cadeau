import tkinter as tk
from PIL import Image, ImageTk
import os
import fun_math

class FunRiddles:
    def __init__(self, main_frame, window_width, window_height, show_note_callback):
        self.main_frame = main_frame
        self.window_width = window_width
        self.window_height = window_height
        self.show_note_callback = show_note_callback
        self.feedback_text = None  # Store reference to feedback text
        
        # Clear all widgets from the main frame
        for widget in self.main_frame.winfo_children():
            widget.destroy()
        
        # Create canvas for the riddles
        self.canvas = tk.Canvas(self.main_frame, width=window_width, height=window_height, 
                              bg="#FFF8DC", highlightthickness=0)
        self.canvas.pack(expand=True, fill="both")
        
        # Add decorative border
        border_padding = 80  # Doubled from 40
        self.canvas.create_rectangle(border_padding, border_padding, 
                                   window_width-border_padding, window_height-border_padding, 
                                   outline="#8B4513", width=4)  # Doubled from 2
        
        # Add the riddle
        riddle = """Here's a riddle for you, Papa!

I speak without a mouth and hear without ears.
I have no body, but I come alive with wind.
What am I?"""
        
        # Add the text with decorative font
        text_margin = 160  # Doubled from 80
        self.canvas.create_text(
            window_width//2,
            window_height//2 - 200,  # Doubled from 100
            text=riddle,
            font=("Brush Script MT", 48),  # Doubled from 24
            fill="#8B4513",  # Brown text
            justify=tk.CENTER,
            width=window_width - (2 * text_margin)
        )
        
        # Create a frame for the input box and buttons
        input_frame = tk.Frame(self.main_frame, bg="#FFF8DC")
        input_frame.place(x=window_width//2, y=window_height//2 + 200, anchor="center")  # Moved down from +100 to +200
        
        # Add input box with a visible border
        self.answer_entry = tk.Entry(
            input_frame,
            font=("Arial", 28),  # Doubled from 14
            width=25,
            bg="white",
            fg="black",
            relief=tk.SOLID,  # Solid border
            bd=6,            # Doubled from 3
            highlightthickness=4,  # Doubled from 2
            highlightcolor="black"
        )
        self.answer_entry.pack(pady=20)  # Doubled from 10
        
        # Bind the key press event to clear feedback
        self.answer_entry.bind('<Key>', self.clear_feedback)
        
        # Add submit button
        submit_button = tk.Button(
            input_frame,
            text="Submit Answer",
            font=("Arial", 24),  # Doubled from 12
            command=self.check_answer,
            bg="#8B4513",
            fg="white",
            relief=tk.RAISED
        )
        submit_button.pack(pady=10)  # Doubled from 5
        
        # Add a back button
        back_button = tk.Button(
            input_frame,
            text="Retour à la note",
            font=("Arial", 24),  # Doubled from 12
            command=self.show_note_callback,
            bg="#8B4513",
            fg="white",
            relief=tk.RAISED
        )
        back_button.pack(pady=10)  # Doubled from 5
        
        # Create next button but don't show it yet
        self.next_button = tk.Button(
            input_frame,
            text="Suivant",
            font=("Arial", 24),  # Doubled from 12
            command=self.show_next,
            bg="#FFF8DC",
            fg="black",
            relief=tk.RAISED,
            borderwidth=4  # Doubled from 2
        )
        
    def clear_feedback(self, event=None):
        # Clear the feedback text if it exists
        if self.feedback_text:
            self.canvas.delete(self.feedback_text)
            self.feedback_text = None
        
    def check_answer(self):
        answer = self.answer_entry.get().strip().lower()
        if answer == "echo":
            # Show correct answer message
            self.feedback_text = self.canvas.create_text(
                self.window_width//2,
                self.window_height//2 + 300,  # Doubled from 150
                text="Correct! The answer is Echo!",
                font=("Arial", 28, "bold"),  # Doubled from 14
                fill="green"
            )
            # Show the next button
            self.next_button.pack(pady=10)  # Doubled from 5
        else:
            # Show incorrect answer message
            self.feedback_text = self.canvas.create_text(
                self.window_width//2,
                self.window_height//2 + 300,  # Doubled from 150
                text="Try again!",
                font=("Arial", 28, "bold"),  # Doubled from 14
                fill="red"
            )
    
    def show_next(self):
        # Create and show the math problem
        fun_math.FunMath(self.main_frame, self.window_width, self.window_height, self.show_note_callback)

if __name__ == "__main__":
    app = FunRiddles()
    app.run() 