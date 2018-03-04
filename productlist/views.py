from django.views import generic

from .models import Product

class IndexView(generic.ListView):
    template_name       = 'index.html'
    context_object_name = 'number_of_products'

    def get_queryset(self):
        return Product.objects.all().count()

class ProductListView(generic.ListView):
    model         = Product
    template_name = 'product_list.html'
    paginate_by   = 10

class ProductDetailView(generic.DetailView):
    model         = Product
    template_name = 'product_detail.html'

class ProductCreateView(generic.CreateView):
    model         = Product
    template_name = 'product_new.html'
    fields        = '__all__'
