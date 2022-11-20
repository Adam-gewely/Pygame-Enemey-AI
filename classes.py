class Player:
    x = int
    y = int
    surface = None
    rect = None

    def __init__(self, x: int, y: int):
        self.x = x
        self.y = y


class Enemy:
    x = int
    y = int
    surface = None
    rect = None

    def __init__(self, x: int, y: int):
        self.x = x
        self.y = y
