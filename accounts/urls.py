from django.urls import path
from .import  views
app_name = 'accounts'
urlpatterns=[
     path('',views.index, name='index'),
     path('register/',views.register, name='register'),
     path('fpo_register/',views.fpo_register.as_view(), name='fpo_register'),
     path('dealer_register/',views.dealer_register.as_view(), name='dealer_register'),
     path('login/',views.login_request, name='login'),
     path('logout/',views.logout_view, name='logout'),
]