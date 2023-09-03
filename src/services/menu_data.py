# Req 3
import csv

# from src.models.dish import Dish
# from src.models.ingredient import Ingredient

# usar sem testes
from models.dish import Dish
from models.ingredient import Ingredient


class MenuData:
    def __init__(self, source_path: str) -> None:
        self.dishes = set()
        self.__dish_names = {}
        # usar sem testes
        with open(source_path, "r") as file:
            # usar com testes
            # with open('../' + source_path, "r") as file:
            menu_database = csv.DictReader(file, delimiter=",")
            data = menu_database
            # como retornar todas as linhas, sem pular a primeira?
            # o for estava fora do with open...

            for line in data:
                name = line["dish"]
                price = float(line["price"])
                ingredient = line["ingredient"]
                amount = int(line["recipe_amount"])
                # print('INGREDIENT', ingredient)
                # print('AMOUNT:', amount)

                if name not in self.__dish_names:
                    self.__dish_names[name] = Dish(name, price)
                self.__dish_names[name].add_ingredient_dependency(
                    Ingredient(ingredient), amount
                )
                self.dishes.add(self.__dish_names[name])


path1 = "../../tests/mocks/menu_base_data.csv"

# if __name__ == "__main__":
#     menu1 = MenuData(path1)

#     print(menu1.dishes)
