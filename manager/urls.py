from django.urls import path

from .views import vehicleDataView
from . import views

urlpatterns = [
    path("", views.user_login, name="login"),
    path("create/", views.enter_vehicle_data, name="create"),
    path("transactions/", views.transactions, name="transaction"),

    path("log/", views.getData, name="getData"),
    # path("last/", views.vehicle, name="getData"),

    path('dispense/', views.dispense, name='dispense'),
    path('Check-vehicle/', views.check_vehicle, name='check_vehicle'),
    path('data-log/<str:vehicleNumber>/', vehicleDataView.as_view(), name='vehicleDataView'),
    path('data-log/', vehicleDataView.as_view(), name='vehicleDataView'),
    path('post-vehicle/', views.post_vehicle, name='post_vehicle'),
    path('get-vehicle/<str:vehicleNumber>/', views.get_vehicle, name='get_vehicle'),


]