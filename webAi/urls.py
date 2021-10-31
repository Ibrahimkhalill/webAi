from django.urls import path
from . import views

urlpatterns = [
    path('', views.Home, name='home'),
    path('submit_data', views.submit, name='submit_data'),
    path('login/', views.Login, name='login'),
    path('register/', views.Register, name='register'),
    path('logout/', views.logoutUser, name='logout'),
 


]