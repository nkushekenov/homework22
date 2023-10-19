from django.shortcuts import render

def index(request):
    context = {
        'title': 'Главная страница',
        'items': ['элемент 1', 'элемент 2', 'элемент 3'],
    }
    return render(request, 'HW22/index.html', context)
