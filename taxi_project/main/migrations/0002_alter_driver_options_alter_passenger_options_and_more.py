# Generated by Django 4.0.6 on 2022-08-20 14:44

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='driver',
            options={'verbose_name': 'Водитель', 'verbose_name_plural': 'Водители'},
        ),
        migrations.AlterModelOptions(
            name='passenger',
            options={'verbose_name': 'Пассажир', 'verbose_name_plural': 'Пассажиры'},
        ),
        migrations.AlterField(
            model_name='driver',
            name='driver_license',
            field=models.IntegerField(verbose_name='Водительское удостоверение'),
        ),
        migrations.AlterField(
            model_name='driver',
            name='identification_card',
            field=models.IntegerField(verbose_name='Удостоверение личности, №'),
        ),
        migrations.AlterField(
            model_name='passenger',
            name='telephone_number',
            field=models.IntegerField(verbose_name='Номер телефона'),
        ),
        migrations.CreateModel(
            name='Comment',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('author', models.CharField(max_length=30, verbose_name='Автор обращения')),
                ('comment_text', models.TextField(verbose_name='Текст обращения')),
                ('created_date', models.DateField(auto_now_add=True, verbose_name='Дата создания обращения')),
                ('passenger', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='main.passenger')),
            ],
            options={
                'verbose_name': 'Обращение',
                'verbose_name_plural': 'Обращения',
            },
        ),
    ]
