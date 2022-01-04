from django.db import models
from django.contrib.auth.models import User
from django.core.validators import MaxValueValidator, MinValueValidator
from django_auto_one_to_one import AutoOneToOneModel


class Question(models.Model):
    """ Questions and point where point min - 5  max - 20 """

    question = models.CharField(max_length=255, unique=True)
    point = models.IntegerField(default=5, validators=[MinValueValidator(5),
                                                       MaxValueValidator(20)])

    def question_answers(self):
        return self.question_answers.all()

    def __str__(self):
        return self.question


class Answer(models.Model):
    """ Answers and connection with Questions """

    question_id = models.ForeignKey(Question, on_delete=models.CASCADE, related_name='question_answers',
                                    verbose_name='Question name')
    answer = models.CharField(max_length=20)
    right = models.BooleanField('Right Answer')

    def __str__(self):
        return self.answer


class UserPoint(AutoOneToOneModel(User, related_name='user_id')):
    """ Create new record for User where score by default is 0 """

    score = models.PositiveIntegerField(default=0)

    def __str__(self):
        return f'{self.score}'
