# Generated by Django 5.1.3 on 2024-12-09 04:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Guest', '0003_tbl_shop'),
    ]

    operations = [
        migrations.AlterField(
            model_name='tbl_user',
            name='user_id',
            field=models.TextField(editable=False, primary_key=True, serialize=False),
        ),
    ]
