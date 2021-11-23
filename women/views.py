from django.http import HttpResponse
from django.shortcuts import render, get_object_or_404, redirect

from women.forms import *
from women.models import Women, Category


def index(request):
    womens = Women.objects.all()
    context = {
        'womens': womens,
        'cat_selected': 0,
    }
    return render(request, 'women/index.html', context=context)


def about(request):
    return HttpResponse("О сайте")


def addpage(request):
    if request.method == 'POST':
        form = AddPostForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('home')
    else:
        form = AddPostForm()
    return render(request, 'women/addpage.html', {'form': form})


def contact(request):
    return HttpResponse("Обратная связь")


def login(request):
    return HttpResponse("Авторизация")


def show_post(request, post_slug):
    post = get_object_or_404(Women, slug=post_slug)

    context = {
        'post': post,
        'title': post.title,
        'cat_selected': 1,
    }
    return render(request, 'women/post.html', context=context)


def show_category(request, cat_slug):
    women_cat = Category.objects.get(slug=cat_slug).pk
    womens = Women.objects.filter(cat=women_cat)
    context = {
        'womens': womens,
        'cat_selected': women_cat,
    }

    return render(request, 'women/index.html', context=context)
