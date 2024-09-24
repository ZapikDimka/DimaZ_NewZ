from django.contrib import admin
from .models import Author, News

# Register the Author model in the admin panel
admin.site.register(Author)

# Register the News model in the admin panel
admin.site.register(News)
