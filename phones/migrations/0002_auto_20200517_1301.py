# Generated by Django 3.0.6 on 2020-05-17 13:01

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('phones', '0001_squashed_0002_auto_20200517_1127'),
    ]

    operations = [
        migrations.CreateModel(
            name='TrustQuestion',
            fields=[
                ('phone', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, primary_key=True, serialize=False, to='phones.Phone')),
                ('yes', models.IntegerField(verbose_name='да')),
                ('no', models.IntegerField(verbose_name='нет')),
            ],
        ),
        migrations.AlterField(
            model_name='phone',
            name='number',
            field=models.CharField(max_length=200, unique=True, verbose_name='Номер телефона'),
        ),
    ]