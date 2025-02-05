from django.shortcuts import render, get_object_or_404
from .cart import Cart
from store.models import Product
from django.http import JsonResponse 
from django.shortcuts import render,redirect
from User_Accounts.models import Profile

def cart_summary(request):
    #Get cart
    cart= Cart(request)
    cart_products = cart.get_prods
    quantities = cart.get_quants
    if not request.user.is_authenticated:
        return redirect('login')
    else:    
     User_profile = get_object_or_404(Profile, user=request.user)
     context = {
         'User_profile':User_profile,
         'cart_products':cart_products,
         'quantities':quantities,
     }
   
    
    return render(request, 'cart/cart_summary.html',context)

    
def cart_add(request):
    cart = Cart(request)
    if request.method == 'POST' and request.POST.get('action') == 'post':
        product_id = int(request.POST.get("product_id"))
        product_qty = int(request.POST.get("product_qty"))
        
        product = get_object_or_404(Product, id=product_id)
        
        cart.add(product=product, quantity=product_qty)
        
        # Get cart quantity
        cart_quantity = cart.__len__()
        
        # Return a JSON response with the cart quantity
        response = JsonResponse({'qty': cart_quantity})
        return response

# def cart_delete(request):
#     pass
# def cart_update(request):        
#         pass