from django.test import TestCase
from django.contrib.auth import get_user_model
from .models import Question, Answer, UserPoint
from django.urls import reverse

User = get_user_model()


class MillionaireTestCases(TestCase):

    def setUp(self) -> None:
        self.user = User.objects.create(username='Test', password='12345')
        self.question = Question.objects.create(question='Which one is data type ?', point=7)
        self.answer = Answer.objects.create(question_id=self.question, answer='frozenset', right=True)

    def test_user_qustion(self):
        user = User.objects.get(username='Test')
        print(f"Username: {user.username} \nPassword: {user.password}")

    def test_question(self):
        q1 = Question.objects.get(point=7)
        print(f"Question: {q1.question} Point: {q1.point}")

    def test_answer(self):
        a1 = Answer.objects.get(question_id=1)
        print(f"Answer: {a1.question_id} Point: {a1.answer}, is_Right {a1.right}")

class ViewsTestCase(TestCase):
    def test_home_page(self):
        response = self.client.get(reverse("home"))
        self.assertEqual(response.status_code, 200)

    def test_top_10_page(self):
        response = self.client.get(reverse("score"))
        self.assertEqual(response.status_code, 200)

    def test_game_page(self):
        response = self.client.get(reverse("gameplay"))
        self.assertEqual(response.status_code, 200)

    def test_check_answer_page(self):
        response = self.client.get(reverse("check_answer"))
        self.assertEqual(response.status_code, 200)


