# Generated by Django 4.1.5 on 2023-01-30 07:39

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="Cart",
            fields=[
                (
                    "cart_no",
                    models.CharField(max_length=13, primary_key=True, serialize=False),
                ),
                ("cart_prod", models.CharField(max_length=30)),
                ("cart_member", models.CharField(max_length=15)),
                ("cart_qty", models.IntegerField(max_length=10)),
            ],
            options={
                "db_table": "cart",
                "managed": False,
            },
        ),
        migrations.CreateModel(
            name="Member",
            fields=[
                (
                    "mem_id",
                    models.CharField(max_length=15, primary_key=True, serialize=False),
                ),
                ("mem_pass", models.CharField(max_length=15)),
                ("mem_name", models.CharField(max_length=10)),
            ],
            options={
                "db_table": "member",
                "managed": False,
            },
        ),
    ]
