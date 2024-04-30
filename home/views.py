from django.shortcuts import render
from django.views import View
from .models import Product, About
from django.core.paginator import Paginator

class HomePageView(View):
     def get(self, request ):
          products = Product.objects.filter(is_active=True)
          random_three_products=products.order_by('?')[:3]
          conttext = {
               'product': products,
               'random_three_products':random_three_products,
          }
          return render(request, 'index.html', conttext)


class AllProductView(View):
    def get(self, request):

        products_all = Product.objects.all().filter(is_active = True)

        page_size=request.GET.get('page_size', 8)
        paginator = Paginator(products_all, page_size)

        page = request.GET.get('page', 1)
        page_obj = paginator.page(page)
        context = {
            'products_all':page_obj,
            
        }

        return render(request, "products.html", context)




class ProductDetailView(View):
     def get(self, request, uuid):
        product=Product.objects.filter(is_active = True, id=uuid).first()

        context = {
            'product':product
        }
        
        return render(request, 'product-details.html', context)

class AboutView(View):
    def get(self, request):
        all_about=About.objects.all().filter(is_active=True)
        # chosen_about=all_about.filter(id=id)

        context = {
            'all_about':all_about
        }
        

        return render(request, 'about.html', context)
