from django.contrib import admin
from .models import Shoes, MoreInfo, Opinion, WearedBy


def brand_and_model(Shoes):
    return "{} {}".format(Shoes.brand, Shoes.model)

@admin.register(Shoes)
class ShoesAdmin(admin.ModelAdmin):
    #fields = ['brand', 'model', 'size']
    #exclude = ['description']
    list_display = [brand_and_model,'size', 'quantity']
    list_filter = ['price']
    search_fields = ['model', 'brand']


admin.site.register(MoreInfo)

admin.site.register(Opinion)

admin.site.register(WearedBy)
