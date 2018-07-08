//******************* DEALS handler *******************
//3 PIZZAS tripledeal_addtop_1
function threepizzas_deal(order_type){
	//initialize variables
	var size = document.getElementsByName(order_type + '_size');
	var size_value;
	var dealcounter1 = 0;
	var dealcounter2 = 0;
	var dealcounter3 = 0;
	//first
	var pizza1_crust = document.getElementsByName(order_type + '_crust_1');
	var pizza1_crust_value;
	var pizza1_addtop = document.getElementsByName(order_type + '_addtop_1');
	var pizza1_addtop_value = '';
	var pizza1_dough = document.getElementsByName(order_type + '_dough_1');
	var pizza1_dough_value;
	var pizza1_sauce= document.getElementsByName(order_type + '_sauce_1');
	var pizza1_sauce_value;
	var pizza1_cheese= document.getElementsByName(order_type + '_cheese_1');
	var pizza1_cheese_value;
	var pizza1_meat= document.getElementsByName(order_type + '_meat_1');
	var pizza1_meat_value = '';
	//second
	var pizza2_crust = document.getElementsByName(order_type + '_crust_2');
	var pizza2_crust_value;
	var pizza2_addtop = document.getElementsByName(order_type + '_addtop_2');
	var pizza2_addtop_value = '';
	var pizza2_dough = document.getElementsByName(order_type + '_dough_2');
	var pizza2_dough_value;
	var pizza2_sauce= document.getElementsByName(order_type + '_sauce_2');
	var pizza2_sauce_value;
	var pizza2_cheese= document.getElementsByName(order_type + '_cheese_2');
	var pizza2_cheese_value;
	var pizza2_meat= document.getElementsByName(order_type + '_meat_2');
	var pizza2_meat_value = '';
	//third
	var pizza3_crust = document.getElementsByName(order_type + '_crust_3');
	var pizza3_crust_value;
	var pizza3_addtop = document.getElementsByName(order_type + '_addtop_3');
	var pizza3_addtop_value = '';
	var pizza3_dough = document.getElementsByName(order_type + '_dough_3');
	var pizza3_dough_value;
	var pizza3_sauce= document.getElementsByName(order_type + '_sauce_3');
	var pizza3_sauce_value;
	var pizza3_cheese= document.getElementsByName(order_type + '_cheese_3');
	var pizza3_cheese_value;
	var pizza3_meat= document.getElementsByName(order_type + '_meat_3');
	var pizza3_meat_value = '';
	
	var addtop_factor = 0;
	var deal_price = 0;
	
	//size
	for(var i = 0; i < size.length; i++){
		if(size[i].checked){
			size_value = size[i].value;
		}
	}
	if(size_value == 'medium'){
		deal_price += 30.99;
		addtop_factor = 1.35;
	}
	else if(size_value == 'large'){
		deal_price += 35.99;
		addtop_factor = 1.50;
	}
	else if(size_value == 'xlarge'){
		deal_price += 39.99;
		addtop_factor = 1.99;
	}
		else if(size_value == 'party'){
		deal_price += 39.99;
		addtop_factor = 2.99;
	}
	
	//PIZZA ONE
	//crust
	for(var i = 0; i < pizza1_crust.length; i++){
	    if(pizza1_crust[i].checked){
	        pizza1_crust_value = pizza1_crust[i].value;
	    }
	}
	//dough
	for(var i = 0; i < pizza1_dough.length; i++){
	    if(pizza1_dough[i].checked){
	        pizza1_dough_value = pizza1_dough[i].value;
	    }
	}
	//sauce
	for(var i = 0; i < pizza1_sauce.length; i++){
	    if(pizza1_sauce[i].checked){
	        pizza1_sauce_value = pizza1_sauce[i].value;
	    }
	}
	//cheese
	for(var i = 0; i < pizza1_cheese.length; i++){
	    if(pizza1_cheese[i].checked){
	    	if(pizza1_cheese[i].value == "doublecheese"){
	    	   //dealcounter1 += 2;
	           deal_price += addtop_factor*2;
	    	}
	    	if(pizza1_cheese[i].value == "xcheese"){
	    	   //dealcounter1 += 1;
	           deal_price += addtop_factor;
	    	}
	        pizza1_cheese_value = pizza1_cheese[i].value;
	    }
	}
	//addtop
	for(var i = 0; i < pizza1_addtop.length; i++){
	    if(pizza1_addtop[i].checked && pizza1_addtop[i].value != "garlic" && pizza1_addtop[i].value != "chilipepper" && pizza1_addtop[i].value != "parmesan"){
	    	dealcounter1 += 1;
	        pizza1_addtop_value +=  '+' + pizza1_addtop[i].value;
	        if(dealcounter1 > 3){
	        	deal_price += addtop_factor;
	        }
	    }
	    else if(pizza1_addtop[i].checked){
	    	pizza1_addtop_value +=  '+' + pizza1_addtop[i].value;
	    }
	}
	//special meat
	for(var i = 0; i < pizza1_meat.length; i++){
	    if(pizza1_meat[i].checked){
	    	dealcounter1 += 2; 
	        pizza1_addtop_value += '+' + pizza1_meat[i].value;
	        if(dealcounter1 == 4){
	        	deal_price += addtop_factor;
	        }
	        else if(dealcounter1 > 3){
	        	deal_price += 2 * addtop_factor;
	        }
	    }
	}
	
	//PIZZA TWO
	//crust
	for(var i = 0; i < pizza2_crust.length; i++){
	    if(pizza2_crust[i].checked){
	        pizza2_crust_value = pizza2_crust[i].value;
	    }
	}
	//dough
	for(var i = 0; i < pizza2_dough.length; i++){
	    if(pizza2_dough[i].checked){
	        pizza2_dough_value = pizza2_dough[i].value;
	    }
	}
	//sauce
	for(var i = 0; i < pizza1_sauce.length; i++){
	    if(pizza1_sauce[i].checked){
	        pizza2_sauce_value = pizza2_sauce[i].value;
	    }
	}
	//cheese
	for(var i = 0; i < pizza2_cheese.length; i++){
	    if(pizza2_cheese[i].checked){
	        if(pizza2_cheese[i].value == "doublecheese"){
	    	   //dealcounter2 += 2;
	           deal_price += addtop_factor*2;
	    	}
	    	if(pizza2_cheese[i].value == "xcheese"){
	    	   //dealcounter2 += 1;
	           deal_price += addtop_factor;
	    	}
	        pizza2_cheese_value = pizza2_cheese[i].value;
	    }
	}
	//addtop
	for(var i = 0; i < pizza2_addtop.length; i++){
	    if(pizza2_addtop[i].checked && pizza2_addtop[i].value != "garlic" && pizza2_addtop[i].value != "chilipepper" && pizza2_addtop[i].value != "parmesan"){
	    	dealcounter2 += 1;
	        pizza2_addtop_value +=  '+' + pizza2_addtop[i].value;
	        if(dealcounter2 > 3){
	        	deal_price += addtop_factor;
	        }
	    }
	    else if(pizza2_addtop[i].checked){
	    	pizza2_addtop_value +=  '+' + pizza2_addtop[i].value;
	    }
	}
	//special meat
	for(var i = 0; i < pizza2_meat.length; i++){
	    if(pizza2_meat[i].checked){
	    	dealcounter2 += 2;
	        pizza2_addtop_value += '+' + pizza2_meat[i].value;
	        if(dealcounter2 == 4){
	        	deal_price += addtop_factor;
	        }
	        else if(dealcounter2 > 3){
	        	deal_price += 2 * addtop_factor;
	        }
	    }
	}

	//PIZZA THREE
	//crust
	for(var i = 0; i < pizza3_crust.length; i++){
	    if(pizza3_crust[i].checked){
	        pizza3_crust_value = pizza3_crust[i].value;
	    }
	}
	//dough
	for(var i = 0; i < pizza3_dough.length; i++){
	    if(pizza3_dough[i].checked){
	        pizza3_dough_value = pizza3_dough[i].value;
	    }
	}
	//sauce
	for(var i = 0; i < pizza3_sauce.length; i++){
	    if(pizza3_sauce[i].checked){
	        pizza3_sauce_value = pizza3_sauce[i].value;
	    }
	}
	//cheese
	for(var i = 0; i < pizza3_cheese.length; i++){
	    if(pizza3_cheese[i].checked){
	    	if(pizza3_cheese[i].value == "doublecheese"){
	    	   //dealcounter3 += 2;
	           deal_price += addtop_factor*2;
	    	}
	    	if(pizza3_cheese[i].value == "xcheese"){
	    	   //dealcounter3 += 1;
	           deal_price += addtop_factor;
	    	}
	        pizza3_cheese_value = pizza3_cheese[i].value;
	    }
	}
	//addtop
	for(var i = 0; i < pizza3_addtop.length; i++){
	    if(pizza3_addtop[i].checked && pizza3_addtop[i].value != "garlic" && pizza3_addtop[i].value != "chilipepper" && pizza3_addtop[i].value != "parmesan"){
	    	dealcounter3 += 1;
	        pizza3_addtop_value +=  '+' + pizza3_addtop[i].value;
	        if(dealcounter3 > 3){
	        	deal_price += addtop_factor;
	        }
	    }
	    else if(pizza3_addtop[i].checked){
	    	pizza3_addtop_value +=  '+' + pizza3_addtop[i].value;
	    }
	}
	//special meat
	for(var i = 0; i < pizza3_meat.length; i++){
	    if(pizza3_meat[i].checked){
	    	dealcounter3 += 2;
	        pizza3_addtop_value +=  '+' + pizza3_meat[i].value;
	        if(dealcounter3 == 4){
	        	deal_price += addtop_factor;
	        }
	        else if(dealcounter3 > 3){
	        	deal_price += 2 * addtop_factor;
	        }
	    }
	}
	
	var all_checkboxes = jQuery(':checkbox'); // choose & store all checkboxes
	all_checkboxes.prop('checked', false); 
	var pizza1desc = '3 ' + size_value + ' (Pizza 1: ' + pizza1_crust_value + ' ' + pizza1_dough_value + ' ' + pizza1_sauce_value + ' ' + pizza1_cheese_value + ' ' + pizza1_addtop_value + ' ' + pizza1_meat_value + ')';
	var pizza2desc = '(Pizza 2: ' + pizza2_crust_value + ' ' + pizza2_dough_value + ' ' + pizza2_sauce_value + ' ' + pizza2_cheese_value + ' ' + pizza2_addtop_value + ' ' + pizza2_meat_value + ') ';
	var pizza3desc = '(Pizza 3: ' + pizza3_crust_value + ' ' + pizza3_dough_value + ' ' + pizza3_sauce_value + ' ' + pizza3_cheese_value + ' ' + pizza3_addtop_value + ' ' + pizza3_meat_value + ')';
	
	var templist1 = pizza1_meat_value + " " + pizza1_addtop_value;
	var templist2 = pizza2_meat_value + " " + pizza2_addtop_value;
	var templist3 = pizza3_meat_value + " " + pizza3_addtop_value;
	var finaldesc1 = "SIZE: " + size_value + " CRUST: " + pizza1_crust_value + " DOUGH: " +  pizza1_dough_value + " SAUCE: " +  pizza1_sauce_value + " CHEESE: " +  pizza1_cheese_value + "\n" +createToppingList(templist1);
	var finaldesc2 = "\n\n" + size_value + " " + pizza2_crust_value + " " +  pizza2_dough_value + " " +  pizza2_sauce_value + " " +  pizza2_cheese_value + "\n" +createToppingList(templist2);
	var finaldesc3 = "\n\n" + size_value + " " + pizza3_crust_value + " " +  pizza3_dough_value + " " +  pizza3_sauce_value + " " +  pizza3_cheese_value + "\n" +createToppingList(templist3);
	var itemdesc = finaldesc1.concat(finaldesc2).concat(finaldesc3 );
	return[itemdesc, deal_price];
	
}

//2 PIZZAS 
function twopizzas_deal(order_type, topping_limit){
	//initialize variables
	var size = document.getElementsByName(order_type + '_size');
	var size_value;
	var dealcounter1 = 0;
	var dealcounter2 = 0;
	//first
	var pizza1_crust = document.getElementsByName(order_type + '_crust_1');
	var pizza1_crust_value;
	var pizza1_addtop = document.getElementsByName(order_type + '_addtop_1');
	var pizza1_addtop_value = '';
	var pizza1_dough = document.getElementsByName(order_type + '_dough_1');
	var pizza1_dough_value;
	var pizza1_sauce= document.getElementsByName(order_type + '_sauce_1');
	var pizza1_sauce_value;
	var pizza1_cheese= document.getElementsByName(order_type + '_cheese_1');
	var pizza1_cheese_value;
	var pizza1_meat= document.getElementsByName(order_type + '_meat_1');
	var pizza1_meat_value = '';
	//second
	var pizza2_crust = document.getElementsByName(order_type + '_crust_2');
	var pizza2_crust_value;
	var pizza2_addtop = document.getElementsByName(order_type + '_addtop_2');
	var pizza2_addtop_value = '';
	var pizza2_dough = document.getElementsByName(order_type + '_dough_2');
	var pizza2_dough_value;
	var pizza2_sauce= document.getElementsByName(order_type + '_sauce_2');
	var pizza2_sauce_value;
	var pizza2_cheese= document.getElementsByName(order_type + '_cheese_2');
	var pizza2_cheese_value;
	var pizza2_meat= document.getElementsByName(order_type + '_meat_2');
	var pizza2_meat_value = '';
	
	var addtop_factor = 0;
	var deal_price = 0;
	for(var i = 0; i < size.length; i++){
		if(size[i].checked){
			size_value = size[i].value;
		}
	}
	//size
	if(size_value == 'small'){
		deal_price += 22.99;
		addtop_factor = 1.20;
	}
	else if(size_value == 'medium'){
		deal_price += 26.99;
		addtop_factor = 1.35;
	}
	else if(size_value == 'large'){
		deal_price += 30.99;
		addtop_factor = 1.50;
	}
	else if(size_value == 'xlarge'){
		deal_price += 33.99;
		addtop_factor = 1.99;
	}
	else if(size_value == 'monstermedium'){
		deal_price += 36.99;
		addtop_factor = 1.35;
	}
	else if(size_value == 'megamedium'){
		deal_price += 32.99;
		addtop_factor = 1.35;
	}
	else if(size_value == 'monsterlarge'){
		deal_price += 40.99;
		addtop_factor = 1.50;
	}
	else if(size_value == 'megalarge'){
		deal_price += 36.99;
		addtop_factor = 1.50;
	}
	else if(size_value == 'monsterxlarge'){
		deal_price += 46.99;
		addtop_factor = 1.99;
	}
	else if(size_value == 'party'){
		deal_price += 43.99;
		addtop_factor = 2.45;
	}
	//panzo deal
	else if(size_value == 'mediumpanzo'){
		deal_price += 19.99;
		addtop_factor = 1.35;
	}
	else if(size_value == 'largepanzo'){
		deal_price += 21.99;
		addtop_factor = 1.50;
	}
	
	//PIZZA 1 toppings
	//crust
	for(var i = 0; i < pizza1_crust.length; i++){
	    if(pizza1_crust[i].checked){
	        pizza1_crust_value = pizza1_crust[i].value;
	    }
	}
	//dough
	for(var i = 0; i < pizza1_dough.length; i++){
	    if(pizza1_dough[i].checked){
	        pizza1_dough_value = pizza1_dough[i].value;
	    }
	}
	//sauce
	for(var i = 0; i < pizza1_sauce.length; i++){
	    if(pizza1_sauce[i].checked){
	        pizza1_sauce_value = pizza1_sauce[i].value;
	    }
	}
	//cheese
	for(var i = 0; i < pizza1_cheese.length; i++){
	    if(pizza1_cheese[i].checked){
	    	if(pizza1_cheese[i].value == "doublecheese"){
	    	   //dealcounter1 += 2;
	           deal_price += addtop_factor*2;
	    	}
	    	if(pizza1_cheese[i].value == "xcheese"){
	    	   //dealcounter1 += 1;
	           deal_price += addtop_factor;
	    	}
	        pizza1_cheese_value = pizza1_cheese[i].value;
	    }
	}
	//addtop
	for(var i = 0; i < pizza1_addtop.length; i++){
	    if(pizza1_addtop[i].checked && pizza1_addtop[i].value != "garlic" && pizza1_addtop[i].value != "chilipepper" && pizza1_addtop[i].value != "parmesan"){
	    	dealcounter1 += 1;
	        pizza1_addtop_value +=  '+' + pizza1_addtop[i].value;
	        if(dealcounter1 > topping_limit){
	        	deal_price += addtop_factor;
	        }
	    }
	    else if(pizza1_addtop[i].checked){
	    	pizza1_addtop_value +=  '+' + pizza1_addtop[i].value;
	    }
	}
	//special meat
	for(var i = 0; i < pizza1_meat.length; i++){
	    if(pizza1_meat[i].checked){
	    	dealcounter1 += 2; 
	        pizza1_addtop_value += '+' + pizza1_meat[i].value;
	        if(dealcounter1 == topping_limit+1){
	        	deal_price += addtop_factor;
	        }
	        else if(dealcounter1 > topping_limit){
	        	deal_price += 2 * addtop_factor;
	        }
	    }
	}
	
	//PIZZA 2 toppings
	//crust
	for(var i = 0; i < pizza2_crust.length; i++){
	    if(pizza2_crust[i].checked){
	        pizza2_crust_value = pizza2_crust[i].value;
	    }
	}
	//dough
	for(var i = 0; i < pizza2_dough.length; i++){
	    if(pizza2_dough[i].checked){
	        pizza2_dough_value = pizza2_dough[i].value;
	    }
	}
	//sauce
	for(var i = 0; i < pizza2_sauce.length; i++){
	    if(pizza1_sauce[i].checked){
	        pizza2_sauce_value = pizza2_sauce[i].value;
	    }
	}
	//cheese
	for(var i = 0; i < pizza2_cheese.length; i++){
	    if(pizza2_cheese[i].checked){
	       if(pizza2_cheese[i].value == "doublecheese"){
	    	   //dealcounter2 += 2;
	           deal_price += addtop_factor*2;
	       }
	       if(pizza2_cheese[i].value == "xcheese"){
	    	   //dealcounter2 += 1;
	           deal_price += addtop_factor;
	       }
	        pizza2_cheese_value = pizza2_cheese[i].value;
	    }
	}
	//addtop
	for(var i = 0; i < pizza2_addtop.length; i++){
	    if(pizza2_addtop[i].checked && pizza2_addtop[i].value != "garlic" && pizza2_addtop[i].value != "chilipepper" && pizza2_addtop[i].value != "parmesan"){
	    	dealcounter2 += 1;
	        pizza2_addtop_value +=  '+' + pizza2_addtop[i].value;
	        if(dealcounter2 > topping_limit){
	        	deal_price += addtop_factor;
	        }
	    }
	     else if(pizza2_addtop[i].checked){
	    	pizza2_addtop_value +=  '+' + pizza2_addtop[i].value;
	    }
	}
	//special meat
	for(var i = 0; i < pizza2_meat.length; i++){
	    if(pizza2_meat[i].checked){
	    	dealcounter2 += 2;
	        pizza2_addtop_value += '+' + pizza2_meat[i].value;
	        if(dealcounter2 == topping_limit+1){
	        	deal_price += addtop_factor;
	        }
	        else if(dealcounter2 > topping_limit){
	        	deal_price += 2 * addtop_factor;
	        }
	    }
	}
	var all_checkboxes = jQuery(':checkbox'); // choose & store all checkboxes
	all_checkboxes.prop('checked', false); 
	var templist1 = pizza1_meat_value + " " + pizza1_addtop_value;
	var templist2 = pizza2_meat_value + " " + pizza2_addtop_value;
	var finaldesc1 = "SIZE: " + size_value + " CRUST: " + pizza1_crust_value + " DOUGH: " +  pizza1_dough_value + " SAUCE: " +  pizza1_sauce_value + " CHEESE: " +  pizza1_cheese_value + "\n" +createToppingList(templist1);
	var finaldesc2 = "\n\nSIZE: " + size_value + " CRUST: " + pizza2_crust_value + " DOUGH: " +  pizza2_dough_value + "  SAUCE:  " +  pizza2_sauce_value + " CHEESE: " +  pizza2_cheese_value + "\n" +createToppingList(templist2);
	
	var itemdesc = finaldesc1.concat(finaldesc2);
	return[itemdesc, deal_price];
}

//******************* WINGS hanlder*******************
function wing_order(order_type){
	var amount = document.getElementsByName(order_type + '_wings');
	var amount_value;
	var wing_price = 0;
	for(var i = 0; i < amount.length; i++){
		if(amount[i].checked){
			amount_value = amount[i].value;
		}
	}
	if(amount_value == 'onepound'){
		wing_price = 9.99;
	}
	else if(amount_value == 'twopounds'){
		wing_price = 18.99;
	}
	else if(amount_value == 'fourpounds'){
		wing_price = 36.99;
	}
	var all_checkboxes = jQuery(':checkbox'); // choose & store all checkboxes
	all_checkboxes.prop('checked', false); 
	return [amount_value, wing_price];
}
//******************* PIZZA handler *******************
function topping_desc(order_type, topping_limit){
	//standard
	var sizes = document.getElementsByName(order_type + '_sizes');
	var sizes_value;
	var crust = document.getElementsByName(order_type + '_crust');
	var crust_value;
	var dough = document.getElementsByName(order_type + '_dough');
	var dough_value;
	var sauce = document.getElementsByName(order_type + '_sauce');
	var sauce_value;
	//standard cheese choices
	var cheese = document.getElementsByName(order_type + '_cheese');
	var cheese_value;
	//addtional toppings (veg, meat, cheese)
	var additional = document.getElementsByName(order_type + '_additional_top');
	var additional_value = '';
	//special priced meats
	var meat = document.getElementsByName(order_type + '_meat');
	var meat_value = '';
	var pizza_price = 0;
	var addtop_factor = 0;
	var dealcounter = 0;
	//check size
	for(var i = 0; i < sizes.length; i++){
	    if(sizes[i].checked){
	        sizes_value = sizes[i].value;
	    }
	}
	//set size and additional topping cost
	if(sizes_value == 'small'){
		pizza_price += 8.95;
		addtop_factor = 1.20;
	}
	else if(sizes_value == 'medium'){
		pizza_price += 12.95;
		addtop_factor = 1.35;
	}
	else if(sizes_value == 'mediumdeal'){
		pizza_price += 13.95;
		addtop_factor = 1.35;
	}
	else if(sizes_value == 'large'){
		pizza_price += 16.95;
		addtop_factor = 1.50;
	}
	else if(sizes_value == 'largedeal'){
		pizza_price += 15.95;
		addtop_factor = 1.50;
	}
	else if(sizes_value == 'xlarge'){
		pizza_price += 19.95;
		addtop_factor = 1.99;
	}
	else if(sizes_value == 'xlargedeal'){
		pizza_price += 17.99;
		addtop_factor = 1.99;
	}
	else if(sizes_value == 'friendlymedium'){
		pizza_price += 30.99;
		addtop_factor = 1.35;
	}
	else if(sizes_value == 'friendlylarge'){
		pizza_price += 34.99;
		addtop_factor = 1.50;
	}
	else if(sizes_value == 'friendlyxlarge'){
		pizza_price += 39.99;
		addtop_factor = 1.99;
	}
	else if(sizes_value == 'palacespecialmedium'){
		pizza_price += 15.99;
		addtop_factor = 1.35;
	}
	else if(sizes_value == 'palacespeciallarge'){
		pizza_price += 17.99;
		addtop_factor = 1.50;
	}
	else if(sizes_value == 'palacespecialxlarge'){
		pizza_price += 19.99;
		addtop_factor = 1.99;
	}
	else if(sizes_value == 'xlargedeal'){
		pizza_price += 15.99;
		addtop_factor = 1.99;
	}
	else if(sizes_value == 'party'){
		pizza_price += 24.95;
		addtop_factor = 2.45;
	}
	//fam deal
	else if(sizes_value == 'famdeal'){
		pizza_price += 33.99;
		addtop_factor = 1.50;
	}
	//party deal
	else if(sizes_value == 'partydeal'){
		pizza_price += 25.99;
		addtop_factor = 2.45;
	}
	//pickup only deal
	else if(sizes_value == 'pickupdealxlarge'){
		pizza_price += 10.99;
		addtop_factor = 1.99;
	}
	//spinach deal
	if(sizes_value == 'spinachmedium'){
		pizza_price += 10.95;
		addtop_factor = 1.35;
	}
	else if(sizes_value == 'spinachlarge'){
		pizza_price += 12.95;
		addtop_factor = 1.50;
	}
	else if(sizes_value == 'spinachxlarge'){
		pizza_price += 14.95;
		addtop_factor = 1.99;
	}
	//supreme special
	if(sizes_value == 'supremelarge'){
		pizza_price += 25.99;
		addtop_factor = 1.50;
	}
	else if(sizes_value == 'supremexlarge'){
		pizza_price += 28.99;
		addtop_factor = 1.99;
	}
	//calzone deal
	if(sizes_value == 'mediumcalzone'){
		pizza_price += 9.99;
		addtop_factor = 1.35;
	}
	else if(sizes_value == 'largecalzone'){
		pizza_price += 10.99;
		addtop_factor = 1.50;
	}
	for(var i = 0; i < crust.length; i++){
	    if(crust[i].checked){
	        crust_value = crust[i].value;
	    }
	}
	for(var i = 0; i < dough.length; i++){
	    if(dough[i].checked){
	        dough_value = dough[i].value;
	    }
	}
	for(var i = 0; i < sauce.length; i++){
	    if(sauce[i].checked){
	        sauce_value = sauce[i].value;
	    }
	}
	for(var i = 0; i < cheese.length; i++){
	    if(cheese[i].checked){
	    	if(cheese[i].value == "doublecheese"){
	    	   //dealcounter += 2;
	           pizza_price += 2*addtop_factor;	           
	    	}
	    	if(cheese[i].value == "xcheese"){
	    	   //dealcounter += 1;
	           pizza_price += addtop_factor;
	    	}
	        cheese_value = cheese[i].value;
	    }
	}
	//special meat
	for(var i = 0; i < meat.length; i++){
	    if(meat[i].checked){
	    	dealcounter += 2;
	    	//meat_value wasnt work
	        additional_value +=  '+' + meat[i].value;
	        if(dealcounter == topping_limit+1){
	        	pizza_price += addtop_factor;
	        }
	        else if(dealcounter > topping_limit){
	        	pizza_price += 2 * addtop_factor;
	        }
	    }
	}
	//toppings
	for(var i = 0; i < additional.length; i++){
	    if(additional[i].checked && additional[i].value != "garlic" && additional[i].value != "chilipepper" && additional[i].value != "parmesan"){
	    	dealcounter += 1;
	        additional_value +=  '+' + additional[i].value;
	        if(dealcounter > topping_limit){
	        	pizza_price += addtop_factor;
	        }
	    }
	    else if(additional[i].checked){
	    	additional_value +=  '+' + additional[i].value;
	    }
	}
	var templist = meat_value + " " + additional_value;
	var finaldesc = "SIZE: " + sizes_value + " CRUST: " + crust_value + " DOUGH: " +  dough_value + " SAUCE: " +  sauce_value + " CHEESE: " +  cheese_value + "\n" +createToppingList(templist);
	var all_checkboxes = jQuery(':checkbox'); // choose & store all checkboxes
	all_checkboxes.prop('checked', false); 
	return[finaldesc, pizza_price];
}
//******************* TOPPINGS handler *******************
function createToppingList(toppingList){
	var itemdesc = toppingList.split('+').splice(1, toppingList.length);
	var fulltopping_list = ["chilipepper", "garlic", "cheddar", "parmesan", "feta", "mozzarella", "mushroom" , "redpeppers", "pineapple", "greenpepper", "broccoli", "tomatoes", "greenolives", "onions", "sundriedtomatoes", "blackolives", "redonions", "spinach", "hotpeppers", "pepperoni", "salami", "steak", "ham", "groundbeef", "chicken", "bacon", "eggplant", "italiansausage"];
	var finaltopping_list = "";
	for(var i = 0; i < fulltopping_list.length; i++){
		//toppings selected
		if(itemdesc.indexOf(fulltopping_list[i]) != -1){
			finaltopping_list += fulltopping_list[i] + "	    X \n";
		}
	}
	return finaltopping_list;
}