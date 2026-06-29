from collections import Counter


def getPurchases(person):
    return []

def getFriends(person):
    return []

def itemsFriendsPurchases(person):
    already_bought = set(getPurchases(person))
    
    count = Counter()
    
    for friend in getFriends(person):
        for product in getPurchases(friend):
            if product not in already_bought:
                count[product] += 1
                
    return [product for product, _ in count.most_common()]
            