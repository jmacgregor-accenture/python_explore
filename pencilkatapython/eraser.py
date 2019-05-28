class Eraser():

    def __init__(self, startDurability):
        self.durability = startDurability

    def erase(self, itemToErase):
        if itemToErase.isspace() == False:
            self.durability -= 1