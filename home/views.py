from django.shortcuts import render
from django.views import View
from .models import Product

class HomePageView(View):
     def get(self, request):
          products = Product.objects.all()
          conttext = {
               'product': products,
          }
          return render(request, 'index.html', conttext)