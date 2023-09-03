from csv import DictReader
from typing import Dict

# from src.models.dish import Recipe
# from src.models.ingredient import Ingredient

# usar sem testes
from models.dish import Recipe, Dish
from models.ingredient import Ingredient


BASE_INVENTORY = "data/inventory_base_data.csv"

Inventory = Dict[Ingredient, int]


def read_csv_inventory(inventory_file_path=BASE_INVENTORY) -> Inventory:
    inventory = dict()

    # with open("../" + inventory_file_path, encoding="utf-8") as file:
    # with open('../../' + inventory_file_path, encoding="utf-8") as file:
    with open(inventory_file_path, encoding="utf-8") as file:
        for row in DictReader(file):
            ingredient = Ingredient(row["ingredient"])
            inventory[ingredient] = int(row["initial_amount"])

    return inventory


# Req 5
class InventoryMapping:
    def __init__(self, inventory_file_path=BASE_INVENTORY) -> None:
        self.inventory = read_csv_inventory(inventory_file_path)

    # Req 5.1
    def check_recipe_availability(self, recipe: Recipe) -> bool:
        try:
            for ingredient, amount in recipe.items():
                print("INVENTORY:", self.inventory.keys())
                print("INGREDIENTE:", ingredient.name)
                print("AMOUNT:", amount)
                # if ingredient.name not in self.inventory.keys().name:
                #     print('DEU RUIM!')
                #     return False
                if amount > self.inventory[ingredient]:
                    return False
        except KeyError:
            return False
        return True

    # Req 5.2
    def consume_recipe(self, recipe: Recipe) -> None:
        if not self.check_recipe_availability(recipe):
            raise ValueError
        for ingredient, amount in recipe.items():
            print("ingrediente amount:", self.inventory[ingredient])
            self.inventory[ingredient] -= amount
            print("ingrediente amount:", self.inventory[ingredient])


if __name__ == "__main__":
    prato2 = Dish("Pastel de Bacon", 15.50)

    ing_bacon = Ingredient("bacon")
    ing_ovo = Ingredient("ovo")
    ing_farinha = Ingredient("farinha")

    prato2.add_ingredient_dependency(ing_ovo, 1)
    prato2.add_ingredient_dependency(ing_bacon, 2)
    prato2.add_ingredient_dependency(ing_farinha, 3)

    inv1 = InventoryMapping()
    print(inv1.check_recipe_availability(prato2.recipe))
    print(inv1.consume_recipe(prato2.recipe))
