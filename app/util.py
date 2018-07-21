from app.menudata import menu_items

def find_item(category, id):
    items = menu_items[category]

    for item in items:
        if item['id'] == id:
            num_pizzas = int(item['pizzas'])
            pizzas = []
            for i in range(0, num_pizzas):
                pizza_text = 'Pizza ' + str(i)
                pizzas.append({'name': pizza_text})

            num_pops = int(item['extras']['Pop'])
            pops = []
            for i in range(0, num_pops):
                pops_text = 'Pop ' + str(i)
                pops.append({'name': pops_text})

            num_dips = int(item['extras']['Dip'])
            dips = []
            for i in range(0, num_dips):
                dips_text = 'Dip ' + str(i)
                dips.append({'name': dips_text})

            wings = item['extras']['Wings']
            if wings == '0':
                wings = []
            else:
                wing_text = wings + ' of Wings'
                wings = [{'name': wing_text}]

            default_toppings = item['default_toppings']
            if default_toppings == 'null':
                default_toppings = []
            
            return item, pizzas, default_toppings, wings, pops, dips 

    #if it makes it down here, item not found
    return 'null'
