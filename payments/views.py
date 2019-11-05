from django.shortcuts import render, HttpResponse
from .forms import OrderForm, PaymentForm
from django.conf import settings
from django.contrib import messages
from django.utils import timezone
import stripe

# Create your views here.
def ask_for_payment(request):
    return render(request, 'payments/payment_form.template.html')
    
    # simple stripe 
def pay(request):
    if request.method == 'GET':  
       amount = request.GET['amount']
       stripe_publishable_key = settings.STRIPES_PUBLISHABLE_KEY
       return render(request, 'payments/paid.template.html', {
            'publishable_key':stripe_publishable_key,
            'amount_in_dollars':amount,
            'amount':int(amount)*100
        })
    else:
        stripe.api_key = settings.STRIPES_SECRET_KEY
        stripe_token = request.POST["stripeToken"]
        charge = stripe.Charge.create(amount=request.POST["amount"],
            currency='sgd',
            source=stripe_token
        )
        return HttpResponse("Thank you for shoping with us!")
        
        
# complex stripe

def donate(request):
    return render(request, 'payments/complex_payment_form.template.html')
    
def pay_now(request):
    amount = request.GET['amount']
    
    if request.method == 'GET':
        order_form = OrderForm()
        payment_form = PaymentForm()
        return render(request, 'payments/pay.template.html', {
            'order_form' : order_form,
            'payment_form' : payment_form,
            'amount' : amount,
            'publishable': settings.STRIPES_PUBLISHABLE_KEY
        })
    else:
        stripeToken = request.POST['stripe_id']
        
        # set the secret key for the Stripe API
        stripe.api_key = settings.STRIPES_SECRET_KEY
        
        order_form = OrderForm(request.POST)
        payment_form = PaymentForm(request.POST)
        
        if order_form.is_valid() and payment_form.is_valid():
            try:
                customer = stripe.Charge.create(
                    amount= int(request.POST['amount'])*100,
                    currency='usd',
                    description='Donation',
                    card=stripeToken
                    )
                    
                if customer.paid:
                    
                    order = order_form.save(commit=False)
                    order.date=timezone.now()
                    order.save()
                    
                    return render(request, 'payments/thankyou.template.html')
                else:
                    messages.error(request, "Your card has been declined")
            except stripe.error.CardError:
                    messages.error(request, "Your card was declined!")
            
        else:
             return render(request, 'payments/pay.template.html', {
            'order_form' : order_form,
            'payment_form' : payment_form,
            'amount' : amount,
            'publishable': settings.STRIPES_PUBLISHABLE_KEY
        })
        
        return render(request, 'payments/pay.template.html', {
            'order_form' : order_form,
            'payment_form' : payment_form,
            'amount' : amount,
            'publishable': settings.STRIPES_PUBLISHABLE_KEY
            })