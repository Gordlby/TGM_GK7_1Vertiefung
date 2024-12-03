# Generated by Django 5.1.3 on 2024-12-03 12:32

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0002_fach_genau_richtig_fach_zu_hoch_fach_zu_niedrig_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='fach',
            name='genau_richtig',
        ),
        migrations.RemoveField(
            model_name='fach',
            name='zu_hoch',
        ),
        migrations.RemoveField(
            model_name='fach',
            name='zu_niedrig',
        ),
        migrations.CreateModel(
            name='Antwort',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('choice', models.IntegerField(default=0)),
                ('fach', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='main.fach')),
            ],
        ),
    ]
