from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect, get_object_or_404
from django.utils import timezone
from django.views.generic import ListView
from django.http import HttpResponseNotAllowed
from .models import Todo, Answer, Question
from .forms import QuestionForm, AnswerForm
from django.contrib import messages



def main(request):
    return render(request, 'todoapp/todo.html')


def create(request):
    # todo = request.GET.get('todo')
    # 값을 꺼내오는 로직.
    # 모델 객체로 정의한 Todo 클래스에 필요한 값을 넣어서 객체를 생성
    todo = Todo(todo=request.GET.get('todo'), author=request.user)  # create_date=timezone.now()) 얘 없어도 값이 자동으로 들어감.
    todo.save()
    # return render(request, 'todoapp/todo.html', {'todo': todo})
    return redirect('/todo/list')


# def list(request):
#     todo_list = Todo.objects.order_by('create_date')
#     return render(request,'todoapp/list.html',{'todo_list':todo_list})

class TodoList(ListView):
    model = Todo
    # template_name = 'todoapp/list.html'


def update(request, todo_id):
    todo = Todo.objects.get(id=todo_id)
    if todo.end_date:
        todo.end_date = None
    else:
        todo.end_date = timezone.now()
    todo.save()
    return redirect('/todo/list')


def delete(requset, todo_id):
    todo = Todo.objects.get(id=todo_id)
    todo.delete()
    return redirect('/todo/list')


def baseTest(request):
    return render(request, "todoapp/baseTest.html")

@login_required(login_url='accounts:login')
def answer_create(request, question_id):
    question = get_object_or_404(Question, pk=question_id)
    if request.method == "POST":
        form = AnswerForm(request.POST)
        if form.is_valid():
            answer = form.save(commit=False)
            answer.author = request.user
            answer.create_date = timezone.now()
            answer.question = question
            answer.save()
            return redirect('todo:detail', question_id=question.id)
    else:
        return HttpResponseNotAllowed('Only POST is possible.')
    context = {'question': question, 'form': form}
    return render(request, 'todoapp/question_detail.html', context)


def index(request):
    question_list = Question.objects.order_by('-create_date')
    context = {'question_list': question_list}
    return render(request, 'todoapp/question_list.html', context)


def detail(request, question_id):
    question = Question.objects.get(id=question_id)
    context = {'question': question}
    return render(request, 'todoapp/question_detail.html', context)

@login_required(login_url='accounts:login')
def question_create(request):
    if request.method == 'POST':
        form = QuestionForm(request.POST)
        if form.is_valid():  # 폼이 유효하면
            question = form.save(commit=False)  # 임시저장 question 객체리턴
            question.author = request.user
            question.create_date = timezone.now()  # 실제저장 작성일시
            question.save()  # 데이터 저장
            return redirect('todo:index')
    else:
        form = QuestionForm()
    context = {'form': form}
    return render(request, 'todoapp/question_form.html', context)

@login_required(login_url='accounts:login')
def question_modify(request, question_id):
    question = get_object_or_404(Question, pk=question_id)
    if request.user != question.author:
        messages.error(request, '수정권한이 없습니다')
        return redirect('todo:detail', question_id=question.id)
    if request.method == "POST":
        form = QuestionForm(request.POST, instance=question)
        if form.is_valid():
            question = form.save(commit=False)
            question.modify_date = timezone.now()  # 수정일시 저장
            question.save()
            return redirect('todo:detail', question_id=question.id)
    else:
        form = QuestionForm(instance=question)
    context = {'form': form}
    return render(request, 'todoapp/question_form.html', context)

@login_required(login_url='accounts:login')
def question_delete(request, question_id):
    question = get_object_or_404(Question, pk=question_id)
    if request.user != question.author:
        messages.error(request, '삭제권한이 없습니다')
        return redirect('todo:detail', question_id=question.id)
    question.delete()
    return redirect('todo:index')

