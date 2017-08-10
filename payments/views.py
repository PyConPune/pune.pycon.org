from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt

@csrf_exempt
def webhook(request):
    print request.method
    print request.path
    print request.POST.get
    return render(request, 'ticket/thanks.html')
