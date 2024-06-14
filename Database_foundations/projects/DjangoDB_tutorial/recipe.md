
db - shop_manager

classes:
item : name price quantity?
item_repo: items_list item_quantity? create item
order: customer(name), ordered items, date,
order_repo: - list of order create order

App:

Welcome to the shop management program!

What do you want to do?
  1 = list all shop items
  2 = create a new item
  3 = list all orders
  4 = create a new order

1 [enter]

Here's a list of all shop items:

 #1 Super Shark Vacuum Cleaner - Unit price: 99 - Quantity: 30
 #2 Makerspresso Coffee Machine - Unit price: 69 - Quantity: 15
 (...)


