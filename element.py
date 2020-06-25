class Element:

    def __init__(self, x, y):
        self.q_table = []
        self.x = x
        self.y = y
        self.initial_x = x
        self.initial_y = y

    def move(self, x, y):
            self.x += x
            self.y += y

    def get_position(self):
        return self.x, self.y

    def set_position(self, x, y):
        self.x = x
        self.y = y

    def distance(self, other_element):
        return self.x - other_element.x, self.y - other_element.y
