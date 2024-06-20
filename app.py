import tkinter as tk
from tkinter import simpledialog

class HexagonNote:
    def __init__(self, master, x, y, size, text=""):
        self.master = master
        self.size = size
        self.text = text
        self.center_x = x
        self.center_y = y
        self.create_hexagon()

    def create_hexagon(self):
        size = self.size
        points = [
            self.center_x, self.center_y - size,
            self.center_x + size * 0.866, self.center_y - size * 0.5,
            self.center_x + size * 0.866, self.center_y + size * 0.5,
            self.center_x, self.center_y + size,
            self.center_x - size * 0.866, self.center_y + size * 0.5,
            self.center_x - size * 0.866, self.center_y - size * 0.5
        ]
        self.polygon = self.master.create_polygon(points, outline="black", fill="lightblue", width=2)
        self.text_id = self.master.create_text(self.center_x, self.center_y, text=self.text)
        self.master.tag_bind(self.polygon, "<Button-1>", self.on_click)
        self.master.tag_bind(self.text_id, "<Button-1>", self.on_click)

    def on_click(self, event):
        text = simpledialog.askstring("Input", "Enter note:")
        if text is not None:
            self.text = text
            self.master.itemconfig(self.text_id, text=self.text)


class HexaNoteApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Hexa Note")
        self.canvas = tk.Canvas(root, bg="white")
        self.canvas.pack(fill=tk.BOTH, expand=True)
        self.add_hexagon_notes()

    def add_hexagon_notes(self):
        size = 50
        spacing_x = size * 2  # Adjusted spacing for x to avoid overlap
        spacing_y = size * 1.732  # sqrt(3) * size
        for i in range(10):  # Increase range for more hexagons
            for j in range(10):
                x = spacing_x * i
                y = spacing_y * j
                if j % 2 == 1:  # Offset every other row
                    x += spacing_x / 2
                HexagonNote(self.canvas, x, y, size)

if __name__ == "__main__":
    root = tk.Tk()
    app = HexaNoteApp(root)
    root.mainloop()
