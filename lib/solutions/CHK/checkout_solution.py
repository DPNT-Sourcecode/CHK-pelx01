

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
        "E":40,
        "F":10,
        "G":20,
        "H":10,
        "I":35,
        "J":60,
        "K":80,
        "L":90,
        "M":15,
        "N":40,
        "O":10,
        "P":50,
        "Q":30,
        "R":50,
        "S":30,
        "T":20,
        "U":40,
        "V":50,
        "W":20,
        "X":90,
        "Y":10,
        "Z":50
    }

    special_offers = {
        "A": [(5, 200), (3, 130)],
        "B": [(2, 45)],
        "F": [(3, 20)],
    }

    valid_items = set(price_list.keys())
    if (len(skus) < 1):
        return 0
    if not all(i in valid_items for i in skus):
        return -1

    item_counts = {char: skus.count(char) for char in skus if char in price_list}
    item_counts = free_item_check(item_counts)

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
    return total_price

