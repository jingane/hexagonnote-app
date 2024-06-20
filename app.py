import streamlit as st

class HexagonNote:
    def __init__(self, x, y, size, text=""):
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
        st.plotly_chart({
            'data': [{
                'type': 'scatter',
                'x': [self.center_x, self.center_x + size * 0.866, self.center_x + size * 0.866, self.center_x, self.center_x - size * 0.866, self.center_x - size * 0.866, self.center_x],
                'y': [self.center_y - size, self.center_y - size * 0.5, self.center_y + size * 0.5, self.center_y + size, self.center_y + size * 0.5, self.center_y - size * 0.5, self.center_y - size],
                'fill': 'toself',
                'line': {'color': 'black'},
                'hoverinfo': 'text',
                'text': self.text,
                'mode': 'lines+text'
            }],
            'layout': {}
        })

if __name__ == "__main__":
    st.title("Hexa Note App")
    st.markdown("### Click on the hexagons to enter notes.")
    
    size = 50
    spacing_x = size * 2  # Adjusted spacing for x to avoid overlap
    spacing_y = size * 1.732  # sqrt(3) * size
    for i in range(10):  # Increase range for more hexagons
        for j in range(10):
            x = spacing_x * i
            y = spacing_y * j
            if j % 2 == 1:  # Offset every other row
                x += spacing_x / 2
            text_input = st.text_input(f'Note for hexagon at ({x}, {y})')
            HexagonNote(x, y, size, text_input)
