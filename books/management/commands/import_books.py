from django.core.management.base import BaseCommand
from books.models import Book
import csv
import os

class Command(BaseCommand):
    help = 'Loads data from BookData.csv into Book model'

    def handle(self, *args, **options):
        with open('BookData.csv', newline='', encoding='utf-8') as csvfile:
            reader = csv.DictReader(csvfile)
            for row in reader:
                book = Book()
                book.title = row['Title']
                book.author = row['Author']
                book.genre = row['Genre']
                book.year_written = row['Year Written']
                book.gutenberg_id = row['Gutenberg ID']
                book.flesch_kincaid_score = row['Flesch-Kincaid Score']
                book.difficulty = row['Difficulty']
                book.save()
