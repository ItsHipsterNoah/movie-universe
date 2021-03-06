"""movie_universe URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from movieuniverse import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('', views.index, name='index'),
    path('result/', views.result, name='result'),
    path('show/<int:tv_show_id>', views.tv_detail, name='tv_detail') ,
    path('movie/<int:movie_id>/', views.detail, name='int_detail'),
    path('movie/<str:title>/', views.recommendation_detail, name='detail'),
    path('insights/', views.stats, name='insights'),
    path('admin/', admin.site.urls), 
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)

handler404 = 'movieuniverse.views.handle404'