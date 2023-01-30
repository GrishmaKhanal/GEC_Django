from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('', views.home, name='home'),
    path('index/', views.home, name='index'),
    # path('about/', views.about, name='about'),
    # path('contact/', views.contact, name='contact'),
    # path('history/', views.history, name='history'),
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
