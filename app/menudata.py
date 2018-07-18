deal_items = [
        {
            'name': '2 Pizza Deal',
            'desc': '2 Pizzas with 4 Toppings each, 4 Pops, and 4 Dips',
            'price': '22.99',
            'pizzas': '2',
			'size': 'Small',
			'toppings': '4',
			'default_toppings': 'null',
			'addon':  [
				{
					'name': 'Upgrade to Medium',
					'price': '4.00'
				},
				{
					'name': 'Upgrade to Large',
					'price': '8.00'
				},
				{
					'name': 'Upgrade to X-Large',
					'price': '11.00'
				},
				{
					'name': 'Upgrade to Party',
					'price': '21.00'
				}
			],
		  	'extras': {
				'Wings': '0',
				'Garlic bread with cheese': 'False',
				'Pop': '4',
				'Dip': '4',
				'Pasta': 'False'
		  	}
        },
        {
            'name': 'Triple Deal',
            'desc': '3 Pizzas with 3 Toppings each',
            'price': '30.99',
            'pizzas': '3',
			'size': 'Medium',
			'toppings': '3',
			'default_toppings': 'null',
			'addon':  [
				{
					'name': 'Upgrade to Large',
					'price': '5.00'
				},
				{
					'name': 'Upgrade to X-Large',
					'price': '9.00'
				},
				{
					'name': 'Upgrade to Party',
					'price': '13.00'
				}
			],
		  	'extras': {
				'Wings': '0',
				'Garlic bread with cheese': 'False',
				'Pop': '0',
				'Dip': '0',
				'Pasta': 'False'
		  	}
        },
        {
            'name': 'Mega Deal',
            'desc': '2 Pizzas with 3 Toppings each, 1lb of Wings, 4 Pops, 2 Dips, and Garlic Bread w/ Cheese',
            'price': '32.99',
            'pizzas': '2',
			'size': 'Medium',
			'toppings': '3',
			'default_toppings': 'null',
			'addon':  [
				{
					'name': 'Upgrade to Large',
					'price': '4.00'
				}
			],
		  	'extras': {
				'Wings': '1lb',
				'Garlic bread with cheese': 'True',
				'Pop': '4',
				'Dip': '2',
				'Pasta': 'False'
		  	}
        },
        {
            'name': 'Monster Deal',
            'desc': '2 Pizzas with 3 Toppings each, 2lbs of Wings, 4 Pops, 4 Dips, and Garlic Bread w/ Cheese',
            'price': '36.99',
            'pizzas': '2',
			'size': 'Medium',
			'toppings': '3',
			'default_toppings': 'null',
			'addon':  [
				{
					'name': 'Upgrade to Large',
					'price': '4.00'
				},
				{
					'name': 'Upgrade to X-Large',
					'price': '10.00'
				}
			],
		  	'extras': {
				'Wings': '2lb',
				'Garlic bread with cheese': 'True',
				'Pop': '4',
				'Dip': '4',
				'Pasta': 'False'
		  	}
        },
        {
            'name': 'Party Deal',
            'desc': '2 Topping Party Pizza with 2 Pops and 2 Dips',
            'price': '25.99',
            'pizzas': '1',
			'size': 'Party',
			'toppings': '2',
			'default_toppings': 'null',
			'addon':  'null',
		  	'extras': {
				'Wings': '0',
				'Garlic bread with cheese': 'False',
				'Pop': '2',
				'Dip': '2',
				'Pasta': 'False'
		  	}
        },
        {
            'name': 'Panzo and Pop',
            'desc': '2 Panzerottis with 3 Toppings each, 2 Pops, and 2 Dips',
            'price': '19.99',
            'pizzas': '2',
			'size': 'Medium Panzo',
			'toppings': '3',
			'default_toppings': 'null',
			'addon':  [
				{
					'name': 'Upgrade to Large',
					'price': '2.00'
				}
			],
		  	'extras': {
				'Wings': '0',
				'Garlic bread with cheese': 'False',
				'Pop': '2',
				'Dip': '2',
				'Pasta': 'False'
		  	}
        },
        {
            'name': 'Family Deal',
            'desc': 'Large 3 Topping Pizza with 1lb of Wings, 4 Pops, 2 Dips, Garlic Bread w/ Cheese, and Spaghetti w/ Meat Sauce',
            'price': '33.99',
            'pizzas': '1',
			'size': 'Large',
			'toppings': '3',
			'default_toppings': 'null',
			'addon':  'null',
		  	'extras': {
				'Wings': '1lb',
				'Garlic bread with cheese': 'True',
				'Pop': '4',
				'Dip': '2',
				'Pasta': 'True'
		  	}
        },
        {
            'name': 'Supreme Special',
            'desc': '3 Topping Pizza with 1lb of Wings, 4 Pops, 2 Dips, and Garlic Bread w/ Cheese',
            'price': '25.99',
            'pizzas': '1',
			'size': 'Large',
			'toppings': '3',
			'default_toppings': 'null',
			'addon':  [
				{
					'name': 'Upgrade to X-Large',
					'price': '3.00'
				}
			],
		  	'extras': {
				'Wings': '1lb',
				'Garlic bread with cheese': 'True',
				'Pop': '4',
				'Dip': '2',
				'Pasta': 'False'
		  	}
        },
        {
            'name': 'Friendly Deal',
            'desc': '2 Topping Pizza with 2lbs of Wings, 4 Pops, 2 Dips, and Garlic Bread w/ Cheese',
            'price': '30.99',
            'pizzas': '1',
			'size': 'Medium',
			'toppings': '2',
			'default_toppings': 'null',
			'addon':  [
				{
					'name': 'Upgrade to Large',
					'price': '4.00'
				},
                {
					'name': 'Upgrade to X-Large',
					'price': '9.00'
				}
			],
		  	'extras': {
				'Wings': '2lb',
				'Garlic bread with cheese': 'True',
				'Pop': '4',
				'Dip': '2',
				'Pasta': 'False'
		  	}
        },
        {
            'name': 'X-Large Deal',
            'desc': '3 Topping X-Large Pizza, 3 Pops, and 2 Dips',
            'price': '15.99',
            'pizzas': '1',
			'size': 'X-Large',
			'toppings': '3',
			'default_toppings': 'null',
			'addon':  'null',
		  	'extras': {
				'Wings': '0',
				'Garlic bread with cheese': 'False',
				'Pop': '3',
				'Dip': '2',
				'Pasta': 'False'
		  	}
        },
        {
            'name': 'Pick-up Only Deal',
            'desc': 'X-Large Pepperoni Pizza',
            'price': '10.99',
            'pizzas': '1',
			'size': 'X-Large',
			'toppings': '0',
			'default_toppings': ['Pepperoni'],
			'addon':  'null',
		  	'extras': {
				'Wings': '0',
				'Garlic bread with cheese': 'False',
				'Pop': '0',
				'Dip': '0',
				'Pasta': 'False'
		  	}
        },
        {
            'name': 'Single Panzo Deal',
            'desc': '',
            'price': '9.99',
            'pizzas': '1',
			'size': 'Medium',
			'toppings': '0',
			'default_toppings': 'null',
			'addon':  [
				{
					'name': 'Upgrade to Large',
					'price': '1.00'
				},
            ],
		  	'extras': {
				'Wings': '0',
				'Garlic bread with cheese': 'False',
				'Pop': '0',
				'Dip': '0',
				'Pasta': 'False'
		  	}
        },
]

menu_items = {'deals': deal_items}
    

