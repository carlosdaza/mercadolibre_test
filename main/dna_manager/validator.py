def dna_validator(matrix):
    n = matrix.__len__()
    total_amount = 0
    if n < 4:
        return False
    if matrix[0] .__len__() != n:
        raise Exception('sample has different amount of rows than columns')
    else:
        row = ''
        other = dict()
        column = dict()
        for i in range(n):
            for j in range(n):
                if i not in other:
                    other[i] = {j: dict(dec=matrix[i][j], inc=matrix[i][j])}
                if j not in other[i]:
                    other[i][j] = dict(dec=matrix[i][j], inc=matrix[i][j])
                if j not in column:
                    column[j] = matrix[i][j]
                else:
                    column_size = column[j].__len__()
                    if n - i + column_size >= 4:
                        if matrix[i][j] not in column[j]:
                            column[j] = matrix[i][j]
                        else:
                            column[j] += matrix[i][j]
                        if column_size > 3:
                            total_amount += 1
                            column[j] = matrix[i][j]
                if i - 1 in other:
                    diagonal_size = column[j].__len__()
                    max_direction = max(i, j)
                    if n - max_direction + diagonal_size >= 4:
                        if j - 1 in other[i - 1]:
                            if matrix[i][j] not in other[i - 1][j - 1]['dec']:
                                other[i][j]['dec'] = matrix[i][j]
                            else:
                                other[i][j]['dec'] = other[i - 1][j - 1]['dec'] + matrix[i][j]
                            if other[i][j]['dec'].__len__() > 3:
                                total_amount += 1
                                other[i][j]['dec'] = matrix[i][j]
                        if j + 1 in other[i - 1]:
                            if matrix[i][j] not in other[i - 1][j + 1]['inc']:
                                other[i][j]['inc'] = matrix[i][j]
                            else:
                                other[i][j]['inc'] = other[i - 1][j + 1]['inc'] + matrix[i][j]
                            if other[i][j]['inc'].__len__() > 3:
                                total_amount += 1
                                other[i][j]['inc'] = matrix[i][j]
                row_size = row.__len__()
                if n - j + row_size >= 4:
                    if matrix[i][j] not in row:
                        row = matrix[i][j]
                    else:
                        row += matrix[i][j]
                    if row.__len__() > 3:
                        total_amount += 1
                        row = matrix[i][j]
            if total_amount > 1:
                break
        return total_amount > 1
