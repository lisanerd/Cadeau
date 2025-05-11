import tkinter as tk
from PIL import Image, ImageTk
import os
import fun_riddles
import note
import instructions

class Envelope:
    def __init__(self, root):
        self.root = root
        self.root.title("Joyeux Anniversaire Papa!")
        
        # Set window size
        self.window_width = 1600
        self.window_height = 1200
        self.root.geometry(f"{self.window_width}x{self.window_height}")
        
        # Create main frame
        self.main_frame = tk.Frame(self.root)
        self.main_frame.pack(expand=True, fill="both")
        
        # Create canvas for the envelope image
        self.canvas = tk.Canvas(self.main_frame, width=self.window_width, height=self.window_height, 
                              bg="#FFF8DC", highlightthickness=0)
        self.canvas.pack(expand=True, fill="both")
        
        # Load and display the envelope image
        try:
            image_path = "envelope_decorated.png"
            if not os.path.exists(image_path):
                raise FileNotFoundError("Envelope image not found")
            
            # Load the image
            image = Image.open(image_path)
            
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
            stamp_radius = 60
            
            # Add "click me" text on top of the stamp
            self.canvas.create_text(
                stamp_x,
                stamp_y,
                text="click me",
                font=("Arial", 28, "bold"),
                fill="white"
            )
            
            # Add decorative text at the bottom
            text_y = y + new_height - 200
            self.canvas.create_text(
                self.window_width//2,  # Center horizontally
                text_y,          # Position near bottom
                text="Joyeux Anniversaire Papa!",
                font=("Brush Script MT", 72),
                fill="#8B4513"  # Brown text
            )
            
            # Store the stamp position and radius for click detection
            self.stamp_x = stamp_x
            self.stamp_y = stamp_y
            self.stamp_radius = stamp_radius
            
            # Bind click event to the canvas
            self.canvas.bind("<Button-1>", self.on_canvas_click)
            
        except Exception as e:
            # If there's an error loading the image, show an error message
            error_label = tk.Label(self.main_frame, 
                                 text=f"Error loading image: {str(e)}", 
                                 font=("Arial", 24),
                                 fg="red")
            error_label.pack(expand=True)
    
    def on_canvas_click(self, event):
        # Calculate distance from click to stamp center
        distance = ((event.x - self.stamp_x) ** 2 + (event.y - self.stamp_y) ** 2) ** 0.5
        
        # If click is within the stamp radius, show the note
        if distance <= self.stamp_radius:
            self.show_note()
    
    def show_note(self):
        # Create and show the note
        note.Note(self.main_frame, self.window_width, self.window_height, self.show_envelope, self.show_instructions)
    
    def show_instructions(self):
        # Create and show the instructions screen
        instructions.Instructions(self.main_frame, self.window_width, self.window_height, 
                                self.show_note, self.show_riddles)
    
    def show_envelope(self):
        # Clear all widgets from the main frame
        for widget in self.main_frame.winfo_children():
            widget.destroy()
        
        # Create canvas for the envelope image
        self.canvas = tk.Canvas(self.main_frame, width=self.window_width, height=self.window_height, 
                              bg="#FFF8DC", highlightthickness=0)
        self.canvas.pack(expand=True, fill="both")
        
        # Load and display the envelope image
        try:
            image_path = "envelope_decorated.png"
            if not os.path.exists(image_path):
                raise FileNotFoundError("Envelope image not found")
            
            # Load the image
            image = Image.open(image_path)
            
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
            stamp_radius = 60
            
            # Add "click me" text on top of the stamp
            self.canvas.create_text(
                stamp_x,
                stamp_y,
                text="click me",
                font=("Arial", 28, "bold"),
                fill="white"
            )
            
            # Add decorative text at the bottom
            text_y = y + new_height - 200
            self.canvas.create_text(
                self.window_width//2,  # Center horizontally
                text_y,          # Position near bottom
                text="Joyeux Anniversaire Papa!",
                font=("Brush Script MT", 72),
                fill="#8B4513"  # Brown text
            )
            
            # Store the stamp position and radius for click detection
            self.stamp_x = stamp_x
            self.stamp_y = stamp_y
            self.stamp_radius = stamp_radius
            
            # Bind click event to the canvas
            self.canvas.bind("<Button-1>", self.on_canvas_click)
            
        except Exception as e:
            # If there's an error loading the image, show an error message
            error_label = tk.Label(self.main_frame, 
                                 text=f"Error loading image: {str(e)}", 
                                 font=("Arial", 24),
                                 fg="red")
            error_label.pack(expand=True)
    
    def show_riddles(self):
        # Create and show the riddles
        fun_riddles.FunRiddles(self.main_frame, self.window_width, self.window_height, self.show_instructions)

if __name__ == "__main__":
    root = tk.Tk()
    app = Envelope(root)
    root.mainloop() 