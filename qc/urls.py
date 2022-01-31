"""qc URL Configuration

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
from APP.views import table2021
from APP.views import table2022
from APP.views import fs2022
from APP.views import chart
from APP.views import index
from APP.views import base



urlpatterns = [
    path('22/', table2022, name='table2022'), 
    path('21/', table2021, name='table2021'), 
    path('fs22/', fs2022, name='fs2022'), 
    path('chart/', chart, name='chart'), 
    path('index/', index, name='index'), 
    path('0/', base), 
    
]