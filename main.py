def calculate_rectangle_area(length, width):
    """
    Calculate the area of a rectangle.

    Args:
    - length (float): The length of the rectangle.
    - width (float): The width of the rectangle.

    Returns:
    - float: The area of the rectangle.
    """
    return length * width

def main():
    # Get input from the user
    length = float(input("Enter the length of the rectangle: "))
    width = float(input("Enter the width of the rectangle: "))

    # Calculate the area
    area = calculate_rectangle_area(length, width)

    # Display the result
    print("The area of the rectangle is:", area)

if __name__ == "__main__":
    main()
