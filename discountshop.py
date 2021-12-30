shopping = []
how_many = input("how many items of shopping do you have? ")
how_many = int(how_many)
if how_many > 4:
    price = 30
    price = int(price)
    over4Items = "£" + str(price)
    discount = 5
    discount = int(discount)
    print("You qualify for a discount of 20%")
    for item_number in range(how_many):
        item = input("what is the item? " + str(item_number) + "? ")
        shopping.append(item)   
    your_item=" ".join(map(str,shopping)) 
    discount_price = 20
    print(discount) 
    print(price)  
    result = price / discount
    final_price = price - result
    print("Your total items are " + str(how_many) + " in your shopping list and the price is £" + str(price) + " and you qualify for " + str(discount_price) + " percent. Your total price is: " + str(price) + " - " + str(result) + " = £" + str(final_price) + " and these are your shopping items: " + your_item + ".")
elif how_many < 5 and how_many > 1:
    tax = 20
    percentage = 5
    total_price = how_many * percentage
    print("Your total items are " + str(how_many) + " in your shopping list and the price is " + str(how_many) + " * " + "tax percentage: " + str(percentage) + " = " + " total price of £" + str(total_price) + ".")
elif how_many == 0 or how_many == "zero" or how_many == "none":
    print("I do not require anything this week, thank you for your time.")  
