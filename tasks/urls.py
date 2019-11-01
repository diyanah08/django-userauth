from django.urls import path, include
from .views import create_item, show_items

urlpatterns = [
    path('create', create_item, name="create_item"),
    path('', show_items, name="show_items")
]