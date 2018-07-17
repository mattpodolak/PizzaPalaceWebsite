## Getting Started
Make new venv
'python -m venv pizza-venv'

Activate venv
'pizza-venv\Scripts\activate'

Set ENVIRONMENT variables
'set FLASK_APP=pizzasite.py'
'set MAIL_SERVER=smtp.googlemail.com'
'set MAIL_PORT=587'
'set MAIL_USE_TLS=1'
'set MAIL_USERNAME=<your-gmail-username>'
'set MAIL_PASSWORD=<your-gmail-password>'

Run app
'flask run'

Run shell in diff terminal for db manipulation
'flask shell'

Running into problems with db migration because u deleted a column?
'db.reflect()'
'db.drop_all()'
delete migration scripts
flask db migrate -m "message"
flask db upgrade

## Base
1. Dynamically change navbar CSS to show loaded page
2. Change CSS so navbar and footer looks correct
3. Make images responsive
4. Banner/modal when store is closed

## Menu
1. Implement dynamic loading for images depending on menu item
2. Create a class to load all the data from
3. Dynamic buttons which pass menu item id to topping selector

## Toppings
1. Update price based on what options are selected
2. Dynamic loading of toppings based on url
3. Add to cart stores order in database
4. Animations to show that item has been added to cart (button changes into text saying: item has been added to cart)

## Cart
1. Persistent cart over different pages for each session
2. Provide detailed description of contents of cart and allow removal (maybe editing too)

## Checkout 
1. Doesn't allow check out when store is closed or cart is empty
2. Links to dynamically generated tracking page
3. Send email to business and send confirmation to user

## Tracking
1. Generate tracking pages for orders
2. Update dynamically based on order process from the business side