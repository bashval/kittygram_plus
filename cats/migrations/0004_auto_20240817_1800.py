# Generated by Django 3.2 on 2024-08-17 16:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cats', '0003_auto_20240817_1551'),
    ]

    operations = [
        migrations.RenameField(
            model_name='cat',
            old_name='achievement',
            new_name='achievements',
        ),
        migrations.AlterField(
            model_name='cat',
            name='color',
            field=models.CharField(choices=[('Gray', 'Серый'), ('Black', 'Чёрный'), ('White', 'Белый'), ('Ginger', 'Рыжий'), ('Mixed', 'Смешанный')], max_length=16),
        ),
    ]
