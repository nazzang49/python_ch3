"""python_ch3 URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
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

import emaillist.views
import helloworld.views
import urltest.views

# Controller 역할
urlpatterns = [
    path('admin/', admin.site.urls),
    path('helloworld/', helloworld.views.hello),
    path('helloworld/hello2/<int:id>', helloworld.views.hello2),
    path('helloworld/hello3', helloworld.views.hello3),
    path('helloworld/counter_max', helloworld.views.counter_max),
    path('helloworld/counter_add', helloworld.views.counter_add),
    path('helloworld/counter_update', helloworld.views.counter_update),
    path('urltest/', urltest.views.test),
    path('emaillist/', emaillist.views.index),
    path('emaillist/form', emaillist.views.form),
    path('emaillist/add', emaillist.views.add)

]
