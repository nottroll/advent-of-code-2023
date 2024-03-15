"""PART 1"""

suits = {'A':14,'K':13,'Q':12,'J':11,'T':10,'9':9,
         '8':8,'7':7,'6':6,'5':5,'4':4,'3':3,'2':2}

with open(r'day7.txt', 'r') as f:
    file = f.readlines()

    hands = [i.split()[0] for i in file]
    bids = [int(i.split()[1]) for i in file]

# print(hands, bids)

bins = [[] for _ in range(7)]

# five = []
# four = []
# full = []
# three = []
# two_pair = []
# one_pair = []
# high_card = []

for hand, bid in zip(hands,bids):
    cards = {}
    for i in range(len(hand)):
        if cards.get(hand[i]):
            cards[hand[i]] = cards.get(hand[i]) + 1
        else:
            cards[hand[i]] = 1

    # print(list(cards.values()))
    
    v = list(cards.values())
    if len(v) == 1:
        bins[6].append((hand, bid))
    elif 4 in v:
        bins[5].append((hand, bid))
    elif 3 in v:
        if len(v) == 2:
            bins[4].append((hand, bid))
        else:
            bins[3].append((hand, bid))
    elif 2 in v:
        if len(v) == 3:
            bins[2].append((hand, bid))
        else:
            bins[1].append((hand, bid))
    else:
        bins[0].append((hand, bid))

res = []
for bin in bins:
    s = sorted(bin, key=lambda pair: [suits.get(pair[0][i]) for i in range(5)])
    res.extend(s)
# print(res)

winnings = 0
for idx, game in enumerate(res):
    winnings += (idx + 1) * game[1]
print(winnings)

cards.clear()
res.clear()

"""PART 2"""

suits_2 = {'A':14,'K':13,'Q':12,'T':10,'9':9,
         '8':8,'7':7,'6':6,'5':5,'4':4,'3':3,'2':2,'J':1}

bins = [[] for _ in range(7)]

for hand, bid in zip(hands,bids):
    cards = {}
    for i in range(len(hand)):
        if cards.get(hand[i]):
            cards[hand[i]] = cards.get(hand[i]) + 1
        else:
            cards[hand[i]] = 1

    v = list(cards.values())

    if cards.get('J'):
        if len(v) == 1 or 4 in v: # (5) or (4,1)
            bins[6].append((hand, bid))
        elif 3 in v:  # (3,2) (3,1,1)
            if cards.get('J') == 3: 
                if len(v) == 2: # (J,J,J,2)
                    bins[6].append((hand, bid))
                if len(v) == 3: # (J,J,J,1,1)
                    bins[5].append((hand, bid))
            elif cards.get('J') == 2: # (3,J,J)
                bins[6].append((hand, bid))
            else: # (3,1,J)
                bins[5].append((hand, bid))

        elif 2 in v: # (2,2,1) (2,1,1,1)
            if cards.get('J') == 1: 
                if len(v) == 3: # (2,2,J)
                    bins[4].append((hand, bid))
                else: # (2,1,1,J)
                    bins[3].append((hand, bid))

            elif cards.get('J') == 2:
                if len(v) == 3: # (J,J,2,1)
                    bins[5].append((hand, bid))
                else: # (J,J,1,1,1)
                    bins[3].append((hand, bid))

        else: # (J,1,1,1,1)
            bins[1].append((hand, bid))
    else:
        if len(v) == 1:
            bins[6].append((hand, bid))
        elif 4 in v:
            bins[5].append((hand, bid))
        elif 3 in v:
            if len(v) == 2:
                bins[4].append((hand, bid))
            else:
                bins[3].append((hand, bid))
        elif 2 in v:
            if len(v) == 3:
                bins[2].append((hand, bid))
            else:
                bins[1].append((hand, bid))
        else:
            bins[0].append((hand, bid))

print(sorted(bins[5], key=lambda pair: [suits_2.get(pair[0][i]) for i in range(5)]))

res_2 = []
for bin in bins:
    s = sorted(bin, key=lambda pair: [suits_2.get(pair[0][i]) for i in range(5)])
    res_2.extend(s)
# print(res_2)

winnings = 0
for idx, game in enumerate(res_2):
    winnings += (idx + 1) * game[1]
print(winnings)