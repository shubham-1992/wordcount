
from django.urls import path
from .import views 

urlpatterns = [
    path('',views.home, name='homepage'),
    path('countwords//',views.count,name='count'),
    path('about',views.about,name='about_')
]
