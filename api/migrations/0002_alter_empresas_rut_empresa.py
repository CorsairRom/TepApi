# Generated by Django 4.2.3 on 2023-07-10 21:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("api", "0001_initial"),
    ]

    operations = [
        migrations.AlterField(
            model_name="empresas",
            name="rut_empresa",
            field=models.CharField(
                max_length=12, primary_key=True, serialize=False, unique=True
            ),
        ),
    ]
