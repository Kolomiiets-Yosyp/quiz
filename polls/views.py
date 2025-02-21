from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse

from .models import Question


def index(request):
    latest_question_list = Question.objects.order_by("-pub_date")[:5]
    output = ", ".join([q.question_text for q in latest_question_list])
    return HttpResponse(output)


# Leave the rest of the views (detail, results, vote) unchanged
def detail(request, question_id):
    out = Question.objects.get(id=question_id)
    return HttpResponse("You're looking at question %s." % out.question_text)


def results(request, question_id):
    res = Question.objects.get(id=question_id)

    response = "You're looking at the results of question %s."
    return HttpResponse(response % res.pub_date)


def vote(request, question_id):
    return HttpResponse("You're voting on question %s." % question_id)