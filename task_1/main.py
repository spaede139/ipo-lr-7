print("start code")
books=[]
for i in range(5):
    print(f"------------Книга {i+1}------------")
    title = input("введите название книги :")
    author = input("введите имя автора :")
    year = input("введите год издания :")
    book={
        "title":title,
        "author":author,
        "year":year
    }
    books.append(book)
for i ,book in enumerate(books,1):
    print(f"{"-"*21}Книга :{i}{"-"*21}")
    print(f" Название: {book['title']}, Автор: {book['author']},")
    print(f" {'-'*24}{book['year']}{'-'*24}")