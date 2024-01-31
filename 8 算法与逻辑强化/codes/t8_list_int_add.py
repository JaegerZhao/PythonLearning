def list_add(num1, num2):
    lens1 = len(num1)
    lens2 = len(num2)
    #进位处理
    carry = 0
    res = []
    #获取两个列表最小长度
    min_index = min(lens1, lens2) * -1
    #从最后一个开始计算
    i = -1
    while i >= min_index:
        #计算当前两位+进位尾
        v = num1[i] + num2[i] + carry
        #如果当前和大于10，产生进位，并将个位插入列表
        if v >= 10:
            carry = 1
            res.insert(0, v - 10)
        else:
            #没有进位，直接将个位插入列表
            carry = 0
            res.insert(0, v)
        #计算下一位
        i -= 1
    #若两个数位数不同，继续处理高位
    if lens1 != lens2:
        if lens1 > lens2:
            last_list = num1
            min_index = lens1*-1
        else:
            last_list = num2
            min_index = lens2*-1
        #使用-索引处理，此处可以修正，使用正索引处理
        while i >= min_index:
            #重复上一操作，处理进位
            v = last_list[i]+ carry
            if v >= 10:
                carry = 1
                res.insert(0, v - 10)
            else:
                carry = 0
                res.insert(0, v)
            i-=1
    #如果最后一位有进位，将进位插入到列表首
    if carry:
        res.insert(0, carry)     
        
    return res
if __name__ == '__main__':
    num1 = [1,2,3]
    num2 = [2,8,9]
    res = list_add(num1, num2)
    print(res)