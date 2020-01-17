from django.urls import path

from .views import *

urlpatterns = [
    path('', animals_list, name='index'),
    path('<int:pk>', animals_list_kind, name='index_kindofanimal'),
    path('add/animal/', CreateAnimal.as_view(), name='add_animal'),
    path('add/kindofanimal/', CreateKindOfAnimal.as_view(), name='add_kind_of_animal'),
    path('edit/animal/<int:pk>', EditAnimal.as_view(), name='edit_animal'),
    path('delete/animal/<int:pk>', DeleteAnimal.as_view(), name='delete_animal'),
    path('edit/kindofanimal/', EditKindOfAnimal.as_view(), name='edit_kind_of_animal'),
    path('animal/<int:pk>/', AnimalDetailView.as_view(), name='animal_detail'),
]

