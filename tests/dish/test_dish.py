import pytest
from src.models.dish import Dish  # noqa: F401, E261, E501
from src.models.ingredient import Ingredient, Restriction


# Req 2
def test_dish():
    prato1 = Dish("Prato 01", 10.90)
    prato2 = Dish("Pastel de Bacon", 15.50)

    ing_bacon = Ingredient("bacon")
    ing_ovo = Ingredient("ovo")
    ing_farinha = Ingredient("farinha")

    assert prato1.name == "Prato 01"

    assert prato1.__repr__() == "Dish('Prato 01', R$10.90)"

    assert prato1.__eq__(prato1) is True
    assert prato1.__eq__(prato2) is False

    assert prato1.__hash__() == prato1.__hash__()
    assert prato1.__hash__() != prato2.__hash__()

    prato2.add_ingredient_dependency(ing_ovo, 1)
    prato2.add_ingredient_dependency(ing_bacon, 2)
    prato2.add_ingredient_dependency(ing_farinha, 3)

    assert prato2.get_ingredients() == {
        Ingredient("ovo"),
        Ingredient("bacon"),
        Ingredient("farinha"),
    }

    assert prato2.get_restrictions() == {
        Restriction.GLUTEN,
        Restriction.ANIMAL_DERIVED,
        Restriction.ANIMAL_MEAT,
    }

    with pytest.raises(TypeError, match="Dish price must be float."):
        Dish("Prato com preço nao float", "12.90")

    with pytest.raises(
        ValueError, match="Dish price must be greater then zero."
    ):
        Dish("Prato com preço menor que zero", -12.90)
