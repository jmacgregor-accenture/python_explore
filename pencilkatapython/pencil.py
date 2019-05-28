class Pencil:

    def __init__(self, startDurability, startLength):
        self.startDurability = startDurability
        self.durability = self.startDurability
        self.length = startLength

    def write(self, input):
        count = 0
        for char in input:
            if input[count].isspace() == False:
                if input[count].isupper():
                    self.durability -= 1

                self.durability -= 1
            count += 1

    def sharpen(self):
        if self.length > 0:
            self.length -= 1
            self.durability = self.startDurability