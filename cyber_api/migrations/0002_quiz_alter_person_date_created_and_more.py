# Generated by Django 4.2.16 on 2024-10-24 08:39

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('cyber_api', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Quiz',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=200)),
                ('description', models.TextField()),
                ('date_created', models.DateField(auto_now_add=True)),
                ('date_update', models.DateField(auto_now=True)),
            ],
        ),
        migrations.AlterField(
            model_name='person',
            name='date_created',
            field=models.DateField(auto_now_add=True),
        ),
        migrations.AlterField(
            model_name='person',
            name='phone_number',
            field=models.CharField(blank=True, max_length=20, null=True, verbose_name='tellfon raqam'),
        ),
        migrations.CreateModel(
            name='Question',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.TextField()),
                ('img', models.ImageField(blank=True, null=True, upload_to='img/')),
                ('option_type', models.CharField(max_length=200)),
                ('date_created', models.DateField(auto_now_add=True)),
                ('date_update', models.DateField(auto_now=True)),
                ('quiz', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='cyber_api.quiz')),
            ],
        ),
        migrations.CreateModel(
            name='Option',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('text', models.CharField(max_length=255)),
                ('is_correct', models.BooleanField(default=False)),
                ('question', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='options', to='cyber_api.question')),
            ],
        ),
    ]
