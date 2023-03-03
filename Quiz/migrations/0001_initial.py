# Generated by Django 4.1.7 on 2023-03-03 17:09

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='CloseQuestions',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('questionText', models.TextField()),
            ],
            options={
                'verbose_name': 'Закрытый вопрос',
                'verbose_name_plural': 'Закрытые вопросы',
            },
        ),
        migrations.CreateModel(
            name='OpenQuestions',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('questionText', models.TextField(verbose_name='Вопрос')),
            ],
            options={
                'verbose_name': 'Открытый вопрос',
                'verbose_name_plural': 'Открытый вопросы',
            },
        ),
        migrations.CreateModel(
            name='RadioText',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('radioText', models.CharField(max_length=255, verbose_name='Вопрос')),
            ],
            options={
                'verbose_name': 'Варианты ответа',
                'verbose_name_plural': 'Варианты ответов',
            },
        ),
        migrations.CreateModel(
            name='Quizzes',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('closeQuestions', models.ForeignKey(blank=True, editable=None, null=True, on_delete=django.db.models.deletion.CASCADE, to='Quiz.closequestions', verbose_name='Закрытые вопросы')),
                ('openQuestions', models.ForeignKey(blank=True, editable=None, null=True, on_delete=django.db.models.deletion.CASCADE, to='Quiz.openquestions', verbose_name='Открыте вопросы')),
            ],
            options={
                'verbose_name': 'Quizzes',
                'verbose_name_plural': 'Quizzes',
            },
        ),
        migrations.AddField(
            model_name='closequestions',
            name='radioText',
            field=models.ForeignKey(blank=True, editable=None, null=True, on_delete=django.db.models.deletion.CASCADE, to='Quiz.radiotext', verbose_name='Варианты овета'),
        ),
    ]
