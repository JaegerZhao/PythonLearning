def inser_x(nums, x):
    #列表不为空
    if nums:
        #x大于nums中的最大值
        if nums[-1] <= x:
            nums.append(x)
        else:
            for index, val in enumerate(nums):
                if x < val:
                    nums.insert(index, val)
                    #插入之后必须调用break
                    break
    else:
        #列表为空，直接插入x
        nums.append(x)
nums = [1,2,4,4]
print('插入前：', nums)
inser_x(nums, 3)
print('插入后：', nums)