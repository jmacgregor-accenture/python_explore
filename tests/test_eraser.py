from pencilkatapython.eraser import Eraser

def test_eraserHasDurability():
    testDurability = 55
    
    eraser = Eraser(testDurability)

    assert eraser.durability == testDurability

def test_eraserDegrades():
    testDurability = 55
    eraser = Eraser(testDurability)

    eraser.erase("b")

    assert eraser.durability == testDurability - 1

def test_eraserDoesNotDegradeOnWhiteSpace():
    testDurability = 55
    eraser = Eraser(testDurability)

    eraser.erase(" ")

    assert eraser.durability == testDurability