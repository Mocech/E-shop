from .cart import Cart
#create context processor so our cart ca work in all pages

def cart(request):
    #Return the default data from our cart
    #This line returns a dictionary. In Python, dictionaries are collections of key-value pairs.
    #The key here is 'cart', and the value is Cart(request).
    return {'cart':Cart(request)}

