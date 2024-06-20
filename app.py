import streamlit as st
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.patches import Polygon

def draw_hexagon(size=1):
    fig, ax = plt.subplots()
    points = [
        (0, 1), (np.sqrt(3)/2, 0.5), (np.sqrt(3)/2, -0.5),
        (0, -1), (-np.sqrt(3)/2, -0.5), (-np.sqrt(3)/2, 0.5)
    ]
    polygon = Polygon(points, closed=True, edgecolor='black', linewidth=2, facecolor='lightblue')
    ax.add_patch(polygon)
    ax.set_aspect('equal', 'box')
    ax.set_xlim(-size, size)
    ax.set_ylim(-size, size)
    ax.axis('off')  # Disable axis
    return fig

def main():
    st.title('Hexa Memo')
    st.write('Click the button to draw a hexagon!')

    size = st.slider('Size of the hexagon', 1, 10, 5)

    if st.button('Draw Hexagon'):
        fig = draw_hexagon(size)
        st.pyplot(fig)

if __name__ == '__main__':
    main()
