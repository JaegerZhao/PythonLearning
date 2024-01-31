def integer_break(n):
    #1,2,3,4与对应值得映射
    n_map = {1:1,2:1,3:2, 4:4}
    val = n_map.get(n, 0)
    k = 0
    if not val:
        #对三求余
        tmp = n%3
        if tmp == 1:
            k = (n-4)//3
            tmp = 4
        elif tmp == 2:
            k = n//3
        else:
            k = n//3
            tmp = 1
        #计算结果
        val = pow(3, k) * tmp
    return val
    
if __name__ == '__main__':
    for n in [1,3,4,5,10,12,100]:
        print(n,integer_break(n))