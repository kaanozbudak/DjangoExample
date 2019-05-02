from django.http import HttpResponse
from django.shortcuts import render


def create_context():
    return {
        'name': 'kaan',
        'surname': 'ozbudak'
    }


def upload_context():
    return {
        'name': 'kaan',
        'surname': 'ozbudak'
    }


def list_context():
    return {
        'name': 'kaan',
        'surname': 'ozbudak'
    }


def index(request):
    return render(request, 'documentUpload/index.html', create_context())
    # return HttpResponse("Hello, world. You're at the document upload pages index.")


def upload(request):
    return render(request, 'documentUpload/upload.html', upload_context())
    # return HttpResponse("Hello, world. You're at the document upload pages index.")


def list_docs(request):
    return render(request, 'documentUpload/list.html', list_context())
    # return HttpResponse("Hello, world. You're at the document upload pages index.")
