from datetime import date
import json
from urllib.request import urlopen

from django.http import JsonResponse
from django.shortcuts import render, HttpResponse

def converter(request):
    if request.method == 'POST':
        currency_from = request.POST.get('from')
        currency_to = request.POST.get('to')
        amount = request.POST.get('amount')
        today = date.today()

        access_key = '28807aceea1acfc131eafe663afdb3e8'
        url = f'https://api.exchangerate.host/convert?access_key={access_key}&from={currency_from}&to={currency_to}&amount={amount}&date={today}'
        with urlopen(url) as response:
            data = json.loads(response.read().decode("utf-8"))
        result = data['result']
        
        return JsonResponse({'result': result})
    else:
        return render (request, 'converter/home.html')
