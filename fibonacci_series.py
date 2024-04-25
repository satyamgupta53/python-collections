def fib(n) -> list[int]:
    li = [1, 1]
    for i in range(2, n):
        li.append(li[i-1] + li[i-2])
    return li

def pattern_rev(li) -> None:
    for i in reversed(li):
        for j in range(i):
            print("*", end=" ")
        print()

if __name__ == "__main__":
    n = int(input("Enter the number of terms: "))
    pattern_rev(fib(n))
        
