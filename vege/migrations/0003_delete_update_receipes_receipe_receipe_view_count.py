# Generated by Django 4.2.1 on 2023-07-03 07:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('vege', '0002_update_receipes_receipe_user'),
    ]

    operations = [
        migrations.DeleteModel(
            name='update_receipes',
        ),
        migrations.AddField(
            model_name='receipe',
            name='receipe_view_count',
            field=models.IntegerField(default=100),
        ),
    ]
