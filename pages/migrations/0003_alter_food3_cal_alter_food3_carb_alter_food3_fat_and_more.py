# Generated by Django 4.0.4 on 2022-05-14 20:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pages', '0002_food3_delete_food'),
    ]

    operations = [
        migrations.AlterField(
            model_name='food3',
            name='cal',
            field=models.DecimalField(decimal_places=4, max_digits=6),
        ),
        migrations.AlterField(
            model_name='food3',
            name='carb',
            field=models.DecimalField(decimal_places=4, max_digits=6),
        ),
        migrations.AlterField(
            model_name='food3',
            name='fat',
            field=models.DecimalField(decimal_places=4, max_digits=6),
        ),
        migrations.AlterField(
            model_name='food3',
            name='prot',
            field=models.DecimalField(decimal_places=4, max_digits=6),
        ),
    ]