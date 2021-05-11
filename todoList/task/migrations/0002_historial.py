# Generated by Django 3.2.1 on 2021-05-10 00:43

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('task', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Historial',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
                ('startTime', models.CharField(max_length=255)),
                ('endTime', models.CharField(max_length=255)),
                ('task', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='task.task')),
            ],
        ),
    ]
