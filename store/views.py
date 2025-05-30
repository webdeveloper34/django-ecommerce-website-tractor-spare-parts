from django.shortcuts import render
from .models import Product

# Home page view
def home(request):
    products = Product.objects.all()
    return render(request, 'store/home.html', {'products': products})

# Product detail page
def product_detail(request, id):
    product = Product.objects.get(id=id)
    return render(request, 'store/product_detail.html', {'product': product})

# Cart page
def cart(request):
    return render(request, 'store/cart.html')

# Checkout page
def checkout(request):
    return render(request, 'store/checkout.html')

# Search page
def search(request):
    query = request.GET.get('q', '')
    products = Product.objects.filter(name__icontains=query)
    return render(request, 'store/search_results.html', {'products': products, 'query': query})
