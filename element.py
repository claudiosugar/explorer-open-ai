class Element:

    def __init__(self, x, y):
        self.x = x
        self.y = y

    def move(self, x, y):
            self.x += x
            self.y += y
