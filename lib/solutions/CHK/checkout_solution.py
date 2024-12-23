

# noinspection PyUnusedLocal
# skus = unicode string

def free_item_check (item_counts):
    if "E" in item_counts and "B" in item_counts and item_counts["E"] >= 2:
        item_counts["B"] -= item_counts["E"] // 2
        return item_counts
    else:
        return item_counts

def checkout(skus):
    price_list = {
        "A":50,
        "B":30,
        "C":20,
        "D":15,
        "E":40
    }

    special_offers = {
        "A": [(5, 200), (3, 130)],
        "B": [(2, 45)],
        "E": [(2, -price_list["B"])]
    }

    valid_items = set(price_list.keys())
    if (len(skus) < 1):
        return 0
    if not all(i in valid_items for i in skus):
        return -1

    item_counts = {char: skus.count(char) for char in skus if char in price_list}
    print(item_counts)
    item_counts = free_item_check(item_counts)
    print(item_counts)

    total_price = 0

    for item, count in item_counts.items():
        remaining_count = count
        if item in special_offers:
            for offer_quantity, offer_price in special_offers[item]:
                while remaining_count >= offer_quantity:
                    total_price += offer_price
                    remaining_count -= offer_quantity
        
        if remaining_count > 0:
            total_price += remaining_count * price_list[item]
    print(total_price, "\n")
    return total_price

checkout("EE")
checkout("EEB")
checkout("EEEB")
