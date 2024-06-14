As a customer
So that I can check if I want to order something
I would like to see a list of dishes with prices.

As a customer
So that I can order the meal I want
I would like to be able to select some number of several available dishes.

As a customer
So that I can verify that my order is correct
I would like to see an itemised receipt with a grand total.

As a customer
So that I am reassured that my order will be delivered on time
I would like to receive a text such as "Thank you! Your order was placed and will be delivered before 18:52" after I have ordered.



classes needed:

Dish
attributes: price, name, available
functions set available/unavailable

Menu
attributes: list of dishes

functions: show and return available dishes


Order
attributes: list of dishes in order, total price

functions: 
add item to the order
remove item from order
confirm order?


Contacter (SMS/e-mail)
attributes: delivery time
functions:
send message