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
        
        # Add decorative border
        self.canvas.create_rectangle(20, 20, window_width-20, window_height-20, 
                                   outline="#8B4513", width=2)  # Brown border
        
        # Add the message
        message = """Cher Papa,

Joyeux Anniversaire! 
Je te souhaite une journée 
remplie de bonheur et d'amour.

Avec tout mon amour,
[Votre nom]"""
        
        # Add the text with decorative font
        self.canvas.create_text(
            window_width//2,
            window_height//2,
            text=message,
            font=("Brush Script MT", 24),
            fill="#8B4513",  # Brown text
            justify=tk.CENTER
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