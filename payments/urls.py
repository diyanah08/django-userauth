from django.urls import path
from .views import ask_for_payment, pay, pay_now, donate

urlpatterns = [
    path('ask', ask_for_payment, name="ask"),
    path('make_payment', pay, name="make_payment"),
    path('donate', donate, name="donate"),
    path('pay_now', pay_now, name="pay_now")
]