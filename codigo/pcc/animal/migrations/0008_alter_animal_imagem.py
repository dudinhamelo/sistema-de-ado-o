# Generated by Django 4.0.3 on 2023-03-31 00:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('animal', '0007_alter_animal_imagem'),
    ]

    operations = [
        migrations.AlterField(
            model_name='animal',
            name='imagem',
            field=models.ImageField(null=True, upload_to='static/imagens/animal/'),
        ),
    ]