from django.http import HttpResponse
from django.shortcuts import render

from women.models import Women, Category


def index(request):
    womens = Women.objects.all()
    cats = Category.objects.all()
    context = {
        'womens': womens,
        'cat_selected': 0,
        'cats': cats,
    }
    return render(request, 'women/index.html', context=context)


def about(request):
    return HttpResponse("О сайте")


def addpage(request):
    return HttpResponse("Добавление статьи")


def contact(request):
    return HttpResponse("Обратная связь")


def login(request):
    return HttpResponse("Авторизация")


def show_post(request, post_id):
    return HttpResponse(f"Отображение статьи с id = {post_id}")


def show_category(request, cat_id):
    womens = Women.objects.filter(cat_id=cat_id)
    cats = Category.objects.all()
    context = {
        'womens': womens,
        'cats': cats,
        'cat_selected': cat_id,
    }

    return render(request, 'women/index.html', context=context)
