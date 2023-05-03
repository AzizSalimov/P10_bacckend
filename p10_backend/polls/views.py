# from django.shortcuts import render, get_object_or_404
# from django.http import HttpResponse, Http404
# from .models import Question, Choice
# from django.shortcuts import get_object_or_404, render
#
#
# # Create your views here.
#
# def homepage(request):
#     return render(request, 'home.html')
#
#
# def questions_list(request):
#
#  # questions = Question.objects.all()
#  # response = ''
#  # for index ,question in enumerate(questions):
#  #     response += f"{index + 1 }. {question.question_text}<br>"
#  # return HttpResponse(f"Assalumu Akeykum <br>{response}")
#
#  questions = Question.objects.all()
#
#  context = {
#      'questions': questions
#  }
#  return render(request, 'polls/questions.html', context=context)
#
#
#
# def questions_detail(request, pk):
#     # try:
#     #     question = Question.objects.get(id=pk)
#     # except Question.DoesNotExist:
#     #     raise Http404
#     # else:
#     #     return HttpResponse(f"Question text: {question.question_text}<br>pub_date: {question.pub_date}")
#     question = get_object_or_404(Question, id=pk)
#
#     context = {
#         'question': question
#     }
#     return render(request, 'polls/question_detail.html', context= context)


from django.contrib import messages
from django.contrib.messages import SUCCESS, ERROR
from django.http import HttpResponse, Http404
from django.shortcuts import get_object_or_404, render, redirect
from django.contrib.messages import constants as message

from polls.forms import QuestionForm
from polls.models import Question, Choice
from django.contrib import messages
from datetime import date
def homepage(request):
    return render(request, 'home.html')


def questions_list(request):
    questions = Question.objects.all()

    context = {
        "questions": questions
    }

    return render(request, 'polls/questions.html', context=context)


def question_detail(request, pk):
    question = get_object_or_404(Question, id=pk)

    context = {
        "question": question,
    }

    return render(request, 'polls/question_detail.html', context=context)


def question_vote(request, vote_id):
    choice = request.POST.get('choice')
    print(choice)
    question = get_object_or_404(Question, id=vote_id)
    try:
        selected_choice = question.choice_set.get(pk=choice)
    except Choice.DoesNotExist:
        raise Http404("Choice doesn't exist.")
    else:
        selected_choice.votes += 1
        selected_choice.save()
        if selected_choice.is_true:
            messages.add_message(request, SUCCESS, 'Your choice is correct.')
            return HttpResponse('Your choice is correct.')
        else:
            messages.add_message(request, ERROR, 'Your choice is incorrect.')
            return HttpResponse('Your choice is incorrect.')
        # return redirect("polls:questions_list")


def question_add(request):
    form = QuestionForm(request.POST)
    if request.method == "POST":
        if form.is_valid():
            form.save()
            return redirect("polls:questions_list")
    return render(request, 'polls/add_question.html', {"form": form})
