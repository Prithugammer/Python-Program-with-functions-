Tax_Rate = 0.13

def apply_discount(price,percent):

    new_price = price - (price * (percent/100))
    return new_price

def apply_tax(price):
    applied_tax = price + Tax_Rate*price
    return applied_tax

def final_price(price,discount):
    price_discount = apply_discount(price,discount)
    final = apply_tax(price_discount)
    return final



