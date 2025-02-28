# Generated by Django 5.0.7 on 2024-07-25 22:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('language', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='language',
            name='description',
            field=models.TextField(verbose_name='Описание'),
        ),
        migrations.AlterField(
            model_name='language',
            name='editor',
            field=models.TextField(verbose_name='Редактор'),
        ),
        migrations.AlterField(
            model_name='language',
            name='example',
            field=models.TextField(verbose_name='Пример'),
        ),
        migrations.AlterField(
            model_name='language',
            name='icon',
            field=models.FileField(upload_to='', verbose_name='Иконка'),
        ),
        migrations.AlterField(
            model_name='language',
            name='name',
            field=models.CharField(max_length=15, verbose_name='Название'),
        ),
        migrations.AlterField(
            model_name='language',
            name='product',
            field=models.TextField(verbose_name='Продукты'),
        ),
        migrations.AlterField(
            model_name='language',
            name='tiobe',
            field=models.DecimalField(decimal_places=3, max_digits=5, verbose_name='Индекс TIOBE'),
        ),
        migrations.AlterField(
            model_name='language',
            name='translation',
            field=models.TextField(verbose_name='Трансляция'),
        ),
        migrations.AlterField(
            model_name='language',
            name='trend',
            field=models.TextField(verbose_name='Применение'),
        ),
        migrations.AlterField(
            model_name='language',
            name='typing',
            field=models.TextField(verbose_name='Типизация'),
        ),
        migrations.AlterField(
            model_name='language',
            name='usage',
            field=models.TextField(verbose_name='Реализация'),
        ),
        migrations.AlterField(
            model_name='language',
            name='version',
            field=models.CharField(max_length=15, verbose_name='Версия'),
        ),
    ]
