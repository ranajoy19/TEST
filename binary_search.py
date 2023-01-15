card = [4,5,6,7,0,1,2]
card.sort()
query =10
output = 5
# binary search

def locate_cards(card,query):
    lb = 0
    ub = len(card) -1

    while (lb<=ub):
        mid_index = (lb +ub) //2
        if card[mid_index] == query:
            return mid_index
        elif card[mid_index]< query:
            lb = mid_index+1

        else:
            ub = mid_index-1

    return -1



print(card)
print(locate_cards(card,query))