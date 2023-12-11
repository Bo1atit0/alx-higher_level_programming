def display(width=2, height=2, x=2, y=2):
        """
        displays the rectangle using '#' character
        """
        for _ in range(height):
              print()

        for _ in range(height):
            print(" " * x + "#" * width)

display()