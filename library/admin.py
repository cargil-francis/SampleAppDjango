from django.contrib import admin

# Register your models here.
from django.contrib import admin
from .models import Book,Author

@admin.register(Book)
class BookAdmin(admin.ModelAdmin):
    list_display = ('Title', 'Author','Summary','Published_date')


@admin.register(Author)
class AuthorAdmin(admin.ModelAdmin):
    list_display = ('Name', 'Age')
