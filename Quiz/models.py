from django.db import models
from uuid import uuid4
# Create your models here.

class Customers(models.Model):
    username = models.CharField(max_length=250,null=True, blank=True)
    email = models.EmailField(max_length=250,null=True, blank=True)
    phone = models.CharField(max_length=250,null=True, blank=True)
    telegramId = models.CharField(max_length=250,null=True, blank=True)
    

    class Meta:
        verbose_name = 'Пользователь'

        verbose_name_plural = 'Пользователи'

    def __str__(self):
        return self.username


class Quizzes(models.Model):
    published = models.BooleanField(default=False)
    author = models.ForeignKey(Customers, on_delete=models.CASCADE, verbose_name='Автор', null=True, blank=True)
    token = models.CharField(max_length=250,null=True, blank=True, editable=True)

    def save(self, *args, **kwargs):
        if self.token is None:
            self.token = str(uuid4())
        super().save(*args, **kwargs)
        
    class Meta:
        verbose_name = 'Quizzes'
        verbose_name_plural = 'Quizzes'

    def __str__(self):
        return 'Quizzes'
    

class CloseQuestions(models.Model):
    questionText = models.TextField()
    mainQuizze = models.ForeignKey("Quizzes",on_delete=models.CASCADE, verbose_name='Опрос', null=True, blank=True)
    type = models.CharField(max_length=255,null=True, blank=True, editable=False, default="radio")
    order = models.IntegerField(default=0)
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
    type = models.CharField(max_length=255,null=True, blank=True, editable=False, default="open")
    order = models.IntegerField(default=0)
    
    class Meta:
        verbose_name = 'Открытый вопрос'

        verbose_name_plural = 'Открытый вопросы'

    def __str__(self):
        return self.questionText
    

class Gifts(models.Model):
    textGift = models.TextField(verbose_name='Текст для отправки', null=True, blank=True)
    gift = models.FileField(upload_to='gifts/', verbose_name='Файл для отправки', null=True, blank=True)
    customer = models.ForeignKey("Customers",on_delete=models.CASCADE, verbose_name='Владелец', null=True, blank=True)

    class Meta:
        verbose_name = 'Подарок'

        verbose_name_plural = 'Подарки'

    def __str__(self):
        return self.textGift