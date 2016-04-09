from django.conf.urls import url    # importujemy metody Django
from . import views                 # importujemy widoki z aplikacji blog

urlpatterns = [
    url(r'^$', views.post_list, name='post_list'),
]
