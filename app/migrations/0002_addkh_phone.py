# Generated by Django 4.2.5 on 2023-12-04 16:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("app", "0001_initial"),
    ]

    operations = [
        migrations.AddField(
            model_name="addkh",
            name="phone",
            field=models.CharField(max_length=200, null=True),
        ),
    ]
