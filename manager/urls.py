from django.urls import path

from .views import transaction, getBuyDate, VehicleList, TransactionsBulkCreateView,PumpStatus
from . import views

urlpatterns = [
    path("", views.user_login, name="login"),
    path("create/", views.enter_vehicle_data, name="create"),
    path('transaction-log/<str:date>/', getBuyDate.as_view(), name='get_buy_date'),
    path("vehicle-list/", VehicleList.as_view(), name="VehicleList-log"),
    path("transaction/", transaction.as_view(), name="transaction"),
    path('transactions/bulk-create/', TransactionsBulkCreateView.as_view(), name='transactions-bulk-create'),
    path('pump-status/', PumpStatus.as_view(), name='PumpStatus'),

    # path("odometer/", odometer.as_view(), name="odometer"),

    path("log/", views.getData, name="getData"),
    path('dispensed_quantity/', views.dispensed_quantity, name='dispensed_quantity'),

    path('dispense/', views.dispense, name='dispense'),
    path('Check-vehicle/', views.check_vehicle, name='check_vehicle'),
    # path('data-log/<str:vehicleNumber>/', vehicleDataView.as_view(), name='vehicleDataView'),
    # path('data-log/', vehicleDataView.as_view(), name='vehicleDataView'),
    path('post-vehicle/', views.post_vehicle, name='post_vehicle'),
    path('get-vehicle/<str:vehicleNumber>/', views.get_vehicle, name='get_vehicle'),

]
