apple = 1000
banana = 2000

fruit = input("chose fruit(apple/banana): ").lower()
qty = int(input("Quantity: "))

price = apple if  fruit == "apple" else banana
total = price * qty
print("Total =", total)

pay = int(input("Your money: "))

if pay > total:
    print("chang =", pay - total)
elif pay == total:
    print("Exact payment.")
else:
    print("Not enough. Need", total - pay)

print("Thank you")        