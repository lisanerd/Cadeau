import tkinter as tk
from PIL import Image, ImageTk
import os
import fun_planes

class FunScience:
    def __init__(self, main_frame, window_width, window_height, show_math_callback):
        self.main_frame = main_frame
        self.window_width = window_width
        self.window_height = window_height
        self.show_math_callback = show_math_callback
        self.feedback_text = None
        
        # Clear all widgets from the main frame
        for widget in self.main_frame.winfo_children():
            widget.destroy()
        
        # Create canvas for the science riddle
        self.canvas = tk.Canvas(self.main_frame, width=window_width, height=window_height, 
                              bg="#FFF8DC", highlightthickness=0)
        self.canvas.pack(expand=True, fill="both")
        
        # Add decorative border
        border_padding = 80
        self.canvas.create_rectangle(border_padding, border_padding, 
                                   window_width-border_padding, window_height-border_padding, 
                                   outline="#8B4513", width=4)
        
        # Add the science riddle
        riddle = """Here's a science riddle about flying, Papa!

What invisible force keeps planes in the air?
(Hint: It's the same force that makes a kite fly)"""
        
        # Add the text with decorative font
        text_margin = 160
        self.canvas.create_text(
            window_width//2,
            window_height//2 - 200,
            text=riddle,
            font=("Brush Script MT", 48),
            fill="#8B4513",  # Brown text
            justify=tk.CENTER,
            width=window_width - (2 * text_margin)
        )
        
        # Create a frame for the input box
        input_frame = tk.Frame(self.main_frame, bg="#FFF8DC")
        input_frame.place(x=window_width//2, y=window_height//2 + 50, anchor="center")
        
        # Add input box
        self.answer_entry = tk.Entry(
            input_frame,
            font=("Arial", 28),
            width=20
        )
        self.answer_entry.pack(pady=20)
        
        # Bind key press event to clear feedback
        self.answer_entry.bind('<Key>', self.clear_feedback)
        
        # Create a frame for the buttons
        button_frame = tk.Frame(self.main_frame, bg="#FFF8DC")
        button_frame.place(x=window_width//2, y=window_height//2 + 250, anchor="center")
        
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
        submit_button.pack(pady=10)
        
        # Add a back button
        back_button = tk.Button(
            button_frame,
            text="Retour aux maths",
            font=("Arial", 24),
            command=self.show_math_callback,
            bg="#8B4513",
            fg="white",
            relief=tk.RAISED
        )
        back_button.pack(pady=10)
        
        # Create next button but don't show it yet
        self.next_button = tk.Button(
            button_frame,
            text="Next Question",
            font=("Arial", 24),
            command=self.show_next,
            bg="#FFF8DC",
            fg="black",
            relief=tk.RAISED,
            borderwidth=4
        )
    
    def clear_feedback(self, event=None):
        if self.feedback_text:
            self.canvas.delete(self.feedback_text)
            self.feedback_text = None
    
    def check_answer(self):
        # Clear any existing feedback
        self.clear_feedback()
        
        answer = self.answer_entry.get().strip().lower()
        if answer == "lift":
            # Show correct answer message
            self.feedback_text = self.canvas.create_text(
                self.window_width//2,
                self.window_height//2 + 400,
                text="Correct! Here is your third hint to the password... \"un\"",
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
    
    def show_next(self):
        # Create and show the planes question
        fun_planes.FunPlanes(self.main_frame, self.window_width, self.window_height, 
                           lambda: self.__init__(self.main_frame, self.window_width, self.window_height, self.show_math_callback)) 