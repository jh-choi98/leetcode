from collections import Counter

"""
P = 본인 구매 수 (set 만들기)
F = 친구 수, Q = 친구당 평균 구매 수 → 모든 친구 구매 순회가 O(F·Q)
U = 고유 제품 수 → 정렬이 O(U log U)

Time: O(P + F·Q + U log U)
Space: O(P + U)
"""
def getPurchases(person):
    return []

def getFriends(person):
    return []

def itemsFriendsPurchases(person):
    already_bought = set(getPurchases(person))
    
    counts = Counter()
    for friend in getFriends(person):
        for product in getPurchases(friend):
            if product not in already_bought:
                counts[product] += 1
                
    return [product for product, _ in counts.most_common()]
