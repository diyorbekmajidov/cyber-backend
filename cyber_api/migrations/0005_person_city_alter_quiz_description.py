# Generated by Django 4.2.16 on 2024-10-31 09:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cyber_api', '0004_alter_question_option_type'),
    ]

    operations = [
        migrations.AddField(
            model_name='person',
            name='city',
            field=models.CharField(default='11', max_length=20, verbose_name='viloyat'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='quiz',
            name='description',
            field=models.TextField(blank=True, null=True),
        ),
    ]
