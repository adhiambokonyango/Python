# object oriented programming
# object have state and behavior
# car; state- height, color, mileage, weight, size, type, make
# behavior - moves, carries, sounds
# class ; can contain states and behaviors of an object


class Triangle:

    def __init__(self, base, height, color):  # special func for declaring states/properties
        # add states to self
        self.base = base
        self.height = height
        self.color = color

    # do behaviors
    def findArea(self):
        return 0.5 * self.base * self.height


# create a real object
object = Triangle(base=5, height=4, color='blue')

print(object.findArea())

