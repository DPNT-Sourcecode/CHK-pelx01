

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

    item_counts = {k: v for k, v in Counter(skus).items() if k in price_list}
    


    print(price_list)
    print(item_counts)

    for item in item_counts:
        total_item_count = price_list[item] * item_counts[item]
        print(total_item_count)
    # print(skus)

checkout("ABCDCBAABCABBAAAZZZ")
