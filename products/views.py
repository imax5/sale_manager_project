from django.views.generic import ListView

from .models import Product

class ProductList(ListView):
    context_object_name = 'products'
    model = Product
    queryset = Product.objects.all()
    paginate_by = 50
    template_name = 'products_list.html'