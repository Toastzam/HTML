# Generated by Django 4.0.5 on 2022-06-15 01:19

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('todoapp', '0003_todo_author'),
    ]

    operations = [
        migrations.CreateModel(
            name='Question',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('subject', models.CharField(max_length=100)),
                ('content', models.TextField()),
                ('create_date', models.DateTimeField()),
            ],
        ),
        migrations.CreateModel(
            name='Answer',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('content', models.TextField()),
                ('create_date', models.DateTimeField()),
                ('question', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='todoapp.question')),
            ],
        ),
    ]
