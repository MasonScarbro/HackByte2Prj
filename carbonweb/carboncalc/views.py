from django.shortcuts import render
import pandas as pd


# Create your views here.

def car(make, model):
    df = pd.read_csv('static/CO2 Emissions_Canada.csv')
    df.pop('Fuel Consumption Comb (mpg)')
    df.pop('Fuel Consumption Comb (L/100 km)')
    df.pop('Vehicle Class')
    df.pop('Fuel Consumption Hwy (L/100 km)')
    df.pop('Fuel Consumption City (L/100 km)')
    df.pop('Engine Size(L)')
    df.pop('Transmission')
    df.pop('Cylinders')
    df.pop('Fuel Type')
    pd.set_option('display.max_rows', None)
    pd.set_option('display.max_columns', None)
    #USER INPUT HERE: Input pulled from the HTML dropdown list form 

    truedf = df[ (df['Make'] == make) & (df['Model'] == model)]
    if truedf.empty:
        return 192

    truedf.set_index('Make', inplace=True)
    return truedf.iloc[0]['CO2 Emissions(g/km)']

def home(request):
    return render(request, 'home.html')

def result(request):
    num1 = int(request.GET.get('number1')) if request.GET.get('number1') else 0
    num2 = int(request.GET.get('number2')) if request.GET.get('number2') else 0
    num3 = int(request.GET.get('number3')) if request.GET.get('number3') else 0
    num4 = int(request.GET.get('number4')) if request.GET.get('number4') else 0
    num5 = int(request.GET.get('number5')) if request.GET.get('number5') else 0
    carmake = str(request.GET.get('carmake')).upper() if request.GET.get('carmake') else ''
    carmodel = str(request.GET.get('carmodel')).upper() if request.GET.get('carmodel') else ''

    
    carEmissions = car(carmake, carmodel)
    carEmissions = carEmissions * 0.003548 #convert to lbs/mile
    
    if request.GET.get('calculate') == "":
        ans = (num1 * 105) + (num2 * 105) + (num3 * 113) + (carEmissions * num4) + (num5 * 2700)
    if ans > 45000:
        return render(request, 'aboavg.html', {'ans': ans})
    if ans < 25000:
        return render(request, 'belavg.html', {'ans': ans})
    else:
        return render(request, 'result.html', {'ans': ans})

