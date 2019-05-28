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

    def erase(self, stringToClear):
        replaceStart = self.content.rfind(stringToClear)
        lengthToReplace = len(stringToClear)
        start = self.content[:replaceStart]
        end = self.content[(replaceStart + lengthToReplace):]
        middle = ""
        count = 0
        while count < lengthToReplace:
            middle += " "
            count += 1

        self.content = F"{start}{middle}{end}"