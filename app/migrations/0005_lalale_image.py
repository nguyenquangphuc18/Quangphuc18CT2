# Generated by Django 4.2.5 on 2023-12-04 17:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("app", "0004_addkh_date"),
    ]

    operations = [
        migrations.AddField(
            model_name="lalale",
            name="image",
            field=models.ImageField(blank=True, null=True, upload_to=""),
        ),
    ]
