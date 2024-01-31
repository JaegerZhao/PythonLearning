def megre_list(list1, list2):
    #初始索引
    index1 = 0
    index2 = 0
    #获取列表长度
    lens1 = len(list1)
    lens2 = len(list2)
    new_list = []
    #遍历两个列表
    while index1 < lens1 and index2 < lens2:
        v1 = list1[index1]
        v2 = list2[index2]
        #对元素进行比较,谁小插入谁
        if v1 <= v2:
            new_list.append(v1)
            index1 += 1
        else:
            new_list.append(v2)
            index2 += 1
    #处理l1中剩余元素
    if index1 < lens1:
        new_list.extend(list1[index1:])
    #处理l2中剩余元素
    if index2 < lens2:
        new_list.extend(list2[index2:])
    return new_list
if __name__ == "__main__":
    l1 = [-1, 1,2,3,3]
    l2 = [0,1,2,2]
    res = megre_list(l1, l2)
    print(res)