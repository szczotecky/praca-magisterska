from django.shortcuts import render, get_object_or_404
from django.http import HttpResponseRedirect
from django.core.urlresolvers import reverse
import random

from .models import Question

# Create your views here.

def index(request):

    #dopisac losowanie pierwszego pytania
    latest_question = Question.objects.order_by('-pub_date')
    number = random.choice(latest_question).pk



    request.session['counter']=1
    request.session.modified = True

    context = { 'latest_question' : latest_question }

    return render(request, 'polls/index.html', {'context':context, 'number':number })


def detail(request, question_id):

    question = Question.objects.get(pk=question_id)
    counter = request.session.get('counter', 1)
    request.session.modified = True
    counter_bar = (counter/30)*100

    return render(request, 'polls/detail.html', {'question': question, 'counter_bar':counter_bar, 'counter':counter})


def results(request, question_id):
    question = get_object_or_404(Question, pk=question_id)

    return render(request, 'polls/vote.html', {'question': question})


def vote(request, question_id):
    question = get_object_or_404(Question, pk = question_id)

    counter = request.session['counter']
    counter_bar = (counter / 30) * 100

    try:
        selected_choice = question.choice_set.get(pk = request.POST['choice'])
        selected_choice2 = question.choice2_set.get(pk = request.POST['choice2'])
    except:
        return render(request, 'polls/detail.html', {'question': question, 'error_message' : "BRAK ODPOWIEDZI, PROSZĘ WYBRAĆ JEDNĄ Z OPCJI", 'counter_bar':counter_bar, 'counter':counter})
    else:
        selected_choice.votes +=1;
        selected_choice.save()

        selected_choice2.votes += 1;
        selected_choice2.save()

        if counter < 30:
            counter += 1
            request.session['counter'] = counter
            request.session.modified = True
        else:
            counter = 1
            request.session['counter'] = counter
            request.session.modified = True
            return HttpResponseRedirect(reverse('polls:index', args=()))

        #question = Question.objects.get(pk=(int(question_id)+1)) #TUTAJ LOSOWAC NASTĘPNE PYTANIE
        latest_question = Question.objects.order_by('-pub_date')
        question = random.choice(latest_question)


        return HttpResponseRedirect(reverse('polls:detail', args=(question.id,)))