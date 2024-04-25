def filter_method(arr) -> list:
    arr1 = list(filter(lambda x: x % 2 == 0, arr))
    arr2 = list(filter(lambda x: x % 2 != 0, arr))
    arr1.extend(arr2)    
    return arr1

def two_pointer(arr) -> list:
    left , right = 0 , 1
    while left < len(arr) and right < len(arr):
        if arr[left] % 2 != 0 and arr[right] % 2 == 0:
            arr[left], arr[right] = arr[right], arr[left]
            left += 1
            right += 1
        elif arr[left] % 2 == 0:
            left += 1
        elif arr[right] % 2 != 0:
            right += 1 
    return arr
    
if __name__ == '__main__':
    arr = [4, 5, 6, 7, 2, 3, 11, 4, 13] 
    print(two_pointer(arr)) # Output: [4, 6, 2, 4, 5, 7, 3, 11, 13] arrange even in order before odd