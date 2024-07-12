# Write a program to categorize the menu items based on the type of food.

from collections import defaultdict, namedtuple
from pprint import pprint

def categorize_menu(menu_items):
    categories = defaultdict(lambda: set())
    for item in menu_items:
        cat = item.type[0:3]
        match cat:
            case "MCO":
                categories["Main Course"].add(item.name)
            case "SOU":
                categories["Soup"].add(item.name)
            case "SAL":
                categories["Salad"].add(item.name)
            case "DES":
                categories["Dessert"].add(item.name)
            case "BEV":
                categories["Beverage"].add(item.name)
            case "STA":
                categories["Starter"].add(item.name)
            case _:
                categories["Other"].add(item.name)
    return categories
    

Food = namedtuple("Food", ["name", "type"])
menu_items = [
    Food("Salmon Fillet", "MCO003"),
    Food("Chicken Soup", "SOU002"),
    Food("Caesar Salad", "SAL001"),
    Food("Tiramisu", "DES002"),
    Food("Lemonade", "BEV002"),
    Food("Iced Tea", "BEV003"),
    Food("Bruschetta", "STA001"),
    Food("Cheesecake", "DES001"),
    Food("Chocolate Cake", "DES003"),
    Food("Ice Cream", "DES004"),
    Food("Greek Salad", "SAL002"),
    Food("Spring Rolls", "STA002"),
    Food("Minestrone", "SOU003"),
    Food("Garlic Bread", "STA003"),
    Food("Tomato Soup", "SOU001"),
    Food("Cappuccino", "BEV004"),
    Food("Garden Salad", "SAL003"),
    Food("Red Wine", "BEV001"),
    Food("Lasagna", "MCO004"),
    Food("Grilled Chicken", "MCO002"),
]
pprint(categorize_menu(menu_items))


