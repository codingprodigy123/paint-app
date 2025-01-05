import tkinter as tk
from tkinter import ttk

class PaintApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Paint App")

        # Set the root window style
        self.root.geometry("900x800")
        self.root.config(bg="#f0f0f0")

        # Canvas setup with rounded corners
        self.canvas = tk.Canvas(root, bg="white", width=800, height=600, bd=0, highlightthickness=0, relief="solid")
        self.canvas.pack(padx=20, pady=20)

        # Brush settings
        self.default_brush_color = "black"
        self.default_brush_size = 5
        self.brush_color = self.default_brush_color
        self.brush_size = self.default_brush_size

        # Color options
        self.colors = ["black", "red", "green", "blue", "yellow", "purple", "orange", "brown", "white", "RGB"]
        self.selected_color = tk.StringVar(value=self.default_brush_color)

        # Buttons and dropdown with rounded corners and gradients
        self.button_frame = tk.Frame(root, bg="#f0f0f0")
        self.button_frame.pack(pady=10)

        tk.Label(self.button_frame, text="Brush Color:", bg="#f0f0f0", font=("Arial", 14)).pack(side=tk.LEFT)

        # Custom dropdown style
        self.color_dropdown = tk.OptionMenu(self.button_frame, self.selected_color, *self.colors, command=self.change_color)
        self.color_dropdown.config(width=15, font=("Arial", 12), relief="flat", highlightthickness=0, bd=0)
        self.color_dropdown.pack(side=tk.LEFT, padx=5)

        self.create_pen_size_button("Increase Size", self.increase_size).pack(side=tk.LEFT, padx=5)
        self.create_pen_size_button("Decrease Size", self.decrease_size).pack(side=tk.LEFT, padx=5)
        self.create_button("Clear", self.clear_canvas).pack(side=tk.LEFT, padx=5)
        self.create_button("Reset", self.reset_settings).pack(side=tk.LEFT, padx=5)

        # Bind events
        self.canvas.bind("<B1-Motion>", self.paint)
        # self.add_tiny_orange_button()

    def create_button(self, text, command):
        """Helper function to create a rounded button with a gradient."""
        button = tk.Button(self.button_frame, text=text, command=command, font=("Arial", 12, "bold"), relief="flat", bd=0, height=2)
        button.config(bg="#4CAF50", fg="white", activebackground="#45a049", activeforeground="white", width=15)
        button.config(borderwidth=2, highlightbackground="#4CAF50", highlightthickness=2, padx=5, pady=5)
        return button

    def create_pen_size_button(self, text, command):
        """Helper function to create a dark blue pen size button."""
        button = tk.Button(self.button_frame, text=text, command=command, font=("Arial", 12, "bold"), relief="flat", bd=0, height=2)
        button.config(bg="#003366", fg="white", activebackground="#00509E", activeforeground="white", width=15)
        button.config(borderwidth=2, highlightbackground="#003366", highlightthickness=2, padx=5, pady=5)
        return button

    def change_color(self, color):
        if color == "RGB":
            self.open_rgb_window()  # Open a new window with RGB sliders
        else:
            self.brush_color = color


    def open_rgb_window(self):
        """Open a new window with RGB sliders."""
        rgb_window = tk.Toplevel(self.root)
        rgb_window.title("Adjust RGB Color")
        rgb_window.geometry("600x500")

        # Set up RGB sliders in the new window
        tk.Label(rgb_window, text="R:", font=("Arial", 12)).pack(pady=5)
        self.r_slider = tk.Scale(rgb_window, from_=0, to=255, orient=tk.HORIZONTAL, command=self.update_rgb_color, sliderlength=30, length=200)
        self.r_slider.pack(pady=5)

        tk.Label(rgb_window, text="G:", font=("Arial", 12)).pack(pady=5)
        self.g_slider = tk.Scale(rgb_window, from_=0, to=255, orient=tk.HORIZONTAL, command=self.update_rgb_color, sliderlength=30, length=200)
        self.g_slider.pack(pady=5)

        tk.Label(rgb_window, text="B:", font=("Arial", 12)).pack(pady=5)
        self.b_slider = tk.Scale(rgb_window, from_=0, to=255, orient=tk.HORIZONTAL, command=self.update_rgb_color, sliderlength=30, length=200)
        self.b_slider.pack(pady=5)

        # Predefined RGB buttons (added more colors)
        self.create_rgb_button(rgb_window, "Red", 255, 0, 0).pack(side=tk.LEFT, padx=5, pady=10)
        self.create_rgb_button(rgb_window, "Green", 0, 255, 0).pack(side=tk.LEFT, padx=5, pady=10)
        self.create_rgb_button(rgb_window, "Blue", 0, 0, 255).pack(side=tk.LEFT, padx=5, pady=10)
        self.create_rgb_button(rgb_window, "White", 255, 255, 255).pack(side=tk.LEFT, padx=5, pady=10)
        self.create_rgb_button(rgb_window, "Yellow", 255, 255, 0).pack(side=tk.LEFT, padx=5, pady=10)
        self.create_rgb_button(rgb_window, "Purple", 128, 0, 128).pack(side=tk.LEFT, padx=5, pady=10)
        self.create_rgb_button(rgb_window, "Orange", 255, 165, 0).pack(side=tk.LEFT, padx=5, pady=10)
        self.create_rgb_button(rgb_window, "Brown", 139, 69, 19).pack(side=tk.LEFT, padx=5, pady=10)

        tk.Button(rgb_window, text="Close", command=rgb_window.destroy, font=("Arial", 12), bg="#4CAF50", fg="white", activebackground="#45a049", activeforeground="white").pack(pady=20)

#    def add_tiny_orange_button(self):
        """Add a tiny orange button in the top-right corner."""
#        tiny_button = tk.Button(self.root, text="", bg="orange", command=self.on_tiny_button_click, width=5, height=1, relief="flat", bd=0)
#        tiny_button.place(x=810, y=20)  # Place near the top-right corner

 #   def on_tiny_button_click(self):
        """Action for tiny orange button click."""
#        pass
    def create_rgb_button(self, window, color_name, r, g, b):
        """Create a button for predefined RGB colors."""
        return tk.Button(window, text=color_name, font=("Arial", 12), bg=self.rgb_to_color_name(r, g, b), fg="white", command=lambda: self.set_rgb_color(r, g, b))

    def rgb_to_color_name(self, r, g, b):
        """Return the RGB color string (used directly for button background)."""
        return f"#{r:02x}{g:02x}{b:02x}"

    def set_rgb_color(self, r, g, b):
        """Set the RGB color from a preset button."""
        self.r_slider.set(r)
        self.g_slider.set(g)
        self.b_slider.set(b)
        self.update_rgb_color(None)  # Update the brush color immediately

    def update_rgb_color(self, _):
        """Update the brush color based on RGB slider values if 'RGB Custom Color' is selected."""
        r = self.r_slider.get()
        g = self.g_slider.get()
        b = self.b_slider.get()
        self.brush_color = f"#{r:02x}{g:02x}{b:02x}"

    def increase_size(self):
        self.brush_size += 2

    def decrease_size(self):
        if self.brush_size > 2:
            self.brush_size -= 2

    def clear_canvas(self):
        self.canvas.delete("all")

    def reset_settings(self):
        self.brush_color = self.default_brush_color
        self.brush_size = self.default_brush_size
        self.selected_color.set(self.default_brush_color)
        self.r_slider.set(0)
        self.g_slider.set(0)
        self.b_slider.set(0)

    def paint(self, event):
        x1, y1 = (event.x - self.brush_size), (event.y - self.brush_size)
        x2, y2 = (event.x + self.brush_size), (event.y + self.brush_size)
        self.canvas.create_oval(x1, y1, x2, y2, fill=self.brush_color, outline=self.brush_color)

# Run the app
if __name__ == "__main__":
    root = tk.Tk()
    app = PaintApp(root)
    root.mainloop()
