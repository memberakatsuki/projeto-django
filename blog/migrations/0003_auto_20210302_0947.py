# Generated by Django 3.1.7 on 2021-03-02 12:47

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0002_auto_20210225_0740'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='post',
            options={'ordering': ('-publicado',)},
        ),
        migrations.RenameField(
            model_name='post',
            old_name='changed',
            new_name='alterado',
        ),
    ]