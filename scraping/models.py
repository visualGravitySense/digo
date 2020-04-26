from django.db import models

class City(models.Model):
    name = models.name = models.CharField(max_length=50, verbose_name='Город')

    def __str__(self):
            return self.name
"""
        super(, self).__init__()
        self.arg = arg
        """

class Vacancy(models.Model):
    url = models.CharField(max_length=250, unique=True, verbose_name='Адрес вакансии')
    title = models.CharField(max_length=250, unique=True, verbose_name='Заголовок вакансии')
    description = models.TextField(blank=True, verbose_name='Описание вакансии')
    company = models.TextField(max_length=250, blank=True, verbose_name='Название компании')
#    city = models.TextField(max_length=250, blank=True, verbose_name='Город')
    city = models.name = models.ForeignKey(City, verbose_name='Город', on_delete=models.CASCADE)
    Speciality = models.TextField(max_length=250, blank=True, verbose_name='Специальность')
    timestamp = models.DateField(auto_now_add=True)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name='Вакансия'
        verbose_name_plural='Вакансии'
