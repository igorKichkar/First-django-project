from django.urls import path

from .views import *
from django.conf import settings
from django.conf.urls.static import static
from django.views.decorators.cache import cache_page

urlpatterns = [
    path('', cache_page(60)(WomenHome.as_view()), name='home'), # добавлен кэш для представления
    path('about/', about, name='about'),
    path('addpage/', AddPage.as_view(), name='add_page'),
    path('contact/', contact, name='contact'),
    path('login/', LoginUser.as_view(), name='login'),
    path('logout/', LoginUser.as_view(), name='logout'),
    path('post/<slug:post_slug>/', ShowPost.as_view(), name='post'),
    path('category/<slug:cat_slug>/', WomenCategory.as_view(), name='category'),
    path('register/', RegisterUser.as_view(), name='register'),
]
if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
