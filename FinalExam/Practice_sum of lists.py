def recursive_sum(ls):
    sum = 0
    i = 0
    while i < len(ls):
        if isinstance(ls[i], int):
            sum += ls[i]
        else:
            sum += recursive_sum(ls[i])
        i += 1
    return sum

def iterative_sum(ls):
    sum = 0
    i = 0
    while i < len(ls):
        if isinstance(ls[i], int):
            sum += ls[i]
        else:
            new_ls = ls[i]
            j = 0
            while j < len(new_ls):
                if isinstance(new_ls[j], int):
                    sum += new_ls[j]
                else:
                    new_ls = ls[j]
                j += 1
        i += 1



ls = [1, 2, [3, 4], [5, [[6, 7], 8]], 9]
print(recursive_sum(ls))    # 45
#print(iterative_sum(ls))    # 45