from django.urls import path, include
from .views import *
urlpatterns = [
    # path('', index, name='main'),
    # path('hospital/<int:pk>', hospital, name='hos')
    path('', index, name='home'),
    path('hospital/<int:hos_id>', hospital, name='hos'),
]
