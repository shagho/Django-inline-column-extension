# Django inline column extension

It's a django package that you can use in django inline admin for pagination and sorting columns like change list page.


## How to use this?
First add *inline_admin_extensions* to your django apps:
```python
INSTALLED_APPS = [
    '...',
    'inline_admin_extensions',
    '...',
]
```

then  define your models:
```python
#models.py
from  django.db  import  models

  
  
class  Author(models.Model):
	name  =  models.CharField(max_length=100)

class  Book(models.Model):
	author  =  models.ForeignKey(Author, on_delete=models.CASCADE)
	title  =  models.CharField(max_length=100)
	isbn  =  models.CharField(max_length=100)
```
then in your **admin.py**:
```python
#admin.py
from  django.contrib import admin

from  inline_admin_extensions.admin import PaginationInline
from  inlineadmin.models import Author, Book

  
class  BookInline(PaginationInline):
	model  =  Book
	per_page  =  5


@admin.register(Author)
class  AuthorAdmin(admin.ModelAdmin):
	inlines  = [BookInline]
```

you see like this:
![screenshot](https://raw.githubusercontent.com/shagho/Django-inline-column-extension/master/pics/1.png)
![screenshot](https://raw.githubusercontent.com/shagho/Django-inline-column-extension/master/pics/2.png)
![screenshot](https://raw.githubusercontent.com/shagho/Django-inline-column-extension/master/pics/3.png)