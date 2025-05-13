import tkinter as tk
from PIL import Image, ImageTk
import os

class Instructions:
    def __init__(self, main_frame, window_width, window_height, show_note_callback, show_riddles_callback):
        self.main_frame = main_frame
        self.window_width = window_width
        self.window_height = window_height
        self.show_note_callback = show_note_callback
        self.show_riddles_callback = show_riddles_callback
        
        # Clear all widgets from the main frame
        for widget in self.main_frame.winfo_children():
            widget.destroy()
        
        # Create canvas for the instructions
        self.canvas = tk.Canvas(self.main_frame, width=window_width, height=window_height, 
                              bg="#FFF8DC", highlightthickness=0)
        self.canvas.pack(expand=True, fill="both")
        
        # Add decorative border
        border_padding = 80
        self.canvas.create_rectangle(border_padding, border_padding, 
                                   window_width-border_padding, window_height-border_padding, 
                                   outline="#8B4513", width=4)
        
        # Add the instructions text
        instructions = """Maintenant, tu vas avoir des enigmes a resoudre pour trouver le password secret du programe...bonne chance!"""
        
        # Add the text with decorative font
        text_margin = 160
        self.canvas.create_text(
            window_width//2,
            window_height//2,
            text=instructions,
            font=("Brush Script MT", 48),
            fill="#8B4513",  # Brown text
            justify=tk.CENTER,
            width=window_width - (2 * text_margin)
        )
        
        # Create a frame for the buttons
        button_frame = tk.Frame(self.main_frame, bg="#FFF8DC")
        button_frame.place(x=window_width//2, y=window_height//2 + 200, anchor="center")
        
        # Add back button
        back_button = tk.Button(
            button_frame,
            text="Retour à la note",
            font=("Arial", 24),
            command=self.show_note_callback,
            bg="#8B4513",
            fg="white",
            relief=tk.RAISED
        )
        back_button.pack(side=tk.LEFT, padx=20)
        
        # Add next button
        next_button = tk.Button(
            button_frame,
            text="Commencer",
            font=("Arial", 24),
            command=self.show_riddles_callback,
            bg="#8B4513",
            fg="white",
            relief=tk.RAISED
        )
        next_button.pack(side=tk.LEFT, padx=20) 