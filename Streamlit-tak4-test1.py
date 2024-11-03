import streamlit as st
import math

def calculate_strips(rectangle_width, rectangle_height, triangle_base, triangle_side, strip_width):
    # Your existing function code here

# Streamlit app
def main():
    st.title("Strip Calculator")

    # Input fields
    rectangle_width = st.number_input("Rectangle Width", min_value=0.0, step=0.1)
    rectangle_height = st.number_input("Rectangle Height", min_value=0.0, step=0.1)
    triangle_base = st.number_input("Triangle Base", min_value=0.0, step=0.1)
    triangle_side = st.number_input("Triangle Side", min_value=0.0, step=0.1)
    strip_width = st.number_input("Strip Width", min_value=0.0, step=0.1)

    # Button to trigger calculation
    if st.button("Calculate"):
        # Call the function and display results
        num_rectangle_strips, rectangle_strip_height, num_triangle_strips, triangle_strip_heights = calculate_strips(
            rectangle_width, rectangle_height, triangle_base, triangle_side, strip_width
        )

        st.write(f"{num_rectangle_strips}x of {rectangle_strip_height:.1f}")
        for height in triangle_strip_heights:
            st.write(f"{num_triangle_strips // 2}x of {height:.1f}")

if __name__ == "__main__":
    main()
