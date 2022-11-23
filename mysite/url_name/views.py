from django.shortcuts import render
from django.http import HttpResponse


# Create your views here.

# def index(request):
#     print(request)
#     return HttpResponse('Hello world')


def test(request):
    name = request.GET.get('name')
    message = request.GET.get(
        'message')  # получить то, что находится в message http://127.0.0.1:8000/url_name/?name=tom&message=lololol
    print(name)
    return render(request, 'url_name/task_recruto.html', {'name': name, 'message': message})


def index(request):
    """основная"""
    name = request.GET.get('name')
    message = request.GET.get(
        'message')  # получить то, что находится в message http://127.0.0.1:8000/url_name/?name=tom&message=lololol
    print(name, message)
    if name == None and message == None:
        return render(request, 'url_name/information_about_me.html', {'name': name, 'message': message})
    return render(request, 'url_name/task_recruto.html', {'name': name, 'message': message})
