def merge_list(intervals):
    if len(intervals)<=1:
            return intervals
    res=[]
    start = 0
    end = -1
    #将区间按照start进行排序
    intervals = sorted(intervals,key = lambda item: item[start])
    #新的列表区间，插入第一个区间
    res.append(intervals[0])
    #遍历剩余区间
    for i in range(1,len(intervals)):
        #如果前一区间与当前区间无交集，直接插入当前区间
        if res[-1][end] < intervals[i][start]:
            res.append(intervals[i])
        #如果前一区间与当前区间有交集，修改前一区间的end值
        elif intervals[i][end] > res[-1][end]:
            res[-1][end] = intervals[i][end]                          
    return res

if __name__ == '__main__':
    l = [[1,3],[2,6],[8,10],[15,18]]
    res = merge_list(l)
    print(res)