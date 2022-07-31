# Generated by Django 4.0.4 on 2022-05-14 20:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pages', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Food3',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=30)),
                ('cal', models.DecimalField(decimal_places=3, max_digits=5)),
                ('carb', models.DecimalField(decimal_places=3, max_digits=5)),
                ('fat', models.DecimalField(decimal_places=3, max_digits=5)),
                ('prot', models.DecimalField(decimal_places=3, max_digits=5)),
                ('img', models.ImageField(upload_to='foodimgs')),
            ],
        ),
        migrations.DeleteModel(
            name='Food',
        ),
    ]