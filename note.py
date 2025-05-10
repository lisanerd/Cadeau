import tkinter as tk
from PIL import Image, ImageTk
import os

class Note:
    def __init__(self):
        self.root = tk.Tk()
        self.root.title("Birthday Note")
        
        # Set fixed window size
        window_width = 600
        window_height = 400
        self.root.geometry(f"{window_width}x{window_height}")
        
        # Create main frame with a light background
        self.main_frame = tk.Frame(self.root, bg="#FFF8DC")  # Cream color background
        self.main_frame.pack(expand=True, fill="both")
        
        # Create canvas for the note
        self.canvas = tk.Canvas(self.main_frame, width=window_width, height=window_height, 
                              bg="#FFF8DC", highlightthickness=0)
        self.canvas.pack(expand=True, fill="both")
        
        # Add decorative border with more padding
        border_padding = 40
        self.canvas.create_rectangle(border_padding, border_padding, 
                                   window_width-border_padding, window_height-border_padding, 
                                   outline="#8B4513", width=2)  # Brown border
        
        # Add the message
        message = """Joyeux Anniversaire Papounet!

J'espere que tu passes une bonne journee 
d'anniversaire, et que ce petit texte 
vibe-code te fait plaisir ♥

Je t'aime a la follie papa, 
joyeux anniversaire!!!!"""
        
        # Add the text with decorative font and proper margins
        text_margin = 80  # Increased margin from edges
        self.canvas.create_text(
            window_width//2,
            window_height//2,
            text=message,
            font=("Brush Script MT", 24),
            fill="#8B4513",  # Brown text
            justify=tk.CENTER,
            width=window_width - (2 * text_margin)  # Ensure text stays within margins
        )
        
        # Add a close button
        close_button = tk.Button(
            self.main_frame,
            text="Fermer",
            font=("Arial", 12),
            command=self.root.destroy,
            bg="#8B4513",
            fg="white",
            relief=tk.RAISED
        )
        close_button.pack(pady=10)
        
    def run(self):
        self.root.mainloop()

if __name__ == "__main__":
    app = Note()
    app.run() 