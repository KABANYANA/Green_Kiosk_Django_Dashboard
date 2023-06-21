# Generated by Django 4.2.1 on 2023-06-20 12:50

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Orders',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(default='Default Order Name', max_length=32)),
                ('placement_date', models.DateTimeField(auto_now_add=True)),
                ('order_Status', models.CharField(max_length=32)),
                ('number_of_Orders', models.PositiveIntegerField()),
                ('total_amount', models.IntegerField()),
            ],
        ),
    ]