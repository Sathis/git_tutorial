def intersection(lst1, lst2):
    return list(set(lst1) & set(lst2))

dict = {100: [6001, 6005], 101: [6005, 6001, 6007], 102: [6005, 6007]}
origin_dest = {}
for key in dict:
    for key1 in dict:
        if (key == key1):
            continue
        origin_dest.ke
        origin_dest[tuple((key, key1))] = intersection(dict[key], dict[key1])

print(origin_dest)
