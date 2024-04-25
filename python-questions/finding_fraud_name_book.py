# Description: This program is to find the fake name of the book. The program takes the name of the book and the array of characters. The program will return the fake name of the book by replacing the characters in the book name with the characters in the array. If the character in the book name is present in the array, then it will be replaced with the other character in the array. If the character is not present in the array, then it will be as it is.

def fake_name(book_name, arr) -> str:
    book_name = book_name.lower()
    for i in arr:   
        temp = ""   
        for j in book_name:
            if (j == i[0]):
                temp += i[1]
            elif (j == i[1]):
                temp += i[0]
            else:
                temp += j
        book_name = temp
    return book_name
                
if __name__ == '__main__':
    book_name = input().strip()
    arr_rows = int(input().strip())
    arr_cols = int(input().strip())
    arr = []

    for _ in range(arr_rows):
        arr.append(list(map(lambda x: x[0], input().rstrip().split())))
        
    result = fake_name(book_name, arr)
    print(result)

