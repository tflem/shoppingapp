from django.shortcuts import render
from .models import Product

def index(request):
    number_of_products = Product.objects.all().count()
    context = {'number_of_products': number_of_products}
    return render(request, 'index.html', context)

# Add Class-Based Generic List View
from django.views import generic

class ProductListView(generic.ListView):
    model = Product
