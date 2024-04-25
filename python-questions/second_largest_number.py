import sys
def second_largest(li) -> int:
    max_num, second_max = - sys.maxsize, - sys.maxsize
    for i in range(len(li)):
        if li[i] > max_num: 
            second_max = max_num
            max_num = li[i]
        elif li[i] > second_max and li[i] < max_num:
            second_max = li[i]
    return second_max , max_num

if __name__ == '__main__':
    li = [1, 8, 4, 5, 6, 7, 2, 3, 11, 4, 13]
    print(second_largest(li))