import copy

warehouse = list()
warehouse.append({"name": "Lolly Pop", "price": 0.4, "weight": 133})
warehouse.append({"name": "Licorice", "price": 0.1, "weight": 251})
warehouse.append({"name": "Chocolate", "price": 1, "weight": 601})
warehouse.append({"name": "Sours", "price": 0.01, "weight": 513})
warehouse.append({"name": "Hard candies", "price": 0.3, "weight": 433})

print("Source list of candies")
for item in warehouse:
    print(item)

print("*" * 10)
print("Price proposal")

warehouse_copy = copy.deepcopy(warehouse)

for item in warehouse_copy:
    discount_percentage = 0.2

    if item["weight"] > 300:
        current_price = item["price"]
        discount = current_price * discount_percentage
        new_price = current_price - discount

        item["price"] = new_price

    print(item)


