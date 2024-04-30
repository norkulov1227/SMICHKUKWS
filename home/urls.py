from django.urls import path
from .views import HomePageView, AllProductView, ProductDetailView, AboutView

urlpatterns=[
     path('', HomePageView.as_view(), name='index'),
     path('products/', AllProductView.as_view(), name = 'products' ),
     path('detail/<uuid:uuid>/', ProductDetailView.as_view(), name="detail" ),
     path ('about/', AboutView.as_view(), name='about' )

]