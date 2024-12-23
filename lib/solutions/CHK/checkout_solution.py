

# noinspection PyUnusedLocal
# skus = unicode string

from collections import Counter


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

    # item_counts = {k: v for k, v in Counter(skus).items() if k in price_list}
    item_counts = {char: skus.count(char) for char in skus if char in price_list}
    
    print(price_list)
    print(item_counts)

    total_price = 0

    for item, count in item_counts.items():
        if item in special_offers:
            offer_quanity, offer_price = special_offers[item]
            eligible_offers = count // offer_quanity
            regular_items = count // offer_quanity
            print (item, eligible_offers)
            print (item, regular_items)

        total_item_count = price_list[item] * item_counts[item]
        # print(total_item_count)
    # print(skus)

checkout("ABCDCBAABCABBAAAZZZ")

