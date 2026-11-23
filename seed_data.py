from django.core.management.base import BaseCommand
from catalog.models import Author, Genre, Language, Book, BookInstance


class Command(BaseCommand):
    help = "Create sample LocalLibrary authors, genres, languages, books and copies."

    def handle(self, *args, **options):
        fantasy, _ = Genre.objects.get_or_create(name="Fantasy")
        science, _ = Genre.objects.get_or_create(name="Science Fiction")
        history, _ = Genre.objects.get_or_create(name="Historical")
        english, _ = Language.objects.get_or_create(name="English")
        ukrainian, _ = Language.objects.get_or_create(name="Ukrainian")

        rowling, _ = Author.objects.get_or_create(
            first_name="Joanne", last_name="Rowling",
            defaults={"date_of_birth": "1965-07-31"},
        )
        asimov, _ = Author.objects.get_or_create(
            first_name="Isaac", last_name="Asimov",
            defaults={"date_of_birth": "1920-01-02", "date_of_death": "1992-04-06"},
        )
        shevchenko, _ = Author.objects.get_or_create(
            first_name="Taras", last_name="Shevchenko",
            defaults={"date_of_birth": "1814-03-09", "date_of_death": "1861-03-10"},
        )

        books = [
            ("Harry Potter and the Philosopher's Stone", rowling, "A young wizard begins his education at Hogwarts.", "9780747532699", english, [fantasy]),
            ("Harry Potter and the Chamber of Secrets", rowling, "The second adventure at Hogwarts.", "9780747538493", english, [fantasy]),
            ("Foundation", asimov, "A science fiction story about a declining galactic empire.", "9780553293357", english, [science]),
            ("I, Robot", asimov, "A collection of stories about robots and humanity.", "9780553382563", english, [science]),
            ("Kobzar", shevchenko, "A collection of poetry by Taras Shevchenko.", "9789660345123", ukrainian, [history]),
        ]
        for title, author, summary, isbn, language, genres in books:
            book, created = Book.objects.get_or_create(
                title=title,
                defaults={"author": author, "summary": summary, "isbn": isbn, "language": language},
            )
            book.genre.set(genres)
            for number, status in enumerate(("a", "o"), start=1):
                BookInstance.objects.get_or_create(
                    book=book,
                    imprint=f"Library edition #{number}",
                    defaults={"status": status},
                )

        self.stdout.write(self.style.SUCCESS("Sample LocalLibrary data is ready."))
