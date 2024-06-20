import streamlit as st
import numpy as np
import matplotlib
matplotlib.use('Agg')  # Use the 'Agg' backend explicitly
import matplotlib.pyplot as plt

def main():
    st.title('Streamlit with Matplotlib Example')
    
    # Generate some data
    x = np.linspace(0, 10, 100)
    y = np.sin(x)
    
    # Plot the data
    fig, ax = plt.subplots()
    ax.plot(x, y)
    
    # Display the plot in Streamlit
    st.pyplot(fig)

if __name__ == '__main__':
    main()
