from django.shortcuts import render

# Create your views here.

# tworzymy metodę (def) zwaną post_list, która przyjmuje zapytanie (request) i zwraca (return)
# metodę zwaną render, której zadaniem jest wyrenderowanie (złożenie w całość) naszego szablonu blog/post_list.html.
def post_list(request):
    return render (request, 'blog/post_list.html', {})
