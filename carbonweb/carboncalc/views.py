from django.shortcuts import render

# Create your views here.

def home(request):
    return render(request, 'home.html')

def result(request):
    num1 = int(request.GET.get('number1'))
    num2 = int(request.GET.get('number2'))
    num3 = int(request.GET.get('number3'))
    num4 = int(request.GET.get('number4'))

    
    if request.GET.get('calculate') == "":
        ans = num1 + num2 + num3 + num4
    return render(request, 'result.html', {'ans': ans})