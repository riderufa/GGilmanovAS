from django.shortcuts import render, redirect
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.views.generic.detail import DetailView
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy
from django.contrib.auth import login, authenticate
from django.contrib.auth.forms import UserCreationForm

from .models import Animal, KindOfAnimal
from .forms import *

# Create your views here.

class RegisterView(CreateView):
    form_class = UserCreationForm

    def form_valid(self, form):  
        form.save()  
        username = form.cleaned_data.get('username')  
        raw_password = form.cleaned_data.get('password1')  
        login(self.request, authenticate(username=username, password=raw_password))  
        return super(RegisterView, self).form_valid(form)  



def signup(request):
    if request.method == 'POST':
        form = SignupForm(request.POST)
        if form.is_valid():
            form.save()
        username = form.cleaned_data.get('username')
        my_password = form.cleaned_data.get('password1')
        user = authenticate(username=username, password=my_password)
        login(request, user)
        return redirect('index')
    else:
        form = SignupForm()
        return render(request, 'register.html', {'form': form})

# @login_required
def animals_list(request):
    animals = Animal.objects.all()
    kindsofanimal = KindOfAnimal.objects.all()
    return render(request, 'shelter/index.html', context={'animals': animals, 'kindsofanimal': kindsofanimal})

def animals_list_kind(request, pk):
    animals = Animal.objects.filter(kindofanimal__pk=pk)
    kindsofanimal = KindOfAnimal.objects.exclude(pk=pk)
    return render(request, 'shelter/index.html', context={'animals': animals, 'kindsofanimal': kindsofanimal})


# def animal_detail(request, animal_id):
#     animal = Animal.objects.get(id=animal_id)
#     return render(request, 'shelter/animal_detail.html', context={'animal': animal})

class AnimalDetailView(DetailView):
    model = Animal

class CreateAnimal(LoginRequiredMixin, CreateView):
    template_name = 'shelter/create_animal.html'
    form_class = AnimalForm
    success_url = reverse_lazy('index')

class CreateKindOfAnimal(LoginRequiredMixin, CreateView):
    template_name = 'shelter/create_kind_of_animal.html'
    form_class = KindOfAnimalForm
    success_url = reverse_lazy('index')

class EditAnimal(LoginRequiredMixin, UpdateView):
    template_name = 'shelter/edit_animal.html'
    model = Animal
    form_class = AnimalForm
    success_url = reverse_lazy('index')

class DeleteAnimal(LoginRequiredMixin, DeleteView):
    template_name = 'shelter/delete_animal.html'
    model = Animal
    success_url = reverse_lazy('index')


class EditKindOfAnimal(LoginRequiredMixin, UpdateView):
    template_name = 'shelter/edit_kind_of_animal.html'
    form_class = KindOfAnimalForm
    success_url = reverse_lazy('index')