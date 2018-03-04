from django.shortcuts import render
from django.views import generic

from .models import Product

class IndexView(generic.ListView):
    template_name       = 'index.html'
    context_object_name = 'number_of_products'

    def get_queryset(self):
        return Product.objects.all().count()

# Add Class-Based Generic List View

class ProductListView(generic.ListView):
    model = Product
    # Add pagination
    paginate_by = 10

class ProductDetailView(generic.DetailView):
    model = Product
