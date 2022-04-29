from django.shortcuts import render

# Create your views here.



def homepage(request):
    return render(request, 'indexii.html')




def aboutpage(request):
    return render(request, 'aboutii.html')


def contactpage(request):
    return render(request, 'contactii.html')

def pricingpage(request):
    return render(request, 'pricingii.html')

def servicespage(request):
    return render(request, 'servicesii.html')