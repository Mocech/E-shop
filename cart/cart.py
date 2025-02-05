from store.models import Product
from django.conf import settings


# cart Class
class Cart():
    
    
    def __init__(self, request):
        #Initialize the cart
        self.session = request.session  # Access the session object from the Http request
        cart = self.session.get(settings.SESSION_KEY)  # Try to retrieve the cart data from self.session using 'session_key'
        if settings.SESSION_KEY not in request.session:  # Check if 'session_key' is not in the session
            cart = self.session[settings.SESSION_KEY] = {}  # If not, create a new empty cart and store it in the session
        self.cart = cart  # Assign the cart data to the instance attribute and make cart accessible to all pages and visits
          
        
    def add(self, product,quantity):
            product_id = str(product.id)  # Get the product ID as a string
            
            product_qty = str(quantity)
            #LOGIC Of adding tot the cart
            if product_id in self.cart:  # Check if the product is already in the cart
                # Placeholder for logic to handle an existing product in the cart
                pass
            else:
               # self.cart[product_id] = {'price': str(product.price)}  # Add the product to the cart with its price
                self.cart[product_id] = int(product_qty)
                self.session.modified = True  # Mark the session as modified to ensure it is saved
                
    def __len__(self):  
            return len(self.cart)        
        
    def get_prods(self):
            #Get IDs from cart
            product_id = self.cart.keys()
            #Look up products using their ids in the database
            
            products =Product.objects.filter(id__in = product_id)
            #return looked up produts 
            return products
        
    def get_quants(self):
        quantities = self.cart
        return quantities    