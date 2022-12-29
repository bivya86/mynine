from django.urls import path
from app2.views import *
app_name='something2'

urlpatterns=[
    path('print2/',print2,name='print2'),
]