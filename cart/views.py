from django.shortcuts import render,redirect
from .cart import CartManager

cart_manager = CartManager()
# Create your views here.
def cart(request):
    
    return render(request,"cart.html")



def add_to_cart(request, item_id):
    if request.user.is_authenticated:
        cart_manager.add_to_cart(request, item_id)
    else:
        cart = request.session.get('cart', {})
        cart[item_id] = cart.get(item_id, 0) + 1
        request.session['cart'] = cart

    return redirect('cart:view_cart')



def view_cart(request):
    cart_manager = CartManager()
    cart_items = cart_manager.get_cart_items(request)
    
    for cart_item in cart_items:
        cart_item.total_price = cart_item.item.price * cart_item.quantity
    cart_total = sum(item.item.price * item.quantity for item in cart_items)

    return render(request, 'cart/cart.html', {'cart_items': cart_items, 'cart_total': cart_total})