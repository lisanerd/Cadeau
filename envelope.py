import tkinter as tk
from PIL import Image, ImageTk
import os
import fun_riddles

class Envelope:
    def __init__(self):
        self.root = tk.Tk()
        self.root.title("Birthday Envelope")
        
        # Set fixed window size (doubled from original)
        window_width = 1600  # Doubled from 800
        window_height = 1200  # Doubled from 600
        self.root.geometry(f"{window_width}x{window_height}")
        
        # Create main frame
        self.main_frame = tk.Frame(self.root)
        self.main_frame.pack(expand=True, fill="both")
        
        # Create canvas for the envelope image
        self.canvas = tk.Canvas(self.main_frame, width=window_width, height=window_height)
        self.canvas.pack(expand=True, fill="both")
        
        # Store window dimensions for later use
        self.window_width = window_width
        self.window_height = window_height
        
        # Show the envelope initially
        self.show_envelope()
        
    def show_envelope(self):
        # Clear all widgets from the main frame
        for widget in self.main_frame.winfo_children():
            widget.destroy()
        
        # Recreate the canvas
        self.canvas = tk.Canvas(self.main_frame, width=self.window_width, height=self.window_height)
        self.canvas.pack(expand=True, fill="both")
        
        # Clear the canvas
        self.canvas.delete("all")
        
        try:
            # Load the image
            image = Image.open("envelope_decorated.png")
            
            # Calculate aspect ratio
            img_width, img_height = image.size
            aspect_ratio = img_width / img_height
            
            # Calculate new dimensions while maintaining aspect ratio
            if self.window_width / self.window_height > aspect_ratio:
                new_height = self.window_height
                new_width = int(new_height * aspect_ratio)
            else:
                new_width = self.window_width
                new_height = int(new_width / aspect_ratio)
            
            # Resize image
            image = image.resize((new_width, new_height), Image.Resampling.LANCZOS)
            self.photo = ImageTk.PhotoImage(image)
            
            # Center the image on canvas
            x = (self.window_width - new_width) // 2
            y = (self.window_height - new_height) // 2
            self.canvas.create_image(x, y, image=self.photo, anchor="nw")
            
            # Calculate stamp area (approximately in the center of the envelope)
            stamp_x = x + (new_width // 2)
            stamp_y = y + (new_height // 2)
            stamp_radius = 60  # Doubled from 30
            
            # Create an invisible clickable area for the stamp
            self.canvas.create_oval(
                stamp_x - stamp_radius, stamp_y - stamp_radius,
                stamp_x + stamp_radius, stamp_y + stamp_radius,
                outline="", fill="", tags="stamp"
            )
            
            # Add "click me" text on top of the stamp
            self.canvas.create_text(
                stamp_x,
                stamp_y,
                text="click me",
                font=("Arial", 28, "bold"),  # Doubled from 14
                fill="white",
                tags="stamp"
            )
            
            # Bind click event to the stamp area
            self.canvas.tag_bind("stamp", "<Button-1>", self.show_note)
            
            # Add decorative text at the bottom
            text_y = y + new_height - 200  # Doubled from 100
            self.canvas.create_text(
                self.window_width//2,  # Center horizontally
                text_y,          # Position near bottom
                text="Joyeux Anniversaire Papa!",
                font=("Brush Script MT", 72, "italic"),  # Doubled from 36
                fill="black"     # Black color
            )
            
        except Exception as e:
            # If image loading fails, display a message
            self.canvas.create_text(self.window_width//2, self.window_height//2, 
                                  text="Please add an envelope image named 'envelope_decorated.png'", 
                                  font=("Arial", 28), fill="black")  # Doubled from 14
    
    def show_note(self, event=None):
        # Clear all widgets from the main frame
        for widget in self.main_frame.winfo_children():
            widget.destroy()
        
        # Recreate the canvas
        self.canvas = tk.Canvas(self.main_frame, width=self.window_width, height=self.window_height)
        self.canvas.pack(expand=True, fill="both")
        
        # Clear the canvas
        self.canvas.delete("all")
        
        # Change background color to cream
        self.canvas.configure(bg="#FFF8DC")
        
        # Add decorative border with padding
        border_padding = 80  # Doubled from 40
        self.canvas.create_rectangle(border_padding, border_padding, 
                                   self.window_width-border_padding, self.window_height-border_padding, 
                                   outline="#8B4513", width=4)  # Doubled from 2
        
        # Add the message
        message = """Joyeux Anniversaire Papounet!

J'espere que tu passes une bonne journee 
d'anniversaire, et que ce petit texte 
vibe-code te fait plaisir ♥

Je t'aime a la follie papa, 
joyeux anniversaire!!!!"""
        
        # Add the text with decorative font and proper margins
        text_margin = 160  # Doubled from 80
        self.canvas.create_text(
            self.window_width//2,
            self.window_height//2 - 100,  # Move text up a bit to make room for buttons
            text=message,
            font=("Brush Script MT", 48),  # Doubled from 24
            fill="#8B4513",
            justify=tk.CENTER,
            width=self.window_width - (2 * text_margin)
        )
        
        # Add a back button in the bottom left
        back_button = tk.Button(
            self.main_frame,
            text="Retour à l'enveloppe",
            font=("Arial", 24),  # Doubled from 12
            command=self.show_envelope,
            bg="#FFF8DC",
            fg="#8B4513",
            relief=tk.RAISED,
            borderwidth=4  # Doubled from 2
        )
        back_button.place(x=border_padding + 20, y=self.window_height - 120)  # Doubled from 60
        
        # Add a next button in the bottom right
        next_button = tk.Button(
            self.main_frame,
            text="Suivant",
            font=("Arial", 24),  # Doubled from 12
            command=self.show_riddles,
            bg="#FFF8DC",
            fg="black",
            relief=tk.RAISED,
            borderwidth=4  # Doubled from 2
        )
        next_button.place(x=self.window_width - border_padding - 200, y=self.window_height - 120)  # Doubled from 60
    
    def show_riddles(self):
        # Create and show the riddles view
        fun_riddles.FunRiddles(self.main_frame, self.window_width, self.window_height, self.show_note)
        
    def run(self):
        self.root.mainloop()

if __name__ == "__main__":
    app = Envelope()
    app.run() 