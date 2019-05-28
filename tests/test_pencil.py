from pencilkatapython.pencil import Pencil

def test_pencilExists():
    pencil = Pencil(0, 0)

    assert pencil.durability == 0

def test_canBeSetWithDurability():
    testDurability = 25
    pencil = Pencil(testDurability, 0)

    assert pencil.durability == 25

def test_durabilityLowersForEachCharacter():
    testDurability = 5
    pencil = Pencil(testDurability, 0)

    pencil.write("test")

    assert pencil.durability == 1

def test_upperCaseLettersDegradePointTwiceAsFast():
    testDurability = 5
    pencil = Pencil(testDurability, 0)

    pencil.write("Test")

    assert pencil.durability == 0

def test_spacesDoNotDegradePoint():
    testDurability = 5
    pencil = Pencil(testDurability, 0)

    pencil.write("oo oo")

    assert pencil.durability == 1

def test_pencilHasLength():
    testDurability = 5
    testLength = 3

    pencil = Pencil(testDurability, testLength)

    assert pencil.length == testLength

def test_sharpeningPencilReducesLength():
    testDurability = 5
    testLength = 3
    pencil = Pencil(testDurability, testLength)

    pencil.sharpen()

    assert pencil.length == testLength - 1

def test_sharpeningPencilRestoresDurability():
    testDurability = 5
    testLength = 3
    pencil = Pencil(testDurability, testLength)
    pencil.write("boo")

    pencil.sharpen()

    assert pencil.durability == testDurability