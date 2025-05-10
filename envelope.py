import tkinter as tk
from PIL import Image, ImageTk, ImageFont, ImageDraw
import os

class Envelope:
    def __init__(self):
        self.root = tk.Tk()
        self.root.title("Birthday Envelope")
        
        # Set fixed window size
        window_width = 800
        window_height = 600
        self.root.geometry(f"{window_width}x{window_height}")
        
        # Create main frame
        self.main_frame = tk.Frame(self.root)
        self.main_frame.pack(expand=True, fill="both")
        
        # Create canvas for the envelope image
        self.canvas = tk.Canvas(self.main_frame, width=window_width, height=window_height)
        self.canvas.pack(expand=True, fill="both")
        
        # Load and display the envelope image
        try:
            # Load the image
            image = Image.open("envelope_decorated.png")
            
            # Calculate aspect ratio
            img_width, img_height = image.size
            aspect_ratio = img_width / img_height
            
            # Calculate new dimensions while maintaining aspect ratio
            if window_width / window_height > aspect_ratio:
                new_height = window_height
                new_width = int(new_height * aspect_ratio)
            else:
                new_width = window_width
                new_height = int(new_width / aspect_ratio)
            
            # Resize image
            image = image.resize((new_width, new_height), Image.Resampling.LANCZOS)
            self.photo = ImageTk.PhotoImage(image)
            
            # Center the image on canvas
            x = (window_width - new_width) // 2
            y = (window_height - new_height) // 2
            self.canvas.create_image(x, y, image=self.photo, anchor="nw")
            
            # Add decorative text at the bottom
            text_y = y + new_height - 100  # Position text 100 pixels from bottom of envelope
            self.canvas.create_text(
                window_width//2,  # Center horizontally
                text_y,          # Position near bottom
                text="Joyeux Anniversaire Papa!",
                font=("Brush Script MT", 36, "italic"),  # Script font
                fill="black"     # Black color
            )
            
        except Exception as e:
            # If image loading fails, display a message
            self.canvas.create_text(window_width//2, window_height//2, 
                                  text="Please add an envelope image named 'envelope_decorated.png'", 
                                  font=("Arial", 14), fill="black")
        
    def run(self):
        self.root.mainloop()

if __name__ == "__main__":
    app = Envelope()
    app.run() 