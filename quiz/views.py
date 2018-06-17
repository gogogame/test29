from django.http import HttpResponseRedirect, HttpResponse
from django.shortcuts import get_object_or_404, render
from django.urls import reverse
from quiz.models import Question, Answer

# Create your views here.
def home_page(request):
    question_list = Question.objects.order_by('id')
    context = {'question_list': question_list}
    return render(request, 'home.html', context)

def detail(request, question_id):
    question = get_object_or_404(Question, pk=question_id)
    return render(request, 'detail.html', {'question': question})

def results(request, question_id):
    question = get_object_or_404(Question, pk=question_id)
    return render(request, 'result.html', {'question': question})
