from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
from .models import News

def index(request):
    #return HttpResponse('<h1> Ура, работает! </h1>')
    value = -2
    n1 = News('Новость 1', 'Текст 1', '07.11.23')
    n2 = News('Новость 2', 'Текст 2', '01.11.23')
    #l = ['раз', 'два', 'три']
    l = [n1, n2]
    context = {'title':'Страница главная',
               'Header1':'Заголовок страницы',
               #'value': value,
               'numbers': l}
    return render(request, 'main/index.html', context)

def sidebar(request):
    return render(request, 'include/sidebar.html')

def about(request):
    return HttpResponse('<h1> страница про нас </h1>')

def contacts(request):
    return HttpResponse('<h1> Контакты </h1>')