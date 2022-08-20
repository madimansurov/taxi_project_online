from django.db import models

# Данные водителя и его автомобиля доступные для суперАдмина

class Driver(models.Model):
    name = models.CharField(max_length=100, verbose_name='ФИО водителя')
    identification_card = models.IntegerField(verbose_name='Удостоверение личности, №')
    driver_license = models.IntegerField(verbose_name='Водительское удостоверение')
    car_info = models.TextField(verbose_name='Марка, модель авто, год выпуска')
    car_number = models.CharField(max_length=8, verbose_name='Государственный номер автомобиля')

    def __str__(self):
        return f"{self.name}: {self.avatar}"
    # Русификация категории пользователей для суперАдмина
    class Meta:
        verbose_name = 'Водитель'
        verbose_name_plural = 'Водители'

#  Данные пассажира доступные для суперАдмина

class Passenger(models.Model):
    name = models.CharField(max_length=100, verbose_name='ФИО пассажира')
    telephone_number = models.IntegerField(verbose_name='Номер телефона')
    email = models.EmailField(max_length=100, verbose_name='Электронная почта')

    def __str__(self):
        return self.name
  # Русификация категории пользователей для суперАдмина
    class Meta:
        verbose_name = 'Пассажир'
        verbose_name_plural = 'Пассажиры'


 #  Данные обращений доступные для суперАдмина

class Comment(models.Model):
    author = models.CharField(max_length=30, verbose_name="Автор обращения")
    comment_text = models.TextField(verbose_name="Текст обращения")
    created_date = models.DateField(auto_now_add=True, verbose_name="Дата создания обращения")
    passenger = models.ForeignKey(Passenger, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.author}: {self.created_date - {self.passenger}}"

    # Русификация категории пользователей для суперАдмина
    class Meta:
        verbose_name = 'Обращение'
        verbose_name_plural = 'Обращения'




