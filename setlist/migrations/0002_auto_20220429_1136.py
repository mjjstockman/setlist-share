# Generated by Django 3.2 on 2022-04-29 11:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('setlist', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Release',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=200)),
            ],
        ),
        migrations.AddField(
            model_name='song',
            name='release',
            field=models.ManyToManyField(to='setlist.Release'),
        ),
    ]
