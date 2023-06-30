from django.shortcuts import render
import pandas as pd

# Create your views here.

def home(request):
    return render(request, 'home.html')

def result(request):
    num1 = int(request.GET.get('number1'))
    num2 = int(request.GET.get('number2'))
    num3 = int(request.GET.get('number3'))
    num4 = int(request.GET.get('number4'))
    num5 = int(request.GET.get('number5'))

    if request.GET.get('calculate') == "":
        ans = (num1 * 105) + (num2 * 105) + (num3 * 113) + (num4 * .79) + (num5 * 2700)
    if ans > 45000:
        return render(request, 'aboavg.html', {'ans': ans})
    if ans < 25000:
        return render(request, 'belavg.html', {'ans': ans})
    else:
        return render(request, 'result.html', {'ans': ans})