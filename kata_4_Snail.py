def snail(snail_map):
    if snail_map == [[]]:
        return []
    elif len(snail_map) == 1:
        return snail_map[0]

    i = 0
    j = 0
    rounder = 0
    lst_to_return = []
    mode = '→'
    all_taken = []
    while True:
        lst_to_return.append(snail_map[j][i])
        all_taken.append((i, j))
        if mode == '→':
            i += 1
            if i == len(snail_map) - 1 - rounder:
                mode = '↓'
        elif mode == '↓':
            j += 1
            if j == len(snail_map) - 1 - rounder:
                mode = '←'
        elif mode == '←':
            i -= 1
            if i == rounder:
                mode = '↑'
                rounder += 1
        elif mode == '↑':
            j -= 1
            if j == rounder:
                mode = '←'
                mode = '→'
        if (i, j) in all_taken:
            return lst_to_return

