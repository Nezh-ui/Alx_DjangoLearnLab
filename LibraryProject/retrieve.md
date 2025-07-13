retrieved_book = Book.objects.get(title=book.title)
print(retrieved_book)
# Retrieves and displays attributes of the book i.e. title= 1984