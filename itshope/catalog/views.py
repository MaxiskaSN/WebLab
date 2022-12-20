from django.shortcuts import render
from .models import Videocard, Product
from django.views.generic import DetailView


class ProductDetailViewPrimary(DetailView):
    model = Product
    template_name = 'catalog/details_view.html'
    context_object_name = 'product_name'


class ProductDetailViewSecondary(DetailView):
    model = Product
    template_name = 'catalog/details_view_cpu.html'
    context_object_name = 'product_name'


class ProductDetailViewTertiary(DetailView):
    model = Product
    template_name = 'catalog/details_view_display.html'
    context_object_name = 'product_name'


def catalog_all(request):
    return render(request, 'catalog/catalog_all.html')


def videocards(request):
    product = Product.objects.filter(product_type='videocard')
    return render(request, 'catalog/videocards.html', {'product': product})


def cpu(request):
    product = Product.objects.filter(product_type='cpu')
    return render(request, 'catalog/cpu.html', {'product': product})


def displays(request):
    product = Product.objects.filter(product_type='display')
    return render(request, 'catalog/displays.html', {'product': product})


