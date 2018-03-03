from django.urls import path
from  . import views

urlpatterns = [
    path('', views.index, name='index'),
    # Define products url pattern
    path('products/', views.ProductListView.as_view(), name='products'),
]
