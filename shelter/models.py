from django.db import models
from PIL import Image

# Create your models here.
class KindOfAnimal(models.Model):
    title = models.CharField(max_length=50)

    def __str__(self):
        return self.title


class Animal(models.Model):
    sex_choices = [
        ('M', 'male'),
        ('F', 'female'),
    ]
    name = models.CharField(max_length=50, verbose_name='Кличка')
    sex = models.CharField(max_length=1, choices=sex_choices, verbose_name='Пол')
    color = models.CharField(max_length=50, verbose_name='Цвет')
    age = models.SmallIntegerField(verbose_name='Возраст')
    breed = models.CharField(max_length=50, default='беспородный', verbose_name='Порода')
    description = models.TextField(verbose_name='Описание')
    receipted = models.DateTimeField(auto_now_add=True, db_index=True)
    kindofanimal = models.ForeignKey(KindOfAnimal, on_delete=models.PROTECT, related_name='animal', verbose_name='Вид животного')
    image = models.ImageField(upload_to='images/%Y/%m/%d', blank=True, verbose_name='Фотография')

    def __str__(self):
        return self.name

    # def get_absolute_url(self):
    #     return reverse('animal-detail', kwargs={'pk': self.pk})

    def save(self):
        super().save()
        
        if self.image:
            img = Image.open(self.image.path)
            if img.height > 100 or img.width > 100:
                output_size = (100, 100)
                img.thumbnail(output_size)
                img.save(self.image.path)