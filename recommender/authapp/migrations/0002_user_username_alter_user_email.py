# Generated by Django 4.2.7 on 2023-11-24 21:05

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("authapp", "0001_initial"),
    ]

    operations = [
        migrations.AddField(
            model_name="user",
            name="username",
            field=models.CharField(default="user", max_length=255, unique=True),
        ),
        migrations.AlterField(
            model_name="user",
            name="email",
            field=models.EmailField(
                blank=True, max_length=254, verbose_name="email address"
            ),
        ),
    ]
