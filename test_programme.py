from programme import addition


def testAditionSucces():
    result = addition(1,3)
    assert result == 4

def AdditionErreur():
    result = addition("huit",2)
    assert result == "Erreur"

    