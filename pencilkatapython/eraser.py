class Eraser():

    def __init__(self, startDurability):
        self.durability = startDurability

    def erase(self, itemToErase):
        self.durability -= 1