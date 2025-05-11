import tkinter as tk
from PIL import Image, ImageTk
import os
import fun_riddles

class Note:
    def __init__(self, main_frame, window_width, window_height, show_envelope_callback, show_instructions_callback):
        self.main_frame = main_frame
        self.window_width = window_width
        self.window_height = window_height
        self.show_envelope_callback = show_envelope_callback
        self.show_instructions_callback = show_instructions_callback
        
        # Clear all widgets from the main frame
        for widget in self.main_frame.winfo_children():
            widget.destroy()
        
        # Create canvas for the note
        self.canvas = tk.Canvas(self.main_frame, width=window_width, height=window_height, 
                              bg="#FFF8DC", highlightthickness=0)
        self.canvas.pack(expand=True, fill="both")
        
        # Add decorative border
        border_padding = 80
        self.canvas.create_rectangle(border_padding, border_padding, 
                                   window_width-border_padding, window_height-border_padding, 
                                   outline="#8B4513", width=4)
        
        # Add the message
        message = """Joyeux Anniversaire Papounet!

J'espere que tu passes une bonne journee 
d'anniversaire, et que ce petit texte 
vibe-code te fait plaisir ♥

Je t'aime a la follie papa, 
joyeux anniversaire!!!!"""
        
        # Add the text with decorative font and proper margins
        text_margin = 160
        self.canvas.create_text(
            window_width//2,
            window_height//2 - 100,
            text=message,
            font=("Brush Script MT", 48),
            fill="#8B4513",
            justify=tk.CENTER,
            width=window_width - (2 * text_margin)
        )
        
        # Add a back button in the bottom left
        back_button = tk.Button(
            self.main_frame,
            text="Retour à l'enveloppe",
            font=("Arial", 24),
            command=self.show_envelope_callback,
            bg="#FFF8DC",
            fg="#8B4513",
            relief=tk.RAISED,
            borderwidth=4
        )
        back_button.place(x=border_padding + 20, y=window_height - 120)
        
        # Add a next button in the bottom right
        next_button = tk.Button(
            self.main_frame,
            text="Suivant",
            font=("Arial", 24),
            command=self.show_instructions_callback,
            bg="#FFF8DC",
            fg="black",
            relief=tk.RAISED,
            borderwidth=4
        )
        next_button.place(x=window_width - border_padding - 200, y=window_height - 120)
    
    def show_riddles(self):
        # Create and show the riddles view
        fun_riddles.FunRiddles(self.main_frame, self.window_width, self.window_height, self.show_instructions_callback)

if __name__ == "__main__":
    app = Note()
    app.run() 