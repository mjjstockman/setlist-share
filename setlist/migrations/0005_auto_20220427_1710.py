# Generated by Django 3.2 on 2022-04-27 17:10

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('setlist', '0004_venue'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='gig',
            name='city',
        ),
        migrations.AddField(
            model_name='gig',
            name='fakedate',
            field=models.CharField(max_length=200, null=True),
        ),
        migrations.AddField(
            model_name='venue',
            name='gig',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='setlist.gig'),
        ),
    ]
