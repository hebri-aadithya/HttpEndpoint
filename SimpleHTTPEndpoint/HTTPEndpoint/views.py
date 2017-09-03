from django.shortcuts import render
from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt
from django.http import JsonResponse
import re

''' 
    This method handles incoming requests.
    1. If the request is a POST request: Return "POST Request"
    2. If the request is a GET request:
       a. If the ACCEPT header accepts JSON, return JSON data
       b. If the ACCEPT header does not accept JSON format, return
          Hello, World HTML data
    3. If the request is not a GET or a POST, error message is sent.
'''
@csrf_exempt
def hello(request):
    # Handle POST requests
    if request.method == 'POST':
        return HttpResponse("<p>Post Request</p>")
    # Handle GET requests
    elif request.method == 'GET':
        Accept_header = request.META.get('HTTP_ACCEPT')
        # Check if Accept_header has 'application/json'
        json_obj = re.search(r'application/json', Accept_header)
        # JSON not found
        if json_obj==None:
            text = """<p>Hello, World</p>"""
            return HttpResponse(text)
        # JSON found
        else:
            data = {
                'message': 'Good morning'
            }
            return JsonResponse(data)
    # Handle all other HTTP request methods
    else:
        return HttpResponse("<p>This Request method is not handled.</p>")
