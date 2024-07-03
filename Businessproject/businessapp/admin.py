from django.contrib import admin

# Register your models here.
from .models import Departments, Product, CSE, ICE, MECHANICAL, CIVIL, ECE, EEE


class DepartmentAdmin(admin.ModelAdmin):
    list_display = ['name', 'slug']
    prepopulated_fields = {'slug': ('name',)}


admin.site.register(Departments, DepartmentAdmin)


class ProductAdmin(admin.ModelAdmin):
    list_display = ['name']

    prepopulated_fields = {'slug': ('name',)}
    list_per_page = 20


admin.site.register(Product, ProductAdmin)

admin.site.register(CSE)
admin.site.register(ICE)
admin.site.register(MECHANICAL)

admin.site.register(CIVIL)
admin.site.register(ECE)
admin.site.register(EEE)
