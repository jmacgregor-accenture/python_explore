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
        whitespace = self._createWhiteSpace(lengthToReplace)

        self.content = F"{start}{whitespace}{end}"

    def _createWhiteSpace(self, lengthOfWhiteSpace):
        whitespace = ""
        count = 0
        while count < lengthOfWhiteSpace:
            whitespace += " "
            count += 1

        return whitespace