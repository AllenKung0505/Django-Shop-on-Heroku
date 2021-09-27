"""DjangoWeb URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
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
from django.conf.urls import url
from django.contrib import admin
from django.urls import path
from Myweb.views import login,logout,product,about,showcart,addcart,order,buy


urlpatterns = [
    path('admin/', admin.site.urls),
    url(r'^$', product),
    url(r'^login/$', login),
    url(r'^logout/$', logout),
    url(r'^product/$', product),
    url(r'^about/$', about),
    url(r'^cart/$', showcart),
    url(r'^addcart/(\w+)/$', addcart),
    url(r'^addcart/(\w+)/(\d+)/$', addcart),
    url(r'^order/$', order),
    url(r'^buy/$', buy),
]

