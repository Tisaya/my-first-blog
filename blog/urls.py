from django.conf.urls import url    # importujemy metody Django
from . import views                 # importujemy widoki z aplikacji blog

urlpatterns = [
    url(r'^$', views.post_list, name='post_list'),
    url(r'^post/(?P<pk>[0-9]+)/$', views.post_detail, name='post_detail'),
]
