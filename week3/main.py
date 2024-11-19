
price = int(input("Enter the original price"))
discount_percent = int(input("Enter the discount percentage"))

def calculate_discount(price, discount_percent):
    if (discount_percent > 20):
        final_price = price - ((discount_percent/100) * price)
    else:
        final_price = price
    return final_price
    
final_price = calculate_discount(price, discount_percent)

print("The final price after the discount is: ", final_price)
    
