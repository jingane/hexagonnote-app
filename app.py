import streamlit as st
import plotly.graph_objects as go
import numpy as np

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
                text_input = st.text_input(f'Note for hexagon at ({x}, {y})')
                hexagon = self.create_hexagon(x, y, size, text_input)
                self.hexagons.append(hexagon)

    def create_hexagon(self, x, y, size, text):
        angles = np.linspace(0, 2 * np.pi, 7)
        hexagon_x = x + size * np.cos(angles)
        hexagon_y = y + size * np.sin(angles)

        # Create polygon path
        path = f'M {hexagon_x[0]}, {hexagon_y[0]} '
        for i in range(1, len(hexagon_x)):
            path += f'L {hexagon_x[i]}, {hexagon_y[i]} '
        path += f'Z'

        # Add hexagon trace
        self.fig.add_trace(go.Scatter(
            x=hexagon_x,
            y=hexagon_y,
            mode='lines',
            fill='toself',
            line=dict(color='black'),
            hoverinfo='text',
            text=text,
            textposition='top center',
            name='',
            showlegend=False
        ))

    def display(self):
        st.plotly_chart(self.fig, use_container_width=True)

if __name__ == "__main__":
    st.title("Hexa Note")
    app = HexaNoteApp()
    app.display()
