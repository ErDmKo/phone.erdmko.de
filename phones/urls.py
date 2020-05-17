from django.urls import path

from . import views

urlpatterns = [
    path('', views.PhoneForm.as_view(), name='index'),
    path('<int:pk>/', views.PhoneView.as_view(), name='phone-detail'),
]