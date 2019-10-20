R = 10
price_Kr = 50
in_box = 25
babka = 75
delivery = 350

amount = int(input("Enter amount of Kr: "))
loss = price_Kr * amount + delivery + babka * round(amount / in_box)
price = loss /(((100 - R)/100) * amount)

print(price)