from django.urls import path,include
from . import  views

app_name= 'fpo'

urlpatterns=[
     path('index_fpo/',views.index_fpo,name='index_fpo'),
     path('createproduct/',views.ProductCreateView.as_view(),name='createproduct'),
     path('allproducts/',views.allproducts,name='allproducts'),
     path('product/<int:pk>',views.ProductUpdateView.as_view(),name='updateproduct'),
     path('delete/<int:pk>',views.ProductDeleteView.as_view(),name='deleteproduct'),
]