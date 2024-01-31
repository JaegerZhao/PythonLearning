from collections import Counter

def intersection_1(list1, list2):
    l1 = list(set(list1))
    l2 = list(set(list2))
    l1.extend(l2)
    r = Counter(l1)
    return [k for k in r if r[k] > 1]

def intersection_2(list1, list2):
    vals = []
    for val in list1:
        if val in list2 and val not in vals:
            vals.append(val)
    return vals
#测试1
list1 = [4,9,5]
list2 = [9,4,9,8,4]  
print(intersection_1(list1, list2))
print(intersection_2(list1, list2))
