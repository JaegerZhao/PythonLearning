def kth_factor_1(n,k):
    '''
    n:整数
    k:因子数量
    '''
    list_fac = []
    #从1开始遍历
    for i in range(1, n+1):
        if n % i == 0:
            list_fac.append(i)
    if len(list_fac) >= k:
        return list_fac, list_fac[k-1]

def kth_factor_2(n,k):
    list_fac =[]
    min_val, max_val = 1, n
    i = 0
    if n > 1:
        #左右最大与最小值
        while min_val < max_val:
            if n % min_val == 0:
                t = n // min_val
                #修改max_val
                max_val = t
                #如果大值与小值不等，插入最大值，例如100=10x10
                if max_val != min_val:
                    list_fac.insert(-1*i, t)
                #插入小的值
                list_fac.insert(i,min_val)
                i += 1
            #小的值每次加1
            min_val += 1
    else:
        list_fac.append(n)
        
    lens = len(list_fac)
    if lens >= k:
        return list_fac, list_fac[k-1]
    else:
        return list_fac, -1

if __name__ == '__main__':  
    print(kth_factor_1(10,2))
    print(kth_factor_1(100,2))
    print(kth_factor_2(100,3))