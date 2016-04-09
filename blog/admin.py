from django.contrib import admin
from .models import Post            # importujemy (dołączamy) model Post

# Register your models here.

admin.site.register(Post)       # Aby nasz model był widoczny w panelu admina, musimy go zarejestrować za pomocą tego polecenia
