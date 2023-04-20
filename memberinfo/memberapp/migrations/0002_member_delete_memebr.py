# Generated by Django 4.1.5 on 2023-01-30 01:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("memberapp", "0001_initial"),
    ]

    operations = [
        migrations.CreateModel(
            name="Member",
            fields=[
                (
                    "mem_id",
                    models.CharField(max_length=15, primary_key=True, serialize=False),
                ),
                ("mem_pass", models.CharField(max_length=15)),
                ("mem_name", models.CharField(max_length=10)),
                ("mem_regno1", models.CharField(max_length=6)),
                ("mem_regno2", models.CharField(max_length=7)),
                ("mem_bir", models.DateTimeField(null=True)),
                ("mem_zip", models.CharField(max_length=7)),
                ("mem_add1", models.CharField(max_length=60)),
                ("mem_add2", models.CharField(max_length=50)),
                ("mem_hometel", models.CharField(max_length=14)),
                ("mem_comtel", models.CharField(max_length=14)),
                ("mem_hp", models.CharField(max_length=15, null=True)),
                ("mem_mail", models.CharField(max_length=40)),
                ("mem_job", models.CharField(max_length=40, null=True)),
                ("mem_like", models.CharField(max_length=40, null=True)),
                ("mem_memorial", models.CharField(max_length=40, null=True)),
                ("mem_memorialday", models.DateTimeField(null=True)),
                ("mem_mileage", models.CharField(max_length=1, null=True)),
            ],
            options={
                "db_table": "member",
                "managed": False,
            },
        ),
        migrations.DeleteModel(
            name="Memebr",
        ),
    ]
