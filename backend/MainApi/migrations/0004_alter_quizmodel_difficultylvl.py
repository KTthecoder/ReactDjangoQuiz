# Generated by Django 3.2.8 on 2022-08-10 09:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('MainApi', '0003_auto_20220810_1153'),
    ]

    operations = [
        migrations.AlterField(
            model_name='quizmodel',
            name='difficultyLvl',
            field=models.CharField(choices=[('Hard', 'Hard'), ('Medium', 'Medium'), ('Easy', 'Easy')], default='Easy', max_length=6),
        ),
    ]
