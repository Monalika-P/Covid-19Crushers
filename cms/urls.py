"""cms URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
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
from covid.views import home1,symptoms1,gethelp1,help2,gethelp_form,symptoms_form,pos_form,helpy_form

urlpatterns = [
    path('admin/', admin.site.urls),
    path('home1', home1),
    path('symptoms1', symptoms1),
    path('gethelp1', gethelp1),
    path('help2', help2),
    path('',home1),
    path('gethelp_form', gethelp_form),
    path('symptoms_form',symptoms_form),
    path('helpy_form',helpy_form),
    path('pos_form',pos_form)



]
