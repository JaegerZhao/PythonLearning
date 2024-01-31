def count_teams(l):
    items = []
    for index,val in enumerate(l):
        #获取剩余列表元素，每个作为第二个元素
        sub_list = l[index+1:]
        for sub_index, sub_val in enumerate(sub_list):
            #将剩余列表元素作为第三个元素
            last_list = l[index+sub_index+2:]
            #根据v1,v2的大小关系，处理第三个元素
            #第一个元素大于第二个元素，则第二个必须大于第三个元素
            if val > sub_val:
                for last in last_list:
                    if sub_val>last:
                        print(val, sub_val, last)
                        items.append((val, sub_val, last))
            else:
                #第一个元素小于第二个元素，则第二个必须小于第三个元素
                for last in last_list:
                    if sub_val<last:
                        print(val, sub_val, last)
                        items.append((val, sub_val, last))
    return items
if __name__ == '__main__':
    l = [2,5,3,4,1]
    items = count_teams(l)
    for item in items:
        print(item)