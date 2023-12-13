class Rectangle:
     def __init__(self, width, height, x, y):
         self.width = width
         self.height = height
         self.x = x
         self.y = y
     def display(self):
        """
        displays the rectangle using '#' character
        """
        for _ in range(self.y):
            print()
        for _ in range(self.height):
            print(" " * self.x + "#" * self.width)

     def __str__(self):
        return "width = {}\nheight = {}\nx = {}\ny = {}".format(self.width, self.height, self.x, self.y)

     def update(self, *args):
        if len(args) >= 1:
            self.width = args[0]
        if len(args) >= 2:
             self.height = args[1]
        if len(args) >= 3:
            self.x = args[2]
        if len(args) >= 4:
            self.y = args[3]






a = Rectangle(10, 10, 10, 10)
print(a)
print()
a.update(2)
print(a)



def test_save_to_file(self):
        #test with valid
        r1 = Rectangle(10, 7, 2, 8)
        r2 = Rectangle(2, 4)
        Rectangle.save_to_file([r1, r2])
        output = [{"y": 8, "x": 2, "id": 1, "width": 10, "height": 7},
                  {"y": 0, "x": 0, "id": 2, "width": 2, "height": 4}]
        with open("rectangle.json", 'r') as f:
            self.assertEqual(output, f.read())

def test_save_to_file_empty(self):
        list_obj = []
        Rectangle.save_to_file(list_obj)

        with open("rectangle.json", "r") as f:
            result = f.read()
            output = '[]'
        self.assertEqual(output, result)