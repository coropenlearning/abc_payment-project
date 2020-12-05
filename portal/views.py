from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
# def = function
def index(request):
    return render(request, 'portal/index.html')

def pay(request):
    wallet_id = request.POST['walletId'] # get value from Form   
    return render(request, 'portal/payment_success.html', {'wallet_id': wallet_id})