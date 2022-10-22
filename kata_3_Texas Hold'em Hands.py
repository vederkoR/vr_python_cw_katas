from collections import Counter


def back_converter(cards_lsd):
    lst_to_return = []
    for rank in cards_lsd:
        if int(rank) in range(2, 11):
            lst_to_return.append(rank)
        elif rank == '11':
            lst_to_return.append("J")
        elif rank == '12':
            lst_to_return.append("Q")
        elif rank == '13':
            lst_to_return.append("K")
        else:
            lst_to_return.append("A")
    return lst_to_return


def straight_check(cards):
    safe_copy = sorted(list(set(cards)), key=lambda i: int(i), reverse=True)
    inc_list = [int(i) + j for i, j in zip(safe_copy, range(0, 7))]
    consecutives = sorted([f"{j}:{i}" for i, j in Counter(inc_list).items()], reverse=True)
    if int(consecutives[0][0]) < 5:
        return False
    else:
        highest = int(consecutives[0][2:]) - inc_list.index(int(consecutives[0][2:]))
        return back_converter([str(i) for i in list(reversed(range(highest - 4, highest + 1)))])


def flushes_check(cards):
    suit_list = sorted([f"{j}:{i}" for i, j in Counter([i[-1] for i in cards]).items()], reverse=True)
    suit = suit_list[0][-1]
    cards_with_suit = [i[0:-1] for i in cards if i[-1] == suit]
    if len(cards_with_suit) < 5:
        return False
    elif straight_check(cards_with_suit):
        return "straight-flush", straight_check(cards_with_suit)
    else:
        return "flush", back_converter(cards_with_suit[:5])


def kind_check(cards):
    combination = sorted([f"{j}:{i}" for i, j in Counter(cards).items()], key=lambda x: (int(x[0]), int(x[2:])),
                         reverse=True)
    cards_to_return = []
    counter = 0
    inx = 0
    while counter < 5:
        cards_to_return.append(combination[inx][2:])
        counter += int(combination[inx][0])
        inx += 1

    if combination[0][0] == '4':
        return "four-of-a-kind", back_converter(cards_to_return)
    elif combination[0][0] == '3' and int(combination[1][0]) >= 2:
        return "full house", back_converter(cards_to_return)
    elif combination[0][0] == '3':
        return "three-of-a-kind", back_converter(cards_to_return)
    elif combination[0][0] == combination[1][0] == '2':
        return "two pair", back_converter(cards_to_return)
    elif combination[0][0] == '2':
        return "pair", back_converter(cards_to_return)
    else:
        return "nothing", back_converter(cards_to_return)


def hand(hole_cards, community_cards):
    all_cards = hole_cards + community_cards
    all_cards_numeric = sorted([i.replace("J", "11").replace("Q", "12").replace("K", "13").replace("A", "14") for i in
                                all_cards], key=lambda i: int(i[0: -1]), reverse=True)
    flushes = flushes_check(all_cards_numeric)
    cards_numeric = [i[0:-1] for i in all_cards_numeric]
    kind = kind_check(cards_numeric)
    straight = straight_check(cards_numeric)
    if flushes and flushes[0] == "straight-flush":
        return flushes
    elif kind[0] == "four-of-a-kind" or kind[0] == "full house":
        return kind
    elif flushes and flushes[0] == "flush":
        return flushes
    elif straight:
        return "straight", straight
    else:
        return kind


