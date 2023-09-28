# Generated by Django 4.2.3 on 2023-07-28 02:31

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('apis', '0002_grade_delete_geeksmodel'),
    ]

    operations = [
        migrations.CreateModel(
            name='Student',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('last', models.CharField(max_length=20)),
                ('first', models.CharField(max_length=20)),
                ('grade', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='students', to='apis.grade')),
            ],
        ),
    ]
