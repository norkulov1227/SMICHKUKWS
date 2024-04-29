from django.urls import path
from .views import HomePageView, ContactView, BlogView, BlogDetailView, AboutView

urlpatterns=[
     path('', HomePageView.as_view(), name='index'),
     path('contact/', ContactView.as_view(), name='contact'),
     path('blog/', BlogView.as_view(), name='blog'),
     path('blog-detail/', BlogDetailView.as_view(), name='blog-detail'),
     path('about/', AboutView.as_view(), name='about'),
]