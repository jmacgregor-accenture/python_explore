from pencilkatapython.pencil import Pencil

def test_pencilExists():
    pencil = Pencil(0)

    assert pencil.durability == 0

def test_canBeSetWithDurability():
    testDurability = 25
    pencil = Pencil(testDurability)

    assert pencil.durability == 25