# Generated by Django 3.0.3 on 2020-03-05 11:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('events', '0014_auto_20200305_1146'),
    ]

    operations = [
        migrations.AlterField(
            model_name='event',
            name='category',
            field=models.CharField(blank=True, choices=[('Pre-Event', 'Pre-Event'), ('Gaming', 'Gaming'), ('Music and Dance', 'Music and Dance'), ('Club', 'Club'), ('Misc', 'Misc')], default='Misc', max_length=200, null=True),
        ),
    ]
