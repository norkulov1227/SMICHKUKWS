from django.shortcuts import render
from django.views import View
from .models import Product, Contact, Blog, About

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



class AboutView(View):
    def get(self, request):
        about = About.objects.all()
        context = {
            'about': about,
        }

        return render(request, 'about.html', context)



class BlogDetailView(View):
    def get(self, request):
        detail = Blog.objects.all().order_by('?')[:3]
        context = {
            'detail': detail,
        }

        return render(request, 'blog-details.html', context)