# Generated by Django 3.0.3 on 2020-02-28 18:32

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('automate', '0001_initial'),
        ('events', '0004_auto_20200226_1400'),
    ]

    operations = [
        migrations.AddField(
            model_name='event',
            name='ImageFrom',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='automate.Image'),
        ),
    ]
