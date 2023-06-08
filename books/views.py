from django.shortcuts import render
from .models import Book
import random

# Create your views here.

def book_list(request):
    return render(request, 'books/books.html')

def ti1(request):
    return render(request, 'books/TI1.html')

def ti2(request):
    return render(request, 'books/TI2.html')

def ti3(request):
    return render(request, 'books/TI3.html')

def tigame(request):
    request.session['played_iliad'] = True
    return render(request, 'books/TIgame.html')

def game_view(request):
    context = {'played_iliad': True}  
    return render(request, 'TIgame.html', context)

def pap1(request):
    return render(request, 'books/PAP1.html')

def pap2(request):
    return render(request, 'books/PAP2.html')

def pap3(request):
    return render(request, 'books/PAP3.html')

def papgame(request):
    request.session['played_pride_and_prejudice'] = True
    return render(request, 'books/PAPgame.html')

def ttm1(request):
    return render(request, 'books/TTM1.html')

def ttm2(request):
    return render(request, 'books/TTM2.html')

def ttm3(request):
    return render(request, 'books/TTM3.html')

def ttmgame(request):
    request.session['played_three_musketeers'] = True
    return render(request, 'books/TTMgame.html')

def wap1(request):
    return render(request, 'books/WAP1.html')

def wap2(request):
    return render(request, 'books/WAP2.html')

def wap3(request):
    return render(request, 'books/WAP3.html')

def wapgame(request):
    request.session['played_war_and_peace'] = True
    return render(request, 'books/WAPgame.html')

def thtb1(request):
    return render(request, 'books/THTB1.html')

def thtb2(request):
    return render(request, 'books/THTB2.html')

def thtb3(request):
    return render(request, 'books/THTB3.html')

def thtbgame(request):
    request.session['played_hound_baskervilles'] = True
    return render(request, 'books/THTBgame.html')

    

def recommend(request):
    if request.method == 'POST':
        # Extract the form data
        user_genre = request.POST['genre']
        user_difficulty = request.POST['difficulty']

        # Get all books
        all_books = Book.objects.all()

        # Define weights for genre and difficulty
        weight_genre = 0.56
        weight_difficulty = 0.44

        # Initialize empty lists for perfect fit books and filtered books
        perfect_fit_books = []
        filtered_books = []

        # Go over each book
        for book in all_books:
            # Check if the book matches both genre and difficulty
            if book.genre == user_genre and book.difficulty == user_difficulty:
                perfect_fit_books.append(book)
            else:
                # Calculate weighted score based on genre and difficulty
                genre_score = 1 if book.genre == user_genre else 0
                difficulty_score = 1 if book.difficulty == user_difficulty else 0
                weighted_score = genre_score * weight_genre + difficulty_score * weight_difficulty

                # Check if the weighted score meets the criteria
                if weighted_score >= weight_genre:
                    filtered_books.append((book, weighted_score))

        # Check if any perfect fit books were found
        if perfect_fit_books:
            # Randomly select a perfect fit book
            recommended_book = random.choice(perfect_fit_books)
        else:
            # Check if any filtered books were found
            if filtered_books:
                # Sort the filtered books by weighted score in descending order
                filtered_books.sort(key=lambda x: x[1], reverse=True)

                # Randomly select a book from the top-rated books
                recommended_book = random.choice(filtered_books[:5])[0]
            else:
                recommended_book = None

        # Render the recommendation page with the recommended book
        return render(request, 'books/recommendation.html', {'book': recommended_book})

