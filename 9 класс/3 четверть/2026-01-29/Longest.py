def longest(s):
    p = s.split()
    return max(p , key = len)
s = input()
print(longest(s))
