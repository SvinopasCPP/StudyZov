str1 = input()
list1 = list(map(int,str1.split()))
def sorting(A):
    for i in range(1,len(A)):
        b = A[i]
        j = i - 1
        while j >= 0 and A[j] > b:
            A[j+1] = A[j]
            j -= 1
        A[j+1] = b
    return A
result = sorting(list1)
print(result)
