from django.shortcuts import render, get_object_or_404
from django.http import HttpResponseRedirect
from .models.categories import Categor
from .models.products import Product
from .models.orders import Order
from .forms import ProductForm, OrderForm
from django.views.generic import UpdateView, CreateView, ListView
from django.urls import reverse_lazy

def ItemDelete(request, pk):
    obj = Order.objects.get(pk=pk)
    obj.delete()
    val = Order.objects.all()
    return render(request, 'savat.html', {'vals':val})


def Search(request):
    val = request.POST['searchvalue']
    
    print(type(val),"aaaaaaaaaa",val)
    allval = Product.objects.all()
    l = []
    for el in allval:
        if val.lower() in str(el.ismi).lower() or val in str(el.price):
            l.append(el)
    return render(request, 'search.html', {'vals':l})

def Add(request, pk):
    val = Product.objects.all()
    val1 = Categor.objects.all()
    obj = Product.objects.get(pk=pk)
    amount = request.POST['inputvalue']
    vals = Order.objects.all()
    k = True
    for el in vals:
        print(el.name.ismi,"aaa", obj.ismi, "bbbb",  el.narxi,"gggg", obj.price,'kkk', el.count,"ss",amount)
        if el.name.ismi == obj.ismi and el.narxi == obj.price:
            el.count  += int(amount)
            el.save()
            k = False
     
    if k:
        Order.objects.create(name = obj, narxi = obj.price, count = amount)    
    return render(request, 'home.html', {'vals': val, 'categors':val1})
# Create your views here.
def Savat(request):
    val = Order.objects.all()
    res  = []
    for el in val:
        res.append(el.narxi*el.count)
    return render(request, 'savat.html', { 'vals': val, 'res':res})

    

def CreateProducts(request):
    context = {}
    form = ProductForm(request.POST or None, request.FILES)
    if form.is_valid():
        form.save()
        return HttpResponseRedirect('/')
    context['form'] = form
    return render(request, 'create.html',context)

def AllCategor(request):
    val = Categor.objects.all()
    return render(request, 'base.html', {'categors':val})
def AllProduct(request):
    val = Product.objects.all()
    val1 = Categor.objects.all()
    return render(request, 'home.html' , {'vals': val, 'categors':val1})

def BYcategory(request, category):
    val = Product.objects.all()
    val1 = Categor.objects.all()
    l = []
    for el in val:
        if str(el.category)==category:
            l.append(el)
    val = l
    return render(request, 'bycategor.html', {'vals': val, 'categors':val1})

def EditProduct(request, pk):
    detail = {}
    obj = get_object_or_404(Product, pk=pk)
    form = ProductForm(request.POST, request.FILES,instance=obj)
    if form.is_valid():
        form.save()
        return HttpResponseRedirect('/')
    detail['form'] = form
    return render(request, 'edit.html', detail)

# class CreateProduct(CreateView):
#     model = Product
#     template_name = 'create.html'
#     form_class = ProductForm
#     success_url = reverse_lazy('/')



# def CreateProduct(request):
#     context = {}
#     form = ProductForm(request.POST or None, request.FILES)
#     if form.is_valid():
#         form.save()
#         return HttpResponseRedirect('/')
#     context['form'] = form
#     return render(request, 'create.html', context)

def DeleteProduct(request, pk):
    val = Product.objects.get(pk=pk)
    if request.method == 'POST':
        val.delete()
        return HttpResponseRedirect('/')
    return render(request, 'delete.html', {'val':val})