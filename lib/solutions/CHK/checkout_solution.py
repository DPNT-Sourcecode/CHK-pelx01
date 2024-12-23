

# noinspection PyUnusedLocal
# skus = unicode string

def free_item_check (item_counts):
    if "E" in item_counts:
        if item_counts["E"] >= 2:
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
        "A": (3, 130),
        "B": (2, 45),
        "E": (2, -price_list["B"])
    }

    valid_items = set(price_list.keys())
    if (len(skus) < 1):
        return 0
    if not all(i in valid_items for i in skus):
        return -1

    item_counts = {char: skus.count(char) for char in skus if char in price_list}
    total_price = 0

    item_counts = free_item_check(item_counts)

    for item, count in item_counts.items():
        if item in special_offers:
            offer_quanity, offer_price = special_offers[item]
            eligible_offers = count // offer_quanity
            regular_items = count % offer_quanity
            total_price += (eligible_offers * offer_price) + (regular_items * price_list[item])
        else:
            total_price += count * price_list[item]
    return total_price







