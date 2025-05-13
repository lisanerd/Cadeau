import tkinter as tk
from PIL import Image, ImageTk
import os
from tkinter import font
import random
import math

class Confetti:
    def __init__(self, canvas, x, y):
        self.canvas = canvas
        self.x = x
        self.y = y
        self.size = random.randint(5, 15)
        self.color = random.choice(['#FFD700', '#FF69B4', '#87CEEB', '#98FB98', '#DDA0DD', '#F08080'])
        self.speed = random.uniform(2, 5)
        self.angle = random.uniform(0, 360)
        self.rotation = random.uniform(-5, 5)
        self.rotation_angle = 0
        self.shape = random.choice(['circle', 'square', 'triangle'])
        self.id = self.draw()

    def draw(self):
        if self.shape == 'circle':
            return self.canvas.create_oval(
                self.x - self.size, self.y - self.size,
                self.x + self.size, self.y + self.size,
                fill=self.color, outline=''
            )
        elif self.shape == 'square':
            return self.canvas.create_rectangle(
                self.x - self.size, self.y - self.size,
                self.x + self.size, self.y + self.size,
                fill=self.color, outline=''
            )
        else:  # triangle
            points = [
                self.x, self.y - self.size,
                self.x - self.size, self.y + self.size,
                self.x + self.size, self.y + self.size
            ]
            return self.canvas.create_polygon(points, fill=self.color, outline='')

    def update(self):
        # Update position
        self.x += math.cos(math.radians(self.angle)) * self.speed
        self.y += math.sin(math.radians(self.angle)) * self.speed + 0.5  # Add gravity effect
        
        # Update rotation
        self.rotation_angle += self.rotation
        
        # Move the confetti piece
        if self.shape == 'circle':
            self.canvas.coords(self.id,
                self.x - self.size, self.y - self.size,
                self.x + self.size, self.y + self.size
            )
        elif self.shape == 'square':
            self.canvas.coords(self.id,
                self.x - self.size, self.y - self.size,
                self.x + self.size, self.y + self.size
            )
        else:  # triangle
            points = [
                self.x, self.y - self.size,
                self.x - self.size, self.y + self.size,
                self.x + self.size, self.y + self.size
            ]
            self.canvas.coords(self.id, *points)

        # Check if confetti is out of bounds
        if self.y > self.canvas.winfo_height():
            self.canvas.delete(self.id)
            return False
        return True

class Heart:
    def __init__(self, canvas, x, y):
        self.canvas = canvas
        self.x = x
        self.y = y
        self.size = random.randint(20, 40)
        self.color = random.choice(['#FF69B4', '#FF1493', '#FFB6C1', '#FFC0CB'])
        self.id = self.draw()

    def draw(self):
        # Create heart shape using bezier curves
        size = self.size
        points = [
            self.x, self.y - size//2,  # Top point
            self.x - size, self.y - size,  # Left curve control
            self.x - size, self.y + size//2,  # Left bottom
            self.x, self.y + size,  # Bottom point
            self.x + size, self.y + size//2,  # Right bottom
            self.x + size, self.y - size,  # Right curve control
            self.x, self.y - size//2  # Back to top
        ]
        return self.canvas.create_polygon(points, fill=self.color, outline='', smooth=True)

class Final:
    def __init__(self, main_frame, window_width, window_height):
        self.main_frame = main_frame
        self.window_width = window_width
        self.window_height = window_height
        
        # Clear the main frame
        for widget in self.main_frame.winfo_children():
            widget.destroy()
            
        # Create canvas
        self.canvas = tk.Canvas(
            self.main_frame,
            width=window_width,
            height=window_height,
            bg='#FFE4E1'  # Misty Rose background
        )
        self.canvas.pack(fill='both', expand=True)
        
        # Create confetti
        self.confetti_list = []
        self.create_confetti()
        
        # Create decorative border
        border_padding = 80
        self.canvas.create_rectangle(
            border_padding, border_padding,
            window_width - border_padding,
            window_height - border_padding,
            outline='#FF69B4',
            width=4
        )
        
        # Create title
        title_font = font.Font(family='Helvetica', size=72, weight='bold')
        self.canvas.create_text(
            window_width//2,
            window_height//4,
            text="Félicitations!",
            font=title_font,
            fill='#FF69B4'
        )
        
        # Create love message
        love_font = font.Font(family='Helvetica', size=48, weight='bold')
        self.canvas.create_text(
            window_width//2,
            window_height//2,
            text="Je t'aime papa!",
            font=love_font,
            fill='#FF1493',
            justify='center'
        )
        
        # Create decorative text at the bottom
        self.canvas.create_text(
            window_width//2,
            window_height - 200,
            text="Joyeux Anniversaire Papa!",
            font=font.Font(family='Helvetica', size=72, weight='bold'),
            fill='#FF69B4'
        )

        # Create hearts button
        self.hearts_button = tk.Button(
            self.canvas,
            text="❤️ Hearts ❤️",
            font=font.Font(family='Helvetica', size=24, weight='bold'),
            bg='#FF69B4',
            fg='white',
            relief='raised',
            borderwidth=4,
            command=self.create_hearts
        )
        self.canvas.create_window(
            window_width//2,
            window_height - 100,
            window=self.hearts_button
        )
        
        # Start confetti animation
        self.animate_confetti()

    def create_confetti(self):
        # Create initial confetti
        for _ in range(50):
            x = random.randint(0, self.window_width)
            y = random.randint(-100, 0)
            self.confetti_list.append(Confetti(self.canvas, x, y))
        
        # Create new confetti periodically
        self.canvas.after(200, self.create_confetti)

    def animate_confetti(self):
        # Update confetti positions
        self.confetti_list = [confetti for confetti in self.confetti_list if confetti.update()]
        
        # Continue animation
        self.canvas.after(20, self.animate_confetti)

    def create_hearts(self):
        # Create 3 hearts at random positions
        for _ in range(3):
            x = random.randint(100, self.window_width - 100)
            y = random.randint(100, self.window_height - 100)
            heart = Heart(self.canvas, x, y)
            # Remove heart after 3 seconds
            self.canvas.after(3000, lambda h=heart: self.canvas.delete(h.id)) 