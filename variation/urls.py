from django.urls import path,include

from variation import views

urlpatterns = [
    path('',views.index,name='index'),
    path('about',views.about,name='about'),
    path('login',views.login,name='login'),
    path('register',views.login,name='register'),
    path('generate_data',views.generate_data,name='generate_data'),
    path('analysis',views.analysis,name='analysis'),
    path('queryapi',views.queryApi,name='queryapi'),
    path('tissuelist',views.tissuelist,name='tissuelist'),
    path('api',views.api,name='api')
]
print (urlpatterns)
