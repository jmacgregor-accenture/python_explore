from pencilkatapython.pencil import Pencil

def test_pencilExists():
    pencil = Pencil()

    assert pencil.durability == 0