from django.http import HttpResponseRedirect, HttpResponse
from django.shortcuts import get_object_or_404, render
from django.urls import reverse
from quiz.models import Question, Answer

# Create your views here.
def home_page(request):
    return render(request, 'home.html')

def detail(request, question_id):
    try:
        question = Question.objects.get(pk=question_id)
    except Question.DoesNotExist:
        raise Http404("Question does not exist")
    return render(request, 'detail.html', {'question': question})

def results(request, question_id):
    def results(request, question_id):
        question = get_object_or_404(Question, pk=question_id)
    return render(request, 'result.html', {'question': question})
