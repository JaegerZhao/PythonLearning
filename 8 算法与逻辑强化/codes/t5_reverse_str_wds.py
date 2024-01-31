def my_reverse(lists):
    
    start = 0
    end = len(lists)-1
    
    while start < end:
        lists[start], lists[end] = lists[end], lists[start]
        start += 1
        end -= 1

def reverse_words(s):
    #切分字符串
    wds = s.split()
    #列表解析去多余字符串，
    wds = [wd for wd in wds if wd.strip()]
    #调用上一节翻转列表方式前后交换元素
    my_reverse(wds)
    #拼接单词
    return ' '.join(wds)

if __name__ == '__main__':
    #多个测试用例
    list_s = ["the sky is blue", "  hello world!  ","a good   example","  Bob    Loves  Alice   "]
    for s in list_s:
        print('[%s]->[%s]'%(s, reverse_words(s)))