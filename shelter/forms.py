from django.forms import ModelForm
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

from .models import *

class AnimalForm(ModelForm):
    class Meta:
        model = Animal
        fields = ('name', 'sex', 'color', 'age', 'breed', 'description', 'kindofanimal', 'image')

class KindOfAnimalForm(ModelForm):
    class Meta:
        model = KindOfAnimal
        fields = (
            'title',
        )

class SignupForm(UserCreationForm):
    email = models.EmailField(max_length=254, help_text='Это поле обязательно')

    class Meta:
        model = User
        fields = ('username', 'email', 'password1', 'password2')