from app.menudata import menu_items

def find_item(category, id):
    items = menu_items[category]

    for item in items:
        if item['id'] == id:
            return item

    #if it makes it down here, item not found
    return 'null'