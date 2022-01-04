from django.http import HttpResponse
from django.shortcuts import render
from django.views.generic import TemplateView
from .models import UserPoint, Question, Answer
from django.contrib.auth.views import LoginView


class UserLoginView(LoginView):
    """ User Registration django-allouth """
    template_name = 'account/login.html'


class IndexView(TemplateView):
    template_name = 'home.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        if 'score' not in self.request.session:
            self.request.session['score'] = 0

        if 'winner' not in self.request.session:
            self.request.session['winner'] = False

        if 'right_answer' not in self.request.session:
            self.request.session['right_answer'] = ""

        user = self.request.user
        if self.request.user.is_authenticated:
            final_score = self.request.session['score']
            is_finish = self.request.session['winner']
            right_answer = self.request.session['right_answer']
            sc = UserPoint.objects.get(user=user)
            sc.score = sc.score + final_score
            sc.save()
            self.request.session['score'] = 0
            self.request.session['winner'] = False
            self.request.session['right_answer'] = ""
        else:
            final_score = self.request.session['score']
            is_finish = self.request.session['winner']
            right_answer = self.request.session['right_answer']

        context['score'] = final_score
        context['winner'] = is_finish
        context['right_answer'] = right_answer
        return context


class GameplayView(TemplateView):
    template_name = 'game.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        self.request.session['q_count'] = 0
        self.request.session['winner'] = False
        self.request.session['score'] = 0
        self.request.session['right_answer'] = ""
        context['questions'] = Question.objects.all().order_by('?')[:5]

        return context


def check_answer(request):
    """ Check the answer which comes in frontend
            and show right answer """

    if request.GET:
        q_count = request.session['q_count']
        answer_id = request.GET.get('answer_id', True)
        answer = Answer.objects.get(pk=answer_id)

        if answer.right:
            request.session['q_count'] += 1
            if q_count == 4:
                request.session['winner'] = True
            current_point = answer.question_id.point
            request.session['score'] += current_point
            return HttpResponse("ok")
        else:
            answers = Answer.objects.filter(question_id=answer.question_id)
            right_answer = ""
            for answer_el in answers:
                if answer_el.right:
                    request.session['right_answer'] = answer_el.answer + ", " + right_answer
            return HttpResponse("not")
    else:
        return render(request, 'home.html')


class GoodPlayersView(TemplateView):
    """ Show Top 10 players if we dont have players show empty """

    template_name = 'good_players.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['scores'] = UserPoint.objects.order_by('-score').all()[:10]
        return context
