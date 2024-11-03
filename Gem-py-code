
import math

def calculate_strips(rectangle_width, rectangle_height, triangle_base, triangle_side, strip_width):
    """
    Calculates the number and height of strips for a 7-sided polygon.

    Args:
        rectangle_width: Width of the rectangle.
        rectangle_height: Height of the rectangle.
        triangle_base: Base of the triangle.
        triangle_side: Side length of the triangle.
        strip_width: Width of each strip.

    Returns:
        A list of tuples, where each tuple contains the number of strips and their heights.
    """

    # Calculate the height of the triangle using Heron's formula
    s = (triangle_side + triangle_side + triangle_base) / 2
    triangle_height = 2 * math.sqrt(s * (s - triangle_side) * (s - triangle_side) * (s - triangle_base)) / triangle_base

    # Calculate the number of strips for the rectangle
    num_rectangle_strips = int(rectangle_width / strip_width)

    # Calculate the number of strips for half of the triangle
    num_half_triangle_strips = int(triangle_base / (2 * strip_width))

    # Calculate the height of each strip for the rectangle
    rectangle_strip_height = rectangle_height

    # Calculate the height of each strip for half of the triangle
    triangle_half_strip_heights = []
    slope = triangle_height / (triangle_base / 2)
    for i in range(1, num_half_triangle_strips + 1):
        x = i * strip_width
        triangle_half_strip_height = slope * x
        triangle_half_strip_heights.append(triangle_half_strip_height)

    # Mirror the heights for the other half of the triangle
    triangle_strip_heights = triangle_half_strip_heights + triangle_half_strip_heights[::-1]

    return num_rectangle_strips, rectangle_strip_height, num_half_triangle_strips * 2, triangle_strip_heights

# Example usage:
rectangle_width = 20
rectangle_height = 10
triangle_base = 6
triangle_side = 5
strip_width = 1

num_rectangle_strips, rectangle_strip_height, num_triangle_strips, triangle_strip_heights = calculate_strips(rectangle_width, rectangle_height, triangle_base, triangle_side, strip_width)

print(f"{num_rectangle_strips}x of {rectangle_strip_height:.1f}")
for height in triangle_strip_heights:
    print(f"{num_triangle_strips // 2}x of {height:.1f}")
