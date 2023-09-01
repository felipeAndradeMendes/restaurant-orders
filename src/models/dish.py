from numbers import Real
from typing import Dict

from models.ingredient import Ingredient

Recipe = Dict[Ingredient, int]


class Dish:
    def __init__(self, name: str, price: float) -> None:
        self.name = name

        if not isinstance(price, Real):
            raise TypeError("Dish price must be float.")
        if price <= 0:
            raise ValueError("Dish price must be greater then zero.")

        self.price = price
        self.recipe: Recipe = {}

    def __repr__(self) -> str:
        return f"Dish('{self.name}', R${self.price:.2f})"

    def __eq__(self, other) -> bool:
        return self.__repr__() == other.__repr__()

    def __hash__(self) -> int:
        return hash(self.__repr__())

    def add_ingredient_dependency(self, ingredient: Ingredient, amount: int):
        self.recipe[ingredient] = amount

    def get_restrictions(self):
        return set(
            restriction
            for ingredient in self.recipe.keys()
            for restriction in ingredient.restrictions
        )

    def get_ingredients(self):
        return set(self.recipe.keys())


# prato1 = Dish('Prato 01', 10.90)
# prato2 = Dish('Pastel de Bacon', 15.50)

# ing_bacon = Ingredient('bacon')
# ing_ovo = Ingredient('ovo')
# ing_farinha = Ingredient('farinha')

# prato2.add_ingredient_dependency(ing_ovo, 1)
# prato2.add_ingredient_dependency(ing_bacon, 2)
# prato2.add_ingredient_dependency(ing_farinha, 3)

# print('entrei no dishes')
# print(prato2.get_ingredients())

# print(prato2.get_restrictions())
