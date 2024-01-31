def my_reverse(lists):
    
    start = 0
    end = len(lists)-1
    
    while start < end:
        #列表前后调换位置
        lists[start], lists[end] = lists[end], lists[start]
        #前索引加1
        start += 1
        #后索引减1
        end -= 1
        
l = list('abcdefg')
print(l)
my_reverse(l)
print(l)