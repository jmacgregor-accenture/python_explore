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
    pencil = Pencil(25, 0)

    paper.write(testString, pencil)

    assert paper.content == testString

def test_WriteAppendsStringToContent():
    testOne = "test"
    testTwo = " two"
    paper = Paper()
    pencil = Pencil(25, 0)

    paper.write(testOne, pencil)
    paper.write(testTwo, pencil)

    assert paper.content == F"{testOne}{testTwo}"

def test_paperCanAddPencil():
    pencil = Pencil(5, 0)
    paper = Paper()

    paper.addPencil(pencil)

    assert paper.pencil is not None

def test_dullPencilOnlyAddsWhitespace():
    pencil = Pencil(5, 0)
    paper = Paper()
    testString = "Bow wow"
    expectedString = "Bow w  "

    paper.write(testString, pencil)

    assert paper.content == expectedString

def test_eraseStringRemovesLastInstanceOfStringFromContent():
    pencil = Pencil(25,0)
    paper = Paper()
    testString = "taco taco taco"
    expectedString = "taco taco     "
    paper.write(testString, pencil)

    paper.erase("taco")

    assert paper.content == expectedString

def test_eraseStringRemovesTwoInstancesOfStringFromContent():
    pencil = Pencil(25,0)
    paper = Paper()
    testString = "taco taco taco"
    expectedString = "taco          "
    paper.write(testString, pencil)

    paper.erase("taco")
    paper.erase("taco")

    assert paper.content == expectedString