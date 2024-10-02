books = input().split(',')
print(len(books)//2)

notreturn = 0


for i in range(len(books)):
    if list(books[i])[-1] == '*' and list(books[i])[-2] == '*':
        notreturn += 1
        
print((len(books)//2) - notreturn )
print(notreturn)

bookslate = 0
booksfine = 0

for m in range(len(books)):
    if books[m] == 0:
        books.remove(books[m])

for e in range(len(books)//2):
    if list(books[e + (len(books)//2)])[-1] == '*' and list(books[e + (len(books)//2)])[-2] == '*':
        e = 0
    elif int(''.join(list(books[e])[7:])) - int(''.join(list(books[e+(len(books)//2)])[7:])) < 0:
        bookslate += 1
        booksfine += int(''.join(list(books[e+(len(books)//2)])[7:])) - int(''.join(list(books[e])[7:]))
print(bookslate)
print(booksfine*2)