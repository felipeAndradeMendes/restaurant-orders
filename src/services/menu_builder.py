from typing import Dict, List

# Original
from services.inventory_control import InventoryMapping
from services.menu_data import MenuData

# from src.services.inventory_control import InventoryMapping
# from src.services.menu_data import MenuData

# from models.ingredient import Ingredient

# usar com testes (ver se original estava assim mesmo)
# DATA_PATH = "../data/menu_base_data.csv"
# INVENTORY_PATH = "../data/inventory_base_data.csv"

#  usar sem testes
DATA_PATH = "../../data/menu_base_data.csv"
INVENTORY_PATH = "../../data/inventory_base_data.csv"


class MenuBuilder:
    def __init__(self, data_path=DATA_PATH, inventory_path=INVENTORY_PATH):
        self.menu_data = MenuData(data_path)
        self.inventory = InventoryMapping(inventory_path)

    def make_order(self, dish_name: str) -> None:
        try:
            curr_dish = [
                dish
                for dish in self.menu_data.dishes
                if dish.name == dish_name
            ][0]
        except IndexError:
            raise ValueError("Dish does not exist")

        self.inventory.consume_recipe(curr_dish.recipe)

    # Req 4
    def get_main_menu(self, restriction=None) -> List[Dict]:
        result = []

        for item in self.menu_data.dishes:
            print("GET RESTRICITONS:", item.get_restrictions())
            # print('ITEM RESTRICTIONS:', Ingredient(restriction).restrictions)
            print("RESTRICITONS:", restriction)

            # has_restriction = False

            if (
                restriction not in item.get_restrictions()
                or restriction is None
            ):
                # print(
                #     "RESULTADO DE COMPARAÇÃO:",
                #     Ingredient(restriction).restrictions
                #     == item.get_restrictions(),
                # )
                # print(f"adicionando item {item} ao result")

                result.append(
                    {
                        "dish_name": item.name,
                        "price": item.price,
                        "ingredients": item.get_ingredients(),
                        "restrictions": item.get_restrictions(),
                    }
                )

        # print("RESULT:", result)
        return result


if __name__ == "__main__":
    menu_builder1 = MenuBuilder()
    print(menu_builder1.get_main_menu("ANIMAL_MEAT"))

    # PArei no meio da implementação desse req. Cabeça nao aguenta mais
    # Pensar em como verificar se a restrição existe na receita
