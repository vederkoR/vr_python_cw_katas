def spiralize(size):
    matrix = [size * [0] for i in range(size)]
    i = 0
    j = 0
    lock = (j, i)
    counter = 0
    mode = '→'
    while True:
        if mode == '→':
            if (i > size - 3) or (matrix[j][i + 2] == 0):
                matrix[j][i] = 1
                lock = (j, i)
                i += 1
            if size - 3 < i < size - 1:
                continue
            if (i == size - 1) or (matrix[j][i + 2] == 1):
                mode = '↓'
        elif mode == '↓':
            if (j > size - 3) or (matrix[j + 2][i] == 0):
                matrix[j][i] = 1
                lock = (j, i)
                j += 1
            if size - 3 < j < size - 1:
                continue
            if (j == size - 1) or (matrix[j + 2][i] == 1):
                mode = '←'
        elif mode == '←':
            if (i < 2) or (matrix[j][i - 2] == 0):
                matrix[j][i] = 1
                lock = (j, i)
                i -= 1
            if 0 < i < 2:
                continue
            if (i == 0) or (matrix[j][i - 2] == 1):
                mode = '↑'
        elif mode == '↑':
            if (j < 2) or (matrix[j - 2][i] == 0):
                matrix[j][i] = 1
                lock = (j, i)
                j -= 1
            # logic here
            if (j == 0) or (matrix[j - 2][i] == 1):
                mode = '→'
        counter += 1
        if counter > size ** 2:
            if size % 2 == 0:
                matrix[lock[0]][lock[1]] = 0
            else:
                matrix[j][i] = 1

            return matrix


