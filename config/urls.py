"""config URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.0/topics/http/urls/
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
from demos.views import calculator, lotto_basic, lotto_challenge, index, lotto_result

urlpatterns = [
    path('admin/', admin.site.urls),
    path('calculator/', calculator),
    path('', index),
    path('lotto/basic/', lotto_basic),
    path('lotto/challenge/', lotto_challenge),
    path('lotto/result/', lotto_result)
]