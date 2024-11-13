# Generated by Django 5.1.3 on 2024-11-13 08:25

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('Admin', '0003_tbl_category_tbl_subcategory'),
    ]

    operations = [
        migrations.CreateModel(
            name='tbl_user',
            fields=[
                ('user_id', models.AutoField(primary_key=True, serialize=False)),
                ('user_name', models.CharField(max_length=50, unique=True)),
                ('user_email', models.EmailField(max_length=254, unique=True)),
                ('user_password', models.CharField(max_length=255)),
                ('user_photo', models.URLField()),
                ('user_contact', models.CharField(max_length=50)),
                ('user_address', models.CharField(max_length=255)),
                ('place', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Admin.tbl_place')),
            ],
        ),
    ]