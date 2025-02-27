def binary_search(a, elem_b, n):
    if elem_b <= a[0]:
        return 0
    
    high = 1 
    while (high < n) and (elem_b > a[high]) :
        high *= 2

    high = min(high, n)
    low = high // 2

    while low < high:
        middle = (high + low)//2
        if elem_b == a[middle]:
            return middle
        if elem_b < a[middle]:
            high = middle
        else: 
            low = middle + 1
    return low

                
n, m = map(int, input().split())
a = list(map(int, input().split()))
b = list(map(int, input().split()))

ans = []
for i in range(m):
    ans.append(str(binary_search(a, b[i], n)))
print(" ".join(ans))

