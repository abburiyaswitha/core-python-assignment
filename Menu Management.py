def add_item_to_menu(menu,item):
    menu.append(item)
def remove_item_from_menu(menu,item):
    if item in menu:
        menu.remove(item)
    else:
        return f"{item} does not exist in the menu"
def check_item_availability(menu,item):
    if item in menu:
        return f"{item} is available"
    else:
        return f"{item} is not available"
menu = ["Pizza", "Burger", "Pasta", "Salad"]
add_item = "Tacos"
remove_item = "Salad"
check_item = "Pizza"
add_item_to_menu(menu,add_item)
remove_item_from_menu(menu,remove_item)
availability = check_item_availability(menu,check_item)
print("Updated menu:",menu)
print("Availability:",availability)
