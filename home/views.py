from django.shortcuts import render, get_object_or_404, redirect
from django.views import View
from django.contrib import messages
from .models import Product, Contact, Blog, About
from django.db.models import Q

class HomePageView(View):
     def get(self, request):
          products = Product.objects.all()
          conttext = {
               'product': products,
          }
          return render(request, 'index.html', conttext)


class ContactView(View):
    def get(self, request):
        return render(request, 'contact.html')

    
    def post(self, request):
        data=request.POST
        contact=Contact()

        contact.name=data.get('name')
        contact.email=data.get('email')
        contact.subject=data.get('subject')
        contact.message=data.get('message')

        contact.save()

        return render(request, 'contact.html')



class BlogView(View):
    def get(self, request):
        blok = Blog.objects.all()
        context = {
            'blok': blok,
        }
        
        return render(request, 'blog.html', context)



class BlogDetailView(View):
    def get(self, request, uuid):
        detail = get_object_or_404(Blog, id=uuid)
        detail.views+=1
        detail.save()
        
        context = {
            'detail': detail,
        }

        return render(request, 'blog-details.html', context)



class AboutView(View):
    def get(self, request):
        about = About.objects.all()
        context = {
            'about': about,
        }

        return render(request, 'about.html', context)



class SearchView(View):
    def get(self, request):
        query = request.GET.get('search')
        if not query:
            messages.error(request, "Bunday mahsulot topilmadi!")
            return redirect('index')

        searchs = Blog.objects.all().filter(Q(title__icontains = query) | Q(description__icontains = query))


        context = {
            'searchs': searchs,
        }
        messages.success(request, "Siz qidirgan mahsulotlar.")
        return render(request, 'search.html', context)