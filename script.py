#Lovely Loveseats for Neat Suites on Fleet Street


#Adding In The Catalog

lovely_loveseat_description = "\nLovely Loveseat. Tufted polyester blend on wood. 32 inches high x 40 inches wide x 30 inches deep. Red or white."
lovely_loveseat_price = 254.00

stylish_settee_description = "\nStylish Settee. Faux leather on birch. 29.50 inches high x 54.75 inches wide x 28 inches deep. Black."
stylish_settee_price = 180.50


luxurious_lamp_description = "\nLuxurious Lamp. Glass and iron. 36 inches tall. Brown with cream shade."
luxurious_lamp_price = 52.15

#In order to be a Business, we should also be calculating sales tax.
sales_tax = 0.088    #8.8%

#Our First Customer
customer_one_total = 0
customer_one_itemization = ""

customer_one_total += lovely_loveseat_price
customer_one_itemization += lovely_loveseat_description

customer_one_total += luxurious_lamp_price
customer_one_itemization += luxurious_lamp_description

#Calcuting Sales Tax
customer_one_tax = customer_one_total * sales_tax

customer_one_total += customer_one_tax

#Printing Up their Receipt
print("Customer One Items: ")
print(customer_one_itemization)
print("\nCustomer One Total: ")
print(customer_one_total)






