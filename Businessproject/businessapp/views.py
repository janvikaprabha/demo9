from django.core.paginator import Paginator, EmptyPage, InvalidPage
from django.shortcuts import render, get_object_or_404
from .models import Departments, Product, CSE, ICE, EEE, CIVIL, MECHANICAL, ECE
from businessapp.models import Departments

#
# Create your views here.
# def department(request):
#     dep=Department.objects.all()
#     context={
#         'dep_list':dep
#     }
#     return render(request,'department.html',context)


def department(request,d_slug=None):
    d_page=None
    products_list=None
    if d_slug!=None:
        c_page=get_object_or_404(Departments,slug=d_slug)
        products_list=Product.objects.all().filter(department=d_page)
    else:
        products_list=Product.objects.all().filter()
        paginator=Paginator(products_list,6)
        try:
            page=int(request.GET.get('page','1'))
        except:
            page=1
        try:
            products_list=paginator.page(page)
        except (EmptyPage,InvalidPage):
            products_list=paginator.page(paginator.num_pages)

    return render(request,"department.html",{'department':d_page,'products':products_list})


def proDetail(request,d_slug,product_slug):
    try:
        product=Product.objects.get(department__slug=d_slug,slug=product_slug)
    except Exception as e:
        raise e
    return render(request, 'product.html', {'product': product})


def index(request):
    return render(request,'index.html')

def cse(request):
    cse = CSE.objects.all()
    context = {
        'cse_list': cse
    }
    return render(request, 'cse.html', context)


def ice(request):
    ice = ICE.objects.all()
    context = {
        'ice_list': ice
    }
    return render(request, 'ice.html', context)

def eee(request):
    eee = EEE.objects.all()
    context = {
        'eee_list': eee
    }
    return render(request, 'eee.html', context)

def civil(request):
    civil = CIVIL.objects.all()
    context = {
        'civil_list': civil
    }
    return render(request, 'civil.html', context)

def mechanical(request):
    mechanical = MECHANICAL.objects.all()
    context = {
        'mechanical_list': mechanical
    }
    return render(request, 'mechanical.html', context)

def ece(request):
    ece = ECE.objects.all()
    context = {
        'ece_list': ece
    }
    return render(request, 'ece.html', context)

