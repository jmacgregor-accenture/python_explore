from pencilkatapython.paper import Paper

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