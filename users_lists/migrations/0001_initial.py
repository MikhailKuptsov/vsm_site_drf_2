# Generated by Django 5.0.4 on 2024-04-07 16:02

import django.core.validators
import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Detail',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('added_date', models.DateField()),
                ('project', models.CharField(choices=[('Desiro', 'Ласточка'), ('Velaro', 'Сапсан'), ('Depot', 'Депо'), ('Sample print', 'Пробная печать')], max_length=100)),
                ('a2v_id', models.CharField(max_length=100, unique=True)),
                ('description', models.TextField()),
            ],
            options={
                'verbose_name': 'Деталь',
                'verbose_name_plural': 'Детали',
                'ordering': ['added_date'],
            },
        ),
        migrations.CreateModel(
            name='Order',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('status', models.CharField(choices=[('processing', 'Обработка'), ('shipped', 'Отправлен'), ('delivered', 'Доставлен'), ('canceled', 'Отменен')], max_length=20)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
            ],
            options={
                'verbose_name': 'Заказ',
                'verbose_name_plural': 'Заказы',
            },
        ),
        migrations.CreateModel(
            name='Users',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('last_name', models.CharField(max_length=70, verbose_name='Фамилия')),
                ('name', models.CharField(max_length=70, verbose_name='Имя')),
                ('email', models.EmailField(max_length=254, unique=True, verbose_name='E-mail')),
                ('phone_number', models.CharField(max_length=12, unique=True, verbose_name='Телефон')),
                ('telegram_id', models.BigIntegerField(unique=True, verbose_name='телеграмм_id')),
                ('location', models.CharField(choices=[('Podmoskovnaya', 'Подмосковная'), ('Andronovka', 'Андроновка'), ('Metallostroy', 'Металлострой'), ('Kaliningrad', 'Калининград'), ('Kryukovo', 'Крюково'), ('Ekaterinburg', 'Екатеринбург'), ('Samara', 'Самара'), ('Nizhny Novgorod', 'Нижний Новгород'), ('Chelyabinsk', 'Челябинск'), ('Adler', 'Адлер'), ('Perm', 'Пермь'), ('Ufa', 'Уфа')], default=0, max_length=100, verbose_name='Локация')),
                ('role', models.CharField(choices=[('user', 'Аутентифицированный пользователь'), ('operator', 'Оператор 3D принтера'), ('admin', 'Администратор')], default=0, max_length=120, verbose_name='Роль')),
                ('password', models.CharField(max_length=100, verbose_name='Пароль')),
            ],
            options={
                'verbose_name': 'Пользователь',
                'verbose_name_plural': 'Пользователи',
                'ordering': ['last_name'],
            },
        ),
        migrations.CreateModel(
            name='Detail3D',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('model_file', models.FileField(upload_to='detail_3d_models/')),
                ('detail', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='model_3d', to='users_lists.detail')),
            ],
            options={
                'verbose_name': 'Модель 3D-детали',
                'verbose_name_plural': 'Модели 3D-деталей',
            },
        ),
        migrations.CreateModel(
            name='DetailImage',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image_file', models.ImageField(upload_to='detail_images/')),
                ('detail', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='images', to='users_lists.detail')),
            ],
            options={
                'verbose_name': 'Изображение детали',
                'verbose_name_plural': 'Изображения деталей',
            },
        ),
        migrations.CreateModel(
            name='OrderDetail',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('quantity', models.PositiveIntegerField(validators=[django.core.validators.MinValueValidator(1, message='Количество не может быть меньше 1!')])),
                ('detail', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='users_lists.detail')),
                ('order', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='order_details', to='users_lists.order')),
            ],
            options={
                'verbose_name': 'Заказ-деталь',
                'verbose_name_plural': 'Заказы-детали',
            },
        ),
        migrations.AddField(
            model_name='order',
            name='user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='users_lists.users'),
        ),
        migrations.AddField(
            model_name='detail',
            name='author',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='users_lists.users'),
        ),
    ]
