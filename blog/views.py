from django.shortcuts import render
from django.utils import timezone   # importujemy dla funkcji timezone.now()
from .models import Post        # dołaczamy model napisany w models.py

# Create your views here.

# tworzymy metodę (def) zwaną post_list, która przyjmuje zapytanie (request) i zwraca (return)
# metodę zwaną render, której zadaniem jest wyrenderowanie (złożenie w całość) naszego szablonu blog/post_list.html.
def post_list(request):
    posts = Post.objects.filter(published_date__lte=timezone.now()).order_by('published_date')  # tworzymy zmienna posts dla QuerySetu
    return render (request, 'blog/post_list.html', {'posts': posts})
