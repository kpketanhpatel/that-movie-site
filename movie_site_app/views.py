from django.shortcuts import render, HttpResponse
import requests

def index(request):
    # retrieve info for the home page
    return render(request, 'index.html')


def jmoore_test(request):
    test_query = requests.get('https://itunes.apple.com/search?media=movie&term=action&limit=1').json()
    context = {
        'response': test_query
    }
    return render(request, 'jmoore_test.html', context)