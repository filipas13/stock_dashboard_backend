# ci855o9r01qnrgm31qa0ci855o9r01qnrgm31qag

from django.conf import settings
import requests
import finnhub
from django.http import JsonResponse
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .serializers import StockSerializer

BASE_PATH = "https://finnhub.io/api/v1"
API_KEY = "ci855o9r01qnrgm31qa0ci855o9r01qnrgm31qag"  # Replace with your actual API key

def search_symbol(request):
    query = request.GET.get('q')

    client = finnhub.Client(api_key='ci855o9r01qnrgm31qa0ci855o9r01qnrgm31qag')
    response = client.search(query)

    if 'result' in response:
        return JsonResponse(response['result'], safe=False)
    else:
        message = f"An error has occurred: {response.get('error')}"
        return JsonResponse({'error': message})


    #url = f"{BASE_PATH}/search?q={query}&token={API_KEY}"
    #response = requests.get(url)

    #if response.ok:
    #    return JsonResponse(response.json(), safe=False)
    #else:
    #    message = f"An error has occurred: {response.status_code}"
    #    return JsonResponse({'error': message}, status=response.status_code)

def fetch_stock_details(request, stock_symbol):
    url = f"{BASE_PATH}/stock/profile2?symbol={stock_symbol}&token={API_KEY}"
    response = requests.get(url)

    if response.ok:
        return JsonResponse(response.json(), safe=False)
    else:
        message = f"An error has occurred: {response.status_code}"
        return JsonResponse({'error': message}, status=response.status_code)

def fetch_quote(request, stock_symbol):
    url = f"{BASE_PATH}/quote?symbol={stock_symbol}&token={API_KEY}"
    response = requests.get(url)

    if response.ok:
        return JsonResponse(response.json(), safe=False)
    else:
        message = f"An error has occurred: {response.status_code}"
        return JsonResponse({'error': message}, status=response.status_code)

def fetch_historical_data(request, stock_symbol, resolution, from_timestamp, to_timestamp):
    url = f"{BASE_PATH}/stock/candle?symbol={stock_symbol}&resolution={resolution}&from={from_timestamp}&to={to_timestamp}&token={API_KEY}"
    response = requests.get(url)

    if response.ok:
        return JsonResponse(response.json(), safe=False)
    else:
        message = f"An error has occurred: {response.status_code}"
        return JsonResponse({'error': message}, status=response.status_code)


@api_view(['GET'])
def get_stock_list(request):
    stocks = Stock.objects.all()
    serializer = StockSerializer(stocks, many=True)
    return Response(serializer.data)

def get_stock_quote(request):
    symbol = 'TSLA'  # Replace with the desired stock symbol
    finnhub_client = finnhub.Client(api_key='ci855o9r01qnrgm31qa0ci855o9r01qnrgm31qag')  # Replace 'YOUR_API_KEY' with your actual Finnhub API key
    quote = finnhub_client.quote(symbol)

    # Process the quote data as needed
    # ...

    return JsonResponse(quote)  # Return the quote as a JSON response
