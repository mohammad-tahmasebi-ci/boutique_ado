from django.shortcuts import render
from .forms import OrderForm
# Create your views here.


def checkout(request):
    bag = request.session.get('bag', {})
    if not bag:
        messages.error(request, "There's nothing in your bag at the moment")
        return redirect(reverse('products'))

    order_form = OrderForm()
    template = 'checkout/checkout.html'
    context = {
        "order_form": order_form,
        "stripe_public_key": "pk_test_51RRzGIFpsB1alqX96u8EbhMF9uwz1kGSZy8c6fn8AC4I6hLk2KWT1imMVcmWQiSGwNhiv4Z8N0lWXWGMVvMoTb7F00DE4P7phh",
        "client_secret": "test client secret",
    }

    return render(request, template, context)
