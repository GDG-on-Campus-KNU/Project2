from datetime import timezone

from django.http import HttpResponse
from django.shortcuts import render, get_object_or_404
# Create your views here.
from vote.forms import QuestionForm
from vote.models import Question


def index(request):
    question_list = Question.objects.order_by('-create_date')
    context = {'question_list':question_list}
    return render(request, 'vote/question_list.html',context)

def detail(request, question_id):
    question = get_object_or_404(Question, pk=question_id)
    context = {'question':question}
    return render(request, 'vote/question_detail.html',context)

def question_create(request):
    if request.method == 'POST':
        form = QuestionForm(request.POST)
        if form.is_valid():
            question = form.save(commit=False)
            question.author = request.user  # 추가한 속성 author 적용
            question.create_date = timezone.now()
            question.save()
            return redirect('vote:index')
    else:
        form = QuestionForm()
    context = {'form': form}
    return render(request, 'vote/question_form.html', context)
