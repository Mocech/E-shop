from django.shortcuts import render,redirect,get_object_or_404
from .models import Product,Category
from django.contrib.auth.decorators import login_required
from django.contrib import messages


def category(request, cate_name):
    # cate_name = cate_name.replace('-',' ')
    try:
        # This line tries to find a Category object with a name that matches cate_name
        category = Category.objects.get(name = cate_name) 
        
        products =Product.objects.filter(category=category)
        return render(request, 'store/category.html',{'products':products})
    
    except Category.DoesNotExist:    
       messages.error(request, f'Category does not exist!')
       return redirect(request, 'store:home')

def index(request):
    products = Product.objects.filter(stock__gt=0).order_by('price')
    return render(request, 'store/home.html' , {'products':products})


def about(request):
    return render(request, 'store/about.html')

@login_required
def product(request,pk):
    product = get_object_or_404(Product, id=pk)
    related_products = Product.objects.filter(category=product.category).exclude(id=product.id)
    return render(request, 'store/product.html', {'product':product,'related_products': related_products})
    




def test(request):
    return render(request, 'store/test.html',{})