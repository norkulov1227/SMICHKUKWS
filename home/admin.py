from django.contrib import admin
from .models import About, Contact, Product, ProductImage, Order, TestModel, Blog
from django.utils.html import mark_safe

# Register your models here.


@admin.register(About)
class AboutAdmin(admin.ModelAdmin):
    search_fields=('id', 'title',)
    list_display=('id', 'title',)
    list_display_links=('id', 'title',)
    readonly_fields=('id',)

    def display_image(self, obj):
        return mark_safe('<img src="%s" width="20" />' % obj.icon.url)
    
    display_image.short_description='Image',



@admin.register(Contact)
class ContactAdmin(admin.ModelAdmin):
    list_display=('id', 'name', 'email', 'subject', 'created_at',)
    list_display_links=('id', 'name', 'email',)
    readonly_fields=('id',)




class ProductImageInline(admin.TabularInline):
    # readonly_fields=('id', 'image')
    model=ProductImage
    extra = 1

@admin.register(Order)
class OrderAdmin(admin.ModelAdmin):
    
    list_display=('id', 'product', 'quantity', 'name', 'phone',)
    list_display_links=('id', 'product', 'quantity', )
    readonly_fields=('id',)
    



class ProductImageInline(admin.StackedInline):
    readonly_fields=('updated_at', )
    model=ProductImage
    extra=1


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    inlines=[ProductImageInline, ]
    list_display=('id', 'title', 'price', 'percentage', 'created_at', 'is_active', )
    list_display_links=('title',)
    readonly_fields=('id',)
    list_editable=( 'is_active',)
    search_fields=('created_at', 'price',)



@admin.register(TestModel)
class TestModelAdmin(admin.ModelAdmin):
    list_display=('id', 'name', )
    search_fields=('name',)
    readonly_fields=('id',)

    def display_image(self, obj):
        return mark_safe('<img src="%s" width="20" />' % obj.icon.url)
    
    display_image.short_description='Image',



@admin.register(Blog)
class BlogAdmin(admin.ModelAdmin):
    list_display=('id', 'title', 'views')
    list_display_links=('id', 'title',)
    search_fields=('title', )
    readonly_fields=('id', 'views',)

