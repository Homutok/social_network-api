from django.db import models
from django_countries.fields import CountryField
from django.contrib.auth.models import User


# Create your models here.
class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='public_user_info')
    person_photo = models.ImageField(upload_to='article', height_field=None, width_field=None, max_length=100,
                                     null=True,
                                     blank=True)  # Фотография пользователя
    date_of_birth = models.DateField(null=True, blank=True)  # Дата рождения
    summary = models.CharField(max_length=1000, db_index=True, null=True)  # Информация о пользователе

    MALE = 'male'
    FEMALE = 'female'
    OTHER = 'other'

    GENDER_CHOICE = (
        (MALE, 'Мужчина'),
        (FEMALE, 'Женщина'),
        (OTHER, 'Другие'),
    )
    person_gender = models.CharField(max_length=50, choices=GENDER_CHOICE, blank=True, default='study',
                                     help_text='Половая '
                                               'принадлежность')

    country = CountryField()  # Страна проживания

    university = models.CharField(max_length=200, db_index=True, null=True,
                                  help_text='Место обучения')  # Университет пользователя

    group_of_study = models.CharField(max_length=200, db_index=True, null=True,
                                      help_text='Группа')  # Группа пользователя

    class Meta:
        ordering = ['user']

    def __str__(self):
        return str(self.user.username)
