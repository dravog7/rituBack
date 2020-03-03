# Generated by Django 3.0.3 on 2020-03-02 09:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('events', '0009_auto_20200301_1551'),
    ]

    operations = [
        migrations.AlterField(
            model_name='event',
            name='dept',
            field=models.CharField(choices=[('CSE', 'CSE'), ('MCA', 'MCA'), ('ECE', 'ECE'), ('EEE', 'EEE'), ('Mech', 'Mech'), ('Civil', 'Civil'), ('B.Arch', 'B.Arch'), ('General', 'General')], default='General', max_length=10),
        ),
        migrations.AlterField(
            model_name='event',
            name='fees',
            field=models.CharField(blank=True, default=0, max_length=200, null=True),
        ),
        migrations.AlterField(
            model_name='workshop',
            name='dept',
            field=models.CharField(choices=[('CSE', 'CSE'), ('MCA', 'MCA'), ('ECE', 'ECE'), ('EEE', 'EEE'), ('Mech', 'Mech'), ('Civil', 'Civil'), ('B.Arch', 'B.Arch'), ('General', 'General')], max_length=10),
        ),
        migrations.AlterField(
            model_name='workshop',
            name='fees',
            field=models.CharField(blank=True, default=0, max_length=200, null=True),
        ),
    ]
