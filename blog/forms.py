from django import forms        # importowanie formularzy django
from .models import Post        # import modelu wpisu

class PostForm(forms.ModelForm):        # PostForm - nazwa formularza, ModelForm - formularz modelu

    class Meta:
        model = Post        # przekazujemy django inf, jaki model wykorzystujemy do stworzenia formularza
        fields = ('title', 'text',)   # wskazujemy, jakie pola pojawiają się w formularzu  
