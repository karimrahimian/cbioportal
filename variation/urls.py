from django.urls import path,include

from variation import views

urlpatterns = [
    path('',views.index,name='index'),
    path('about',views.about,name='about'),
    path('login',views.login,name='login'),
    path('register',views.login,name='register'),
    path('generate_data',views.generate_data,name='generate_data')
]
