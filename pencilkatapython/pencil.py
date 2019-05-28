class Pencil:

    def __init__(self, startDurability, startLength):
        self.durability = startDurability
        self.length = startLength

    def write(self, input):
        count = 0
        for char in input:
            if input[count].isspace() == False:
                if input[count].isupper():
                    self.durability -= 1

                self.durability -= 1
            count += 1