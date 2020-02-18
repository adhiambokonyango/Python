# square obj
# states; height, width, color
# behavior; perimeter, area

class Square:
    def __init__(self, height, width, color):
        self.height = height
        self.width = width
        self.color = color

    def perimeter(self):
        return self.width + self.width +self.height + self.height

    def area(self):
        return self.height * self.width

    def appearance(self):
        return self.color


# states ; name , balance, branch, accNumber
# behavior,; deposit and withdrawal



