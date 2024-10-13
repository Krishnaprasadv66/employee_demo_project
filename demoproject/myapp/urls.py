from django.urls import path
from myapp import views

urlpatterns = [
   
    path('person', views.index, name='person'),
    path('signup', views.signup, name='signup'),
    path('login', views.login, name='login'),
    path('employee', views.employees, name='employee'),
]
