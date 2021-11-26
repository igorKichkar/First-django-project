from django.contrib.auth import logout
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth.views import LoginView
from django.core.paginator import Paginator
from django.http import HttpResponse, request
from django.shortcuts import render, get_object_or_404, redirect
from django.urls import reverse_lazy
from django.views.generic import ListView, DetailView, CreateView
from django.contrib.auth.mixins import LoginRequiredMixin

from women.forms import *
from women.models import Women, Category
from .utils import *


class WomenHome(DataMixin, ListView):
    model = Women
    template_name = 'women/index.html'
    context_object_name = 'womens'

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        c_def = self.get_user_context(title="Главная страница")
        context = dict(list(context.items()) + list(c_def.items()))
        return context

        return dict(list(context.items()) + list(c_def.items()))

    def get_queryset(self):
        return Women.objects.filter(is_published=True)
# def index(request):
#     womens = Women.objects.all()
#     context = {
#         'womens': womens,
#         'cat_selected': 0,
#     }
#     return render(request, 'women/index.html', context=context)


def about(request):             # пагинация для функций
    contact_list = [i for i in range(15)]
    paginator = Paginator(contact_list, 3)

    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    return render(request, 'women/about.html', {'page_obj': page_obj, 'title': 'О сайте'})


class AddPage(LoginRequiredMixin, DataMixin, CreateView):
    raise_exception = True #  срабатывает 403 если неавторизованный пользователь хочет добавить статью
    form_class = AddPostForm
    template_name = 'women/addpage.html'

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        c_def = self.get_user_context(title="Добавление статьи",
                                      cat_selected=None)
        context = dict(list(context.items()) + list(c_def.items()))
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
    return HttpResponse(f"Обратная связь {request.user.is_authenticated}")


def login(request):
    return HttpResponse("Авторизация")


class ShowPost(DataMixin, DetailView):
    model = Women
    slug_url_kwarg = 'post_slug'
    context_object_name = 'post'
    template_name = 'women/post.html'

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        c_def = self.get_user_context(title=context['post'])
        return dict(list(context.items()) + list(c_def.items()))

# def show_post(request, post_slug):
#     post = get_object_or_404(Women, slug=post_slug)
#
#     context = {
#         'post': post,
#         'title': post.title,
#         'cat_selected': 1,
#     }
#     return render(request, 'women/post.html', context=context)


class WomenCategory(DataMixin, ListView):
    model = Women
    template_name = 'women/index.html'
    context_object_name = 'womens'
    allow_empty = False

    def get_queryset(self):
        print(self.kwargs)
        return Women.objects.filter(cat__slug=self.kwargs['cat_slug'], is_published=True)

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        c = Category.objects.get(slug=self.kwargs['cat_slug'])
        c_def = self.get_user_context(title='Категория - ' + str(c.name),
                                      cat_selected=c.pk)

        return dict(list(context.items()) + list(c_def.items()))
# def show_category(request, cat_slug):
#     women_cat = Category.objects.get(slug=cat_slug).pk
#     womens = Women.objects.filter(cat=women_cat)
#     context = {
#         'womens': womens,
#         'cat_selected': women_cat,
#     }
#
#     return render(request, 'women/index.html', context=context)

class RegisterUser(DataMixin, CreateView):
    form_class = RegisterUserForm
    template_name = 'women/register.html'
    success_url = reverse_lazy('login')

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        c_def = self.get_user_context(title="Регистрация")
        return dict(list(context.items()) + list(c_def.items()))


class LoginUser(DataMixin, LoginView):
    form_class = LoginUserForm
    template_name = 'women/login.html'

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        c_def = self.get_user_context(title="Авторизация")
        return dict(list(context.items()) + list(c_def.items()))


    def logout_user(request):
        logout(request)
        return redirect('login')
