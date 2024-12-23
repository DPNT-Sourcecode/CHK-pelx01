

# noinspection PyUnusedLocal
# skus = unicode string

def checkout(skus):
    price_list = {
        "A":50,
        "B":30,
        "C":20,
        "D":15,
    }

    special_offers = {
        "A": (3, 130),
        "B": (2, 45),
    }

    valid_items = set(price_list.keys())
    if (len(skus) < 1):
        return -1
    if not all(i in valid_items for i in skus):
        return -1

    item_counts = {char: skus.count(char) for char in skus if char in price_list}
    total_price = 0

    for item, count in item_counts.items():
        if item in special_offers:
            offer_quanity, offer_price = special_offers[item]
            eligible_offers = count // offer_quanity
            regular_items = count % offer_quanity
            total_price += (eligible_offers * offer_price) + (regular_items * price_list[item])
        else:
            total_price += count * price_list[item]
    
    return total_price

