# Generated by Django 4.2.2 on 2023-07-15 13:39

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Homie', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='contact',
            old_name='Name',
            new_name='name',
        ),
    ]
