from .models import Blog

def index_processor(request):
    blogdetail=Blog.objects.all().order_by('?')[:3]

    context={
        'blok': blogdetail,
    }
    return context