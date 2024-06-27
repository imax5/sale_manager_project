from django.views.generic import ListView

from .models import Product

class ContactList(ListView):
    context_object_name = "contacts"
    paginate_by = 50

    def get_queryset(self):
        user = self.request.user
        if user.is_authenticated:
            return Product.objects.filter(created_by=self.request.user)
        return Product.objects.filter(created_by=None)