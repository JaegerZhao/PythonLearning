def decompress_list(nums):
    lens = len(nums)
    i = 0
    new_list = []
    while i < lens:
        #后一个字符出现频次
        freq = nums[i]
        #后一个字符
        val = nums[i+1]
        #索引加2
        i += 2
        #将元素解压，添加到新的列表中
        new_list.extend([val] * freq)
    return new_list

if __name__ == "__main__":
    nums = [1,2,3,4,5,'c']
    res = decompress_list(nums)
    print(res)