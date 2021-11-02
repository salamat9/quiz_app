from django.db import models


class Quiz(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField()
    created = models.DateTimeField(auto_now_add=True)


class Question(models.Model):
    question = models.CharField(max_length=255)
    quiz = models.ForeignKey(Quiz, on_delete=models.CASCADE,
                             related_name='questions')


class Option(models.Model):
    TRUE_FALSE = (
        ('true', 'TRUE'),
        ('false', 'FALSE')
    )
    option = models.CharField(max_length=255, choices=TRUE_FALSE, default='false')
    question = models.ForeignKey(Question, on_delete=models.CASCADE,
                                 related_name='options')



# python manage.py makemigrations
# python manage.py migrate