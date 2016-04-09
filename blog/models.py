from django.db import models
from django.utils import timezone

# Create your models here.

#definiujemy model, class - tworzymy obiekt, Post - nazwa modelu (zawsze wielka),
# models.Model ozn., że nasz obiekt Post jest modelem Django - Django wie, że przechowywać go w bazie danych
class Post(models.Model):
    author = models.ForeignKey('auth.User')         # models.ForeignKey - odnośnik do innego modelu
    title = models.CharField(max_length=200)
    text = models.TextField()
    created_date = models.DateTimeField(default=timezone.now)
    publish_date = models.DateTimeField(blank=True, null=True)

    def publish(self):                          # metoda publikujaca wpis
        self.published_date = timezone.now()
        self.save()

    def __str__(self):              #wywolujac te metode otrzymamy string - tytul wpisu
        return self.title
