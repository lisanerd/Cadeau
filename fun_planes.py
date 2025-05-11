import tkinter as tk
from PIL import Image, ImageTk
import os

class FunPlanes:
    def __init__(self, main_frame, window_width, window_height, show_science_callback):
        self.main_frame = main_frame
        self.window_width = window_width
        self.window_height = window_height
        self.show_science_callback = show_science_callback
        self.feedback_text = None
        
        # Clear all widgets from the main frame
        for widget in self.main_frame.winfo_children():
            widget.destroy()
        
        # Create canvas for the aviation question
        self.canvas = tk.Canvas(self.main_frame, width=window_width, height=window_height, 
                              bg="#FFF8DC", highlightthickness=0)
        self.canvas.pack(expand=True, fill="both")
        
        # Add decorative border
        border_padding = 80
        self.canvas.create_rectangle(border_padding, border_padding, 
                                   window_width-border_padding, window_height-border_padding, 
                                   outline="#8B4513", width=4)
        
        # Add the aviation question
        question = """What is the primary purpose of the flaps on an aircraft?

(Hint: Think about what helps planes take off and land safely)"""
        
        # Add the text with decorative font
        text_margin = 160
        self.canvas.create_text(
            window_width//2,
            window_height//2 - 400,  # Moved back to -400 since we removed text
            text=question,
            font=("Brush Script MT", 48),  # Restored to original size
            fill="#8B4513",  # Brown text
            justify=tk.CENTER,
            width=window_width - (2 * text_margin)  # Restored to original margin
        )
        
        # Create a frame for the radio buttons
        radio_frame = tk.Frame(self.main_frame, bg="#FFF8DC")
        radio_frame.place(x=window_width//2, y=window_height//2 - 50, anchor="center")  # Moved up from 0 to make room for buttons
        
        # Create a variable to hold the selected answer
        self.selected_answer = tk.StringVar()
        
        # Create radio buttons for each option
        options = [
            "A) To increase the aircraft's speed",
            "B) To provide additional lift during takeoff and landing",
            "C) To help the aircraft turn",
            "D) To reduce engine noise"
        ]
        for i, option in enumerate(options):
            rb = tk.Radiobutton(
                radio_frame,
                text=option,
                variable=self.selected_answer,
                value=chr(65 + i),  # A, B, C, D
                font=("Arial", 28),
                bg="#FFF8DC",
                fg="#8B4513",
                selectcolor="#FFF8DC",
                activebackground="#FFF8DC",
                activeforeground="#8B4513",
                justify=tk.LEFT,
                wraplength=window_width - (4 * text_margin)  # Allow text to wrap
            )
            rb.pack(pady=15)  # Increased padding between options
        
        # Create a frame for the buttons
        button_frame = tk.Frame(self.main_frame, bg="#FFF8DC")
        button_frame.place(x=window_width//2, y=window_height//2 + 250, anchor="center")  # Moved down from +300 to prevent overlap
        
        # Add submit button
        submit_button = tk.Button(
            button_frame,
            text="Submit Answer",
            font=("Arial", 24),
            command=self.check_answer,
            bg="#8B4513",
            fg="white",
            relief=tk.RAISED
        )
        submit_button.pack(pady=10)  # Changed from side=tk.LEFT to pady
        
        # Add a back button
        back_button = tk.Button(
            button_frame,
            text="Retour à la science",
            font=("Arial", 24),
            command=self.show_science_callback,
            bg="#8B4513",
            fg="white",
            relief=tk.RAISED
        )
        back_button.pack(pady=10)  # Changed from side=tk.LEFT to pady
        
        # Create next button but don't show it yet
        self.next_button = tk.Button(
            button_frame,
            text="Félicitations!",
            font=("Arial", 24),
            command=self.show_congratulations,
            bg="#FFF8DC",
            fg="black",
            relief=tk.RAISED,
            borderwidth=4
        )
    
    def check_answer(self):
        answer = self.selected_answer.get()
        if answer == "B":
            # Show correct answer message
            self.feedback_text = self.canvas.create_text(
                self.window_width//2,
                self.window_height//2 + 400,
                text="Correct!",
                font=("Arial", 28, "bold"),
                fill="green"
            )
            # Show the next button
            self.next_button.pack(pady=10)
        else:
            # Show incorrect answer message
            self.feedback_text = self.canvas.create_text(
                self.window_width//2,
                self.window_height//2 + 400,
                text="Try again!",
                font=("Arial", 28, "bold"),
                fill="red"
            )
    
    def show_congratulations(self):
        # Clear all widgets from the main frame
        for widget in self.main_frame.winfo_children():
            widget.destroy()
        
        # Create canvas for the congratulations message
        self.canvas = tk.Canvas(self.main_frame, width=self.window_width, height=self.window_height, 
                              bg="#FFF8DC", highlightthickness=0)
        self.canvas.pack(expand=True, fill="both")
        
        # Add decorative border
        border_padding = 80
        self.canvas.create_rectangle(border_padding, border_padding, 
                                   self.window_width-border_padding, self.window_height-border_padding, 
                                   outline="#8B4513", width=4)
        
        # Add the congratulations message
        message = """Félicitations Papa!

Tu as résolu toutes les énigmes!
Le password secret est: PAPA2024

Je t'aime beaucoup!"""
        
        # Add the text with decorative font
        text_margin = 160
        self.canvas.create_text(
            self.window_width//2,
            self.window_height//2,
            text=message,
            font=("Brush Script MT", 48),
            fill="#8B4513",
            justify=tk.CENTER,
            width=self.window_width - (2 * text_margin)
        ) 