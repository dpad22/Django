from django.shortcuts import render, redirect, HttpResponse
from .models import Book, Author


# Create your views here.
def index(request):
    context = {
        "all_books": Book.objects.all(),
        "all_authors": Author.objects.all()
    }
    return render(request, "book_author.html", context)

def authors (request):
    context = {
        "all_books": Book.objects.all(),
        "all_authors": Author.objects.all()
    }
    return render(request, "author_HP.html", context)

def view_book(request, book_id):
    # Book.objects.create(title = new_title)
    bookToShow = Book.objects.get(id = book_id)
    getAuthors = Author.objects.filter(books = book_id)
    remainingAuthors = Author.objects.exclude(books = book_id)
    print(bookToShow)
    print("*******")
    print(getAuthors)
    print("*******")
    print(remainingAuthors)
    context = {
        'bookInfo': bookToShow,
        'authorInfo': getAuthors,
        'remainingAuthors': remainingAuthors
    }
    return render(request,"showBook.html",context)

def view_author(request, author_id):
    authorToShow = Author.objects.get(id = author_id)
    getBooks = Book.objects.filter(authors = author_id)
    remaining_books = Book.objects.exclude(authors = author_id)
    print(authorToShow)
    print(getBooks)
    print(remaining_books)
    context = {
        'authors': authorToShow,
        'books': getBooks,
        'remaining_books': remaining_books
    }
    return render(request,"showAuthor.html",context)

def add_book(request):
    request.POST
    newBook = Book.objects.create(title = request.POST['newBook'] , description = request.POST['newDescription'])
    return redirect('/')

def createAuthor(request):
    request.POST
    newAuthor = Author.objects.create(first_name = request.POST['fname'], last_name = request.POST['lname'], notes = request.POST['notes'])
    return redirect('/authors')


def add_author(request, book_id):
    (request.POST['addAuthor'])
    print(request.POST['addAuthor'])
    author = Author.objects.get(id = request.POST['addAuthor'])
    book = Book.objects.get(id = book_id) 
    # join book and author
    author.books.add(book)
    return redirect(f'/book/{book_id}')

def join_book(request, author_id):
    join_author = Author.objects.get(id = author_id)
    join_book = Book.objects.get(id = request.POST['join_book'])
    join_book.authors.add(join_author)
    return redirect(f'/author/{author_id}')
