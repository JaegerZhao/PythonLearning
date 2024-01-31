def reverse_left_words(s, k):
    lens = len(s)
    if k > 0 and k < lens:
        start = s[k:]
        end = s[:k]
        return start+end
    
s = "abcdefg"
k = 2
print(s, k)
res = reverse_left_words(s,k)
print(res)