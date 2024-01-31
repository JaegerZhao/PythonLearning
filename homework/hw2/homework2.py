'''
给定整数数组 nums 和整数 k，请返回数组中第 k 个最大的元素。
请注意，你需要找的是数组排序后的第 k 个最大的元素，而不是第 k 个不同的元素。
注意时间复杂度
提示：可以使用快速排序
测试数据：
nums = [3,2,1,5,6,4]
k = 2
'''
def find_k_max(nums,k):
    if(k > 0 and k <= len(nums)):
        sorted_nums = sorted(nums)
        return sorted_nums [-k]
    else:
        print("erro")
        return -1

nums =  [3,2,1,5,6,4]
k = 2
find_k_max(nums,k)