from django.contrib import admin

from inline_admin_extensions.admin import PaginationInline
from inlineadmin.models import Author, Book


class BookInline(PaginationInline):
    model = Book
    per_page = 5


@admin.register(Author)
class AuthorAdmin(admin.ModelAdmin):
    inlines = [BookInline]