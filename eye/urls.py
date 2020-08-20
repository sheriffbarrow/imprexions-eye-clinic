from django.urls import path
from eye import views


urlpatterns = [
    path('', views.home, name='homes'),
    path('about/', views.about, name='about-us'),
    path('appointment/', views.appointmentt, name='appointments'),
]
