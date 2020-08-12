from django.urls import path,include
from . import  views

app_name= 'dealer'

urlpatterns=[
     path('index_dealer/',views.index_dealer,name='index_dealer'),
     path('products/',views.fpoproducts, name='fpoproducts'),
]