# Generated by Django 4.0.2 on 2022-02-19 14:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('notes', '0002_alter_note_message'),
    ]

    operations = [
        migrations.AlterField(
            model_name='note',
            name='title',
            field=models.CharField(max_length=50, unique=True),
        ),
    ]
