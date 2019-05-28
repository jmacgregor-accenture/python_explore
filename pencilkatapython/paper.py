class Paper:
    content = ""

    def write(self, input, pencil):
        for char in input:
            if pencil.durability > 0:
                pencil.write(char)
                self.content += char
            else:
                self.content += " "

    def addPencil(self, pencil):
        self.pencil = pencil