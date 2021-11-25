from django.http import HttpResponse
from django.shortcuts import render, get_object_or_404, redirect
from django.views.generic import ListView, DetailView, CreateView

from women.forms import *
from women.models import Women, Category


class WomenHome(ListView):
    model = Women
    template_name = 'women/index.html'
    context_object_name = 'womens'

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Главная страница'
        context['cat_selected'] = 0
        return context

    def get_queryset(self):
        return Women.objects.filter(is_published=True)
# def index(request):
#     womens = Women.objects.all()
#     context = {
#         'womens': womens,
#         'cat_selected': 0,
#     }
#     return render(request, 'women/index.html', context=context)


def about(request):
    return HttpResponse("О сайте")


class AddPage(CreateView):
    form_class = AddPostForm
    template_name = 'women/addpage.html'
    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Добавление статьи'
        return context
# def addpage(request):
#     if request.method == 'POST':
#         form = AddPostForm(request.POST, request.FILES)
#         if form.is_valid():
#             form.save()
#             return redirect('home')
#     else:
#         form = AddPostForm()
#     return render(request, 'women/addpage.html', {'form': form})


def contact(request):
    return HttpResponse("Обратная связь")


def login(request):
    return HttpResponse("Авторизация")


class ShowPost(DetailView):
    model = Women
    slug_url_kwarg = 'post_slug'
    context_object_name = 'post'
    template_name = 'women/post.html'

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = context['post']
        print(Category.objects.get(name=(context['object']).cat))
        context['cat_selected'] = context['object'].cat_id
        return context

# def show_post(request, post_slug):
#     post = get_object_or_404(Women, slug=post_slug)
#
#     context = {
#         'post': post,
#         'title': post.title,
#         'cat_selected': 1,
#     }
#     return render(request, 'women/post.html', context=context)


class WomenCategory(ListView):
    model = Women
    template_name = 'women/index.html'
    context_object_name = 'womens'
    allow_empty = False

    def get_queryset(self):
        print(self.kwargs)
        return Women.objects.filter(cat__slug=self.kwargs['cat_slug'], is_published=True)

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Категория - ' + str(context['womens'][0].cat)
        context['cat_selected'] = context['womens'][0].cat_id
        return context
# def show_category(request, cat_slug):
#     women_cat = Category.objects.get(slug=cat_slug).pk
#     womens = Women.objects.filter(cat=women_cat)
#     context = {
#         'womens': womens,
#         'cat_selected': women_cat,
#     }
#
#     return render(request, 'women/index.html', context=context)
