from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('payslip/<str:pk>', views.payslip, name='payslip'),
    path('sign-up', views.register, name='register'),
    path('login', views.login_page, name='login'),
    path('logout', views.logout_page, name='logout'),
]