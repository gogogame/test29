from django.http import HttpResponseRedirect, HttpResponse
from django.shortcuts import get_object_or_404, render
from django.urls import reverse
from quiz.models import Question, Answer

# Create your views here.
def home_page(request):
    new_item_text = Question(question_text='item_text')
    return render(request, 'home.html', {
        'new_item_text': request.POST.get( 'item_text', '' ),
    })

def detail(request, question_id):
    question = get_object_or_404(Question, pk=question_id)
    return render(request, 'detail.html', {'question': question})

def results(request, question_id):
    question = get_object_or_404(Question, pk=question_id)
    return render(request, 'result.html', {'question': question})
