from django.shortcuts import render, redirect
from .forms import ProductCreateForm, BrandCreateForm
from .models import Brand, Product


# Create your views here.
# view for creating and listing of all products
# if the method is get this view will return all objects from models
# if method is post will create a new object inside models
def index(request):
    return render(request, 'index.html')


def add_brand(request):
    if request.method == "GET":
        form = BrandCreateForm()
        context = {}
        context["form"] = form
        return render(request, "addbrand.html", context)
    elif request.method == "POST":
        form = BrandCreateForm(request.POST)
        if form.is_valid():
            form.save()
            return render(request, "index.html")


def list_brand(request):
    form = Brand.objects.all()
    context = {}
    context["form"] = form
    return render(request, "list_brand.html", context)


def update_brand(request, id):
    brands = Brand.objects.get(id=id)
    form = BrandCreateForm(instance=brands)
    context = {}
    context["form"] = form
    if request.method == "POST":
        form = BrandCreateForm(instance=brands, data=request.POST)
        if form.is_valid():
            form.save()
            return redirect("list_brand")
    return render(request, "edit_brand.html", context)


def delete_brand(request, id):
    brands = Brand.objects.get(id=id)
    brands.delete()
    return redirect("list_brand")


def create_product(request):
    form = ProductCreateForm()
    context = {}
    context["form"] = form
    if request.method == "POST":
        form = ProductCreateForm(request.POST, files=request.FILES)
        if form.is_valid:
            form.save()
            return render(request, "product_create.html", context)
        else:
            context["form"] = form
            return render(request, "product_create.html", context)
    return render(request, "product_create.html", context)


def list_products(request):
    mobiles = Product.objects.all()
    context = {}
    context["mobiles"] = mobiles
    return render(request, "product_list.html", context)


def get_object(id):
    return Product.objects.get(id=id)


def edit_item(request, *args, **kwargs):
    id = kwargs.get("id")
    product = get_object(id=id)
    form = ProductCreateForm(instance=product)
    context = {}
    context["form"] = form
    if request.method == "POST":
        form = ProductCreateForm(instance=product, data=request.POST)
        if form.is_valid():
            form.save()
            return redirect("fetchitems")
    return render(request, "edit_product.html", context)


def product_detail(request, *args, **kwargs):
    id = kwargs.get("id")
    product = get_object(id=id)
    context = {}
    context["product"] = product
    return render(request, "product_detail.html", context)


def delete_product(request, *args, **kwargs):
    id = kwargs.get("id")
    product = get_object(id=id)
    product.delete()
    return render(request, "product_list.html")
