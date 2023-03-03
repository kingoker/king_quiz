from django.db import models

# Create your models here.

class Quizzes(models.Model):
    published = models.BooleanField(default=False)


    class Meta:
        verbose_name = 'Quizzes'
        verbose_name_plural = 'Quizzes'

    def __str__(self):
        return 'Quizzes'
    

class CloseQuestions(models.Model):
    questionText = models.TextField()
    mainQuizze = models.ForeignKey("Quizzes",on_delete=models.CASCADE, verbose_name='Опрос', null=True, blank=True)


    class Meta:
        verbose_name = 'Закрытый вопрос'

        verbose_name_plural = 'Закрытые вопросы'

    def __str__(self):
        return self.questionText
    


class RadioText(models.Model):
    radioText = models.CharField(max_length=255, verbose_name='Ответ')
    questionText = models.ForeignKey("CloseQuestions",on_delete=models.CASCADE, verbose_name='Вопрос', null=True, blank=True)


    class Meta:
        verbose_name = 'Варианты ответа'

        verbose_name_plural = 'Варианты ответов'

    def __str__(self):
        return self.radioText
    

class OpenQuestions(models.Model):
    questionText = models.TextField(verbose_name='Вопрос')
    mainQuizze = models.ForeignKey("Quizzes",on_delete=models.CASCADE, verbose_name='Вопрос', null=True, blank=True)

    class Meta:
        verbose_name = 'Открытый вопрос'

        verbose_name_plural = 'Открытый вопросы'

    def __str__(self):
        return self.questionText