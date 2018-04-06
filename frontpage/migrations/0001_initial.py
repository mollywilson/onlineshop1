# Generated by Django 2.0.4 on 2018-04-06 15:59

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Earrings',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=250)),
                ('description', models.CharField(max_length=1000)),
                ('price', models.DecimalField(decimal_places=2, max_digits=5)),
                ('picture', models.CharField(max_length=1000)),
            ],
        ),
        migrations.CreateModel(
            name='Rings',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=250)),
                ('description', models.CharField(max_length=1000)),
                ('price', models.DecimalField(decimal_places=2, max_digits=5)),
                ('picture', models.CharField(max_length=1000)),
                ('size', models.CharField(max_length=50)),
                ('collection', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='frontpage.Earrings')),
            ],
        ),
    ]
