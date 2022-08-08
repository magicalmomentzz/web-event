import imp
from unicodedata import name
from urllib import request, response
from django.http import HttpResponse
from django.shortcuts import render
from . models import eventRegisterForm
from django.views.decorators.csrf import csrf_exempt
from paytmchecksum import PaytmChecksum
merchant_key='O7jTmMp29VLt6bV0'


# Create your views here.
def index(request):
    return render(request , "registerevent.html")
def help(request):
    return render(request , "help.html")
def checkout(request):
    if request.method =="POST":
        name= request.POST.get('name', '')
        email= request.POST.get('email', '')
        mobNo= request.POST.get('mobNo', '')
        amount= request.POST.get('quantity', '')
        
        
        eventUsrInfo=eventRegisterForm(name=name , email=email , mobNo=mobNo  ,amount=amount)
        eventUsrInfo.save()
         #request to payment
        param_dict={

            'MID': 'vTBpUR41392170066968',
            'ORDER_ID': str(eventRegisterForm.user_id),
            "TXN_AMOUNT":str(amount),
                
            'CUST_ID': email,
            'INDUSTRY_TYPE_ID': 'RETAIL',
            'WEBSITE': 'DEFAULT',
            'CHANNEL_ID': 'WEB',
            'CALLBACK_URL':'http://127.0.0.1:8000/event/handlerequest/',

        }
        param_dict['CHECKSUMHASH'] = PaytmChecksum.generateSignature (param_dict , merchant_key)
        return render(request, 'paytm.html' ,{'param_dict':param_dict})
    return render(request, 'done.html')
       
@csrf_exempt
def handlerequest(request):
    form=request.POST
    response_dict={}
    for i in form.keys():
        response_dict[i]=form[i]
        if i == 'CHECKSUMHASH':
            checksum=form[i]
    
    verify = PaytmChecksum.verifySignature_checksum(response_dict , merchant_key ,checksum)
    if verify:
        if response_dict['RESPCODE']=='01':
            print("order successful")
        else:
            print('order was not successful' + response_dict['RESPMSG'])
    return render(request , 'paymentstatus.html', {'response':response_dict})
 

    
