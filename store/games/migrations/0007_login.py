# Generated by Django 5.0 on 2023-12-31 06:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('games', '0006_game_title_alter_game_status'),
    ]

    operations = [
        migrations.CreateModel(
            name='Login',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('username', models.CharField(max_length=50)),
                ('password', models.CharField(max_length=50)),
            ],
        ),
    ]
