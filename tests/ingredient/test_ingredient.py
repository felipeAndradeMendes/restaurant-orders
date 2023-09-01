from src.models.ingredient import (
    Ingredient,
    Restriction,
)  # noqa: F401, E261, E501


# Req 1
def test_ingredient():
    ingredient1 = Ingredient("Ingrediente 01")
    ingredient2 = Ingredient("bacon")

    assert ingredient1.__eq__(ingredient2) is False
    assert ingredient1.__eq__(ingredient1) is True
    assert ingredient1.__repr__() == "Ingredient('Ingrediente 01')"

    assert ingredient1.name == "Ingrediente 01"

    assert ingredient1.__hash__() == ingredient1.__hash__()
    assert ingredient1.__hash__() != ingredient2.__hash__()

    assert ingredient2.restrictions == {
        Restriction.ANIMAL_MEAT,
        Restriction.ANIMAL_DERIVED,
    }
