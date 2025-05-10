from django.shortcuts import render, HttpResponse, redirect
from django.http import JsonResponse
import json
import requests

def converter(request):
    access_key = '28807aceea1acfc131eafe663afdb3e8'
    url = f'http://api.exchangerate.host/live?access_key={access_key}'
    response = requests.get(url)
    
    if response.status_code == 200:
        data = response.json()
        data_json = json.dumps(data)
        return HttpResponse(data_json)
    else:
        return HttpResponse('Não foi possível acessar a API externa')