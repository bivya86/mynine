from django.urls import path
from app1.views import *
app_name='something1'

urlpatterns=[
    path('print1/',print1,name='print1'),
]