from pencilkatapython.paper import Paper
from pencilkatapython.pencil import Pencil

def test_PaperExists():
    paper = Paper()

    assert paper is not None

def test_PaperHasEmptyContent():
    paper = Paper()
    result = paper.content

    assert result is ""

def test_WriteAddsStringToContent():
    testString = "string"
    paper = Paper()
    paper.write(testString)

    assert paper.content is testString

def test_WriteAppendsStringToContent():
    testOne = "test"
    testTwo = " two"
    paper = Paper()

    paper.write(testOne)
    paper.write(testTwo)

    assert paper.content == F"{testOne}{testTwo}"

def test_paperCanAddPencil():
    pencil = Pencil(5)
    paper = Paper()

    paper.addPencil(pencil)

    assert paper.pencil is not None

def test_dullPencilOnlyAddsWhitespace():
    pencil = Pencil(5)
    paper = Paper()
    paper.addPencil(pencil)
    testString = "Bow wow"
    expectedString = "Bow w  "

    paper.write(testString)

    assert paper.content == expectedString
