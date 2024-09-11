from django.urls import path
from .views import index, about, contact, prices, price_list_view

urlpatterns = [
    path('index/', index, name='index'),
    path('about/', about, name='about'),
    path('contact/', contact, name='contact'),
    path('prices_page/', prices, name='prices'),
    path('prices/', price_list_view.as_view(), name='price-list'),
]

