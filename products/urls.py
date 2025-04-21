
from django.urls import path

from . import views
urlpatterns=[
    path('hello/',views.hello,name='hello'),
    path('',views.products,name='products'),
    path('<int:id>',views.product,name='product'),
]
