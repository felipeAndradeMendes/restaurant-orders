# Req 3
import csv
from models.dish import Dish
from models.ingredient import Ingredient


# def get_dishes_from_csv(path: str):
#     with open(path) as file:
#         menu_database = csv.DictReader(file, delimiter=",")
#         data = menu_database
#         return data


class MenuData:
    def __init__(self, source_path: str) -> None:
        self.dishes = set()
        self.__dish_names = {}

        with open(source_path) as file:
            menu_database = csv.DictReader(file, delimiter=",")
            header, *data = menu_database

        for line in data:
            name = line["dish"]
            price = float(line["price"])
            ingredient = line["ingredient"]
            amount = line["recipe_amount"]
            # print('INGREDIENT', ingredient)
            # print('AMOUNT:', amount)

            if name not in self.__dish_names:
                self.__dish_names[name] = Dish(name, price)
            self.__dish_names[name].add_ingredient_dependency(
                Ingredient(ingredient), amount
            )
            self.dishes.add(self.__dish_names[name])


# print(get_dishes_from_csv("../../data/menu_base_data.csv"))
# test_menu = MenuData("../../data/menu_base_data.csv")
# print(test_menu.dishes.__eq__())
# test_menu = MenuData("tests/mocks/menu_base_data.csv")


# print(Dish("Prato 01", 12.90))
