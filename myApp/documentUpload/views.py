from django.http import HttpResponse
from django.shortcuts import render

def createContext():
    return {
        'name': 'kaan',
        'surname': 'ozbudak'
    }

def index(request):
    return render(request, 'documentUpload/index.html', createContext())
    #return HttpResponse("Hello, world. You're at the document upload pages index.")

