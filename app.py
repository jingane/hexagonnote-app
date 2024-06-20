import streamlit as st
import matplotlib.pyplot as plt

# Explicitly set matplotlib backend
plt.switch_backend('Agg')

# Your Streamlit app code
st.title('Hexagon Note')

# Example: Plot a simple graph
x = [1, 2, 3, 4, 5]
y = [10, 20, 30, 40, 50]
plt.plot(x, y)
st.pyplot()
