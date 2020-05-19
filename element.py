class Element:

    def __init__(self, x, y):
        self.x = x
        self.y = y

    def move(self, x, y):
            self.x += x
            self.y += y

    def position(self):
        return self.x, self.y

    def distance(self, exit_position):
        return self.x - exit_position.x, self.y - exit_position.y