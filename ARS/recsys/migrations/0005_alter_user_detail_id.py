# Generated by Django 3.2 on 2021-04-22 21:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('recsys', '0004_user_detail_approved'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user_detail',
            name='id',
            field=models.IntegerField(auto_created=True, primary_key=True, serialize=False, unique=True),
        ),
    ]