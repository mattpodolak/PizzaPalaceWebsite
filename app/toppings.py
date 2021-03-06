from app.menudata import menu_items

# double check prices of toppings at different sizes
toppings = {
    "Meat" : [
        {
            "name": "Pepperoni",
            "value" : "1"
        },
        {
            "name": "Chicken",
            "value" : "2"
        },
        {
            "name": "Ham",
            "value" : "1"
        },
        {
            "name": "Bacon",
            "value" : "1"
        },
        {
            "name": "Italian Sausage",
            "value" : "1"
        },
        {
            "name": "Salami",
            "value": "1"
        },
        {
            "name": "Ground Beef",
            "value": "1"
        }
    ],
    "Cheese" : [
        {
            "name": "Mozzarella",
            "value" : "1"
        },
        {
            "name": "Cheddar",
            "value" : "1"
        },
        {
            "name": "Feta",
            "value" : "1"
        },
        {
            "name": "X-Cheese",
            "value" : "1"
        },
        {
            "name": "Double Cheese",
            "value" : "2"
        }        
    ],
    "Vegetable" : [
        {
            "name": "Mushroom",
            "value" : "1"
        },
        {
            "name": "Green Peppers",
            "value" : "1"
        },
        {
            "name": "Green Olives",
            "value" : "1"
        },        
        {
            "name": "Black Olives",
            "value" : "1"
        },  
        {
            "name": "Hot Peppers",
            "value" : "1"
        },    
        {
            "name": "Red Peppers",
            "value" : "1"
        },   
        {
            "name": "Jalapenos",
            "value" : "1"
        },   
        {
            "name": "Broccoli",
            "value" : "1"
        },   
        {
            "name": "Onions",
            "value" : "1"
        },
        {
            "name": "Red Onions",
            "value" : "1"
        },    
        {
            "name": "Pineapple",
            "value" : "1"
        },   
        {
            "name": "Tomatoes",
            "value" : "1"
        },
        {
            "name": "Sun Dried Tomatoes",
            "value" : "1"
        }, 
        {
            "name": "Spinach",
            "value" : "1"
        }        
    ],
    "Free_Toppings" : [
        {
            "name" : "Thin Crust",
            "value" : "0"
        },
        {
            "name" : "Thick Crust",
            "value" : "0"
        },
        {
            "name" : "Whole Wheat Dough",
            "value" : "0"
        },
        {
            "name" : "Gluten Free Dough",
            "value" : "0"
        },
        {
            "name" : "Extra Sauce",
            "value" : "0"
        },
        {
            "name" : "No Sauce",
            "value" : "0"
        },
        {
            "name" : "No Cheese",
            "value" : "0"
        },
        {
            "name" : "Chili Pepper",
            "value" : "0"
        },
        {
            "name" : "Fresh Garlic",
            "value" : "0"
        },
        {
            "name" : "Parmesan",
            "value" : "0"
        }        
    ],
    "Price": [
        {
            "name": "Medium",
            "value": "1.5"
        },
        {
            "name": "Large",
            "value": "2"
        },
        {
            "name": "X-Large",
            "value": "2.5"
        },
        {
            "name": "Party",
            "value": "3.5"
        },
        {
            "name": "Calzone",
            "value": "1"
        },
        {
            "name": "Medium Panzo",
            "value": "1.35"
        },
        {
            "name": "Large Panzo",
            "value": "1.5"
        }
    ],
    "Dip":[
        {
            "name": "Dip",
            "value": "0.96"
        }
    ],
    "Pop":[
        {
            "name": "Pop",
            "value": "1.5"
        }
    ]
}

Pops = ['Coke', 'Diet Coke', 'Coke Zero', 'Sprite', 'Nestea Iced Tea', "Barq's Root Beer", 'Canada Dry', 'C-Plus', 'Fresca', 'Brio', 'Water']
Dips = ['Ranch', 'Creamy Garlic', 'Blue Cheese', 'Marinara', 'Cheddar Chipotle', 'Spicy Buffalo']
Wings = []

# arrays for customization form
PopsArray = []
DipsArray = []
WingsArray = []
ToppingsArray = []
MeatToppings = []
CheeseToppings = []
VegToppings = []
FreeToppings = []

for wing in menu_items['wings']:
    Wings.append(wing['name'])

    #format for selectfields
    WingsArray.append((wing['name'], wing['name']))

#format pop, dip, and toppings for select fields in customize form
for pop in Pops:
    PopsArray.append((pop, pop))

for dip in Dips:
    DipsArray.append((dip, dip))

for topping in toppings['Meat']:
    MeatToppings.append((topping['name'], topping['name']))

for topping in toppings['Cheese']:
    CheeseToppings.append((topping['name'], topping['name']))

for topping in toppings['Vegetable']:
    VegToppings.append((topping['name'], topping['name']))

for topping in toppings['Free_Toppings']:
    FreeToppings.append((topping['name'], topping['name']))