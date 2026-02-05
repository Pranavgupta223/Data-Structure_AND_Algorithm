n = int(input('enter lenght of array: '))
arr = []
for i in range(n):
    x = int(input(f'enter {i} number of array'))
    arr.append(x)

print(f'Given array-> {arr}')

k = int(input('Enter K value : '))
print(f"Given K value {k}")

def reverse(l,r):
    while l<r:
        arr[l],arr[r] = arr[r],arr[l]
        l += 1
        r -= 1
    return arr

reverse(0,n-1)
reverse(0,k-1)
reverse(k,n-1)

print(f"After reversing {k} values\nArray became -> {arr}")


