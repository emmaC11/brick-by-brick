# Generated by Django 3.2.20 on 2023-08-05 15:25

import cloudinary.models
from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='LegoSet',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200)),
                ('price', models.DecimalField(decimal_places=2, max_digits=10)),
                ('piece_count', models.PositiveIntegerField()),
                ('item_number', models.PositiveIntegerField()),
                ('ages', models.PositiveIntegerField()),
                ('minifigures', models.PositiveIntegerField()),
                ('stock_quantity', models.PositiveIntegerField(default=0)),
                ('is_available', models.BooleanField(default=True)),
                ('image', cloudinary.models.CloudinaryField(default='placeholder', max_length=255, verbose_name='image')),
            ],
        ),
        migrations.CreateModel(
            name='LegoSetTheme',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('theme_name', models.CharField(max_length=200)),
                ('theme_description', models.CharField(max_length=500)),
            ],
        ),
        migrations.CreateModel(
            name='OrderItem',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('quantity', models.PositiveIntegerField(default=1)),
                ('item', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='lego_main.legoset')),
            ],
        ),
        migrations.CreateModel(
            name='Order',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('order_date', models.DateTimeField()),
                ('ordered', models.BooleanField(default=False)),
                ('items', models.ManyToManyField(to='lego_main.OrderItem')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.AddField(
            model_name='legoset',
            name='theme',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='lego_main.legosettheme'),
        ),
    ]