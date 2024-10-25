# Generated by Django 4.2.16 on 2024-10-24 09:03

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('cyber_api', '0002_quiz_alter_person_date_created_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='QuestionText',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('text', models.TextField()),
                ('quiz', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='cyber_api.quiz')),
            ],
        ),
    ]