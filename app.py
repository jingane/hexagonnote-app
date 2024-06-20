import streamlit as st
import plotly.graph_objects as go
import numpy as np

class HexagonNote:
    def __init__(self, fig, x, y, size, text=""):
        self.fig = fig
        self.size = size
        self.text = text
        self.center_x = x
        self.center_y = y
        self.create_hexagon()

    def create_hexagon(self):
        size = self.size
        angles = np.linspace(0, 2 * np.pi, 7)
        hexagon_x = self.center_x + size * np.cos(angles)
        hexagon_y = self.center_y + size * np.sin(angles)

        self.fig.add_trace(go.Scatter(
            x=hexagon_x,
            y=hexagon_y,
            mode='lines',
            fill='toself',
            line=dict(color='black'),
            text=self.text,
            hoverinfo='text'
        ))

    def update_text(self, text):
        self.text = text
        self.fig.update_traces(selector=dict(text=self.text), hoverinfo="text")

class HexaNoteApp:
    def __init__(self):
        self.fig = go.Figure()
        self.hexagons = []
        self.add_hexagon_notes()

    def add_hexagon_notes(self):
        size = 50
        spacing_x = size * 1.5  # Adjusted spacing for x to avoid overlap
        spacing_y = size * 1.732  # sqrt(3) * size
        for i in range(10):  # Increase range for more hexagons
            for j in range(10):
                x = spacing_x * i
                y = spacing_y * j
                if j % 2 == 1:  # Offset every other row
                    x += spacing_x / 2
                hex_note = HexagonNote(self.fig, x, y, size)
                self.hexagons.append(hex_note)

    def display(self):
        st.plotly_chart(self.fig, use_container_width=True)

        for hex_note in self.hexagons:
            new_text = st.text_input(f'Note for hexagon at ({hex_note.center_x}, {hex_note.center_y})', hex_note.text)
            if new_text != hex_note.text:
                hex_note.update_text(new_text)

if __name__ == "__main__":
    st.title("Hexa Note")
    app = HexaNoteApp()
    app.display()
