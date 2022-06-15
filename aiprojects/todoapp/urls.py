from django.urls import path
from . import views
app_name = 'todo'
urlpatterns = [
    path('', views.index, name='index'),
    path('create/', views.create, name='add'),
    # path('list/', views.list, name='list'),
    path('list/', views.TodoList.as_view(), name='list'),
    path('update/<int:todo_id>', views.update, name='update'),
    path('delete/<int:todo_id>', views.delete, name='delete'),
    path('baseTest/', views.baseTest, name='baseTest'),
    path('question/', views.index, name='question'),
    path('question/<int:question_id>/', views.detail, name='detail'),
    path('answer/create/<int:question_id>/', views.answer_create, name='answer_create'),
    path('question/create/', views.question_create, name='question_create'),
    path('question/modify/<int:question_id>/', views.question_modify, name='question_modify'),
    path('question/delete/<int:question_id>/', views.question_delete, name='question_delete'),
]
