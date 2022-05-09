def flatten(items, seqtypes=(list, tuple)):
    for i, x in enumerate(items):
        while i < len(items) and isinstance(items[i], seqtypes):
            items[i:i+1] = items[i]
    return items

print(flatten([[1,'a',['cat'],2],[[[3]],'dog'],4,5]))


def deep_reverse(mylist):
    result = []
    for e in mylist:
        if isinstance(e, list):
            result.append(deep_reverse(e))
        else:
            result.append(e)
    result.reverse()
    return result


print(deep_reverse([[1, 2], [3, 4], [[8]], [5, 6, 7]]))

a = [[1, 2], [3, 4], [[8]], [5, 6, 7]]

b = a[::-1]
print(b)

