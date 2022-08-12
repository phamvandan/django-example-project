from django.urls import path

from . import views

urlpatterns = [
    path('', views.index),
    path('des/<int:id>', views.des),
    path('login', views.login_controller),
    path('logout', views.logout_controller),
    path('authen_and_login', views.authen_and_login),
    path('show_questions', views.show_questions),
]