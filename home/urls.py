from django.urls import path
from .views import HomePageView, ContactView, BlogView,CheckoutView, BlogDetailView, AboutView, SearchView,  AllProductView, ProductDetailView, AboutView, SharhlarView

urlpatterns=[
     path('', HomePageView.as_view(), name='index'),
     path('contact/', ContactView.as_view(), name='contact'),
     path('blog/', BlogView.as_view(), name='blog'),
     path('blog-detail/<uuid:uuid>/', BlogDetailView.as_view(), name='blog-detail'),
     path('about/', AboutView.as_view(), name='about'),
    path('search/', SearchView.as_view(), name='search'),
 
     path('products/', AllProductView.as_view(), name = 'products' ),
     path('detail/<uuid:uuid>/', ProductDetailView.as_view(), name="detail" ),
     path ('about/', AboutView.as_view(), name='about' ),
     path('sharhlar/', SharhlarView.as_view(), name='sharhlar'),
     path('checkout/<uuid:uuid>/', CheckoutView.as_view(), name="checkout")
     
]