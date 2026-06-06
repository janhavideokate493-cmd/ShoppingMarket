list1 = {
    "mangoes": 40,
    "apples": 50,
    "banana": 60,
    "cherry": 30,
    "strawberry":50
}

print("List of fruits:", list1)
list1["mangoes"]=50
cart_total = 0

while True:

    items = input("Enter fruit name you want: ").lower()

    if items in list1:

        quantity = int(input("Enter quantity: "))

        price = list1[items]

        total = price * quantity

        cart_total = cart_total + total

        print("Item =", items)
        print("Price =", price)
        print("Quantity =", quantity)
        print("Item Total =", total)

    else:
        print("Item out of stock")

    choice = input("Do you want to add more items? yes/no: ").lower()

    if choice == "no":
        break

print("Final Bill =", cart_total)